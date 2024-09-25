"""
Functions and routines associated with Enasis Network System Monitor.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Literal
from typing import TYPE_CHECKING

from encommon.parse import isvalid_ip

from .child import OrcheChild
from ..models import OrcheModels
from ...utils import InvalidParam

if TYPE_CHECKING:
    from ..params import OrcheSubnetParams



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
