"""
Functions and routines associated with Enasis Network System Monitor.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Literal
from typing import Optional
from typing import TYPE_CHECKING

from encommon.parse import Network
from encommon.parse import insubnet_ip
from encommon.parse import isvalid_ip
from encommon.types import DictStrAny

from .child import OrcheChild
from ..models import OrcheModels
from ...utils import InvalidParam

if TYPE_CHECKING:
    from ..params import OrcheSubnetParams



class OrcheSubnetAddress(Network):
    """
    Convert the network into the various supported formats.

    :param source: Network IPv4 or IPv6 network or address.
    :param params: Parameters used to instantiate the child.
    """

    macpref: Optional[str]
    gateway: Optional[str]
    resolve: Optional[list[str]]
    ntpsync: Optional[list[str]]


    def __init__(
        self,
        source: str,
        params: 'OrcheSubnetParams',
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        super().__init__(source)

        self.macpref = (
            params.macpref
            if params.macpref
            else None)

        self.gateway = (
            params.gateway
            if params.gateway
            else None)

        self.resolve = (
            params.resolve
            if params.resolve
            else None)

        self.ntpsync = (
            params.ntpsync
            if params.ntpsync
            else None)


    @property
    def hwaddr(
        self,
    ) -> str:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        hwaddr = super().hwaddr

        if not self.macpref:
            return hwaddr  # NOCVR

        hwaddr = (
            f'{self.macpref}'
            f'-{hwaddr[3:]}')

        return hwaddr


    @property
    def dumped(
        self,
    ) -> DictStrAny:
        """
        Return the facts about the attributes from the instance.

        :returns: Facts about the attributes from the instance.
        """

        return {
            x: getattr(self, x)
            for x in [

                # from default class
                'version',
                'cidr',
                'address',
                'address_cidr',
                'address_host',
                'network',
                'network_cidr',
                'broadcast',
                'padded',
                'reverse',
                'hwaddr',
                'netmask',
                'ispublic',
                'isprivate',
                'islinklocal',
                'islocalhost',

                # from class override
                'gateway',
                'resolve',
                'ntpsync']}



class OrcheSubnet(OrcheChild):
    """
    Integrate with the Orche routine and perform operations.
    """


    def validate(
        self,
    ) -> None:
        """
        Perform advanced validation on the parameters provided.

        .. note::
           Works differently than other projects because these
           children all have one common attribute between them.
        """

        super().validate()

        params = self.params
        subnet = params.subnet

        if not isvalid_ip(subnet):

            raise InvalidParam(
                param='subnet',
                value=subnet,
                error='invalid')


    @property
    def kind(
        self,
    ) -> Literal['subnet']:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return 'subnet'


    @property
    def params(
        self,
    ) -> 'OrcheSubnetParams':
        """
        Return the Pydantic model containing the configuration.

        :returns: Pydantic model containing the configuration.
        """

        model = (
            OrcheModels
            .subnet())

        params = super().params

        assert isinstance(
            params, model)

        return params


    @property
    def subnet(
        self,
    ) -> str:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.params.subnet


    @property
    def dumped(
        self,
    ) -> DictStrAny:
        """
        Return the facts about the attributes from the instance.

        :returns: Facts about the attributes from the instance.
        """

        dumped = super().dumped

        return dumped | {
            'subnet': self.subnet}


    def address(
        self,
        address: str,
    ) -> OrcheSubnetAddress:
        """
        Return the facts about the attributes from the instance.

        :returns: Facts about the attributes from the instance.
        """

        subn = Network(self.subnet)
        cidr = subn.cidr
        addr = Network(address)

        if addr.cidr == 32:
            addr = Network(
                f'{addr.address}'
                f'/{subn.cidr}')

        assert addr.cidr == cidr, (
            f'Address ({address}) CIDR'
            f' mismatch ({self.subnet})')

        assert self.enable, (
            f'Subnet ({self.subnet})'
            ' is currently disabled')


        insubnet = insubnet_ip(
            addr.address,
            subn.address_cidr)

        assert insubnet, (
            f'Address ({address}) not in'
            f' subnet ({self.subnet})')


        return OrcheSubnetAddress(
            addr.address_cidr,
            params=self.params)





# maybe a function that returns special Network object?

# set subnets = orche_childs.subnets
# set subnet = subnets.saturn_internal
# set addr = subnet.address("172.18.11.40")

# set hwaddr = addr.hwaddr
# set gateway = addr.gateway <
# set resolve = addr.resolve <
# set ntpsync = addr.ntpsync <
