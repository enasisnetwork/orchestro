"""
Functions and routines associated with Enasis Network System Monitor.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Literal
from typing import Optional
from typing import TYPE_CHECKING

from encommon.types import DictStrAny
from encommon.types import NCNone

from .child import OrcheChild
from ..models import OrcheModels

if TYPE_CHECKING:
    from ..params import OrcheSystemParams



class OrcheSystem(OrcheChild):
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


    @property
    def kind(
        self,
    ) -> Literal['system']:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return 'system'


    @property
    def params(
        self,
    ) -> 'OrcheSystemParams':
        """
        Return the Pydantic model containing the configuration.

        :returns: Pydantic model containing the configuration.
        """

        model = (
            OrcheModels
            .system())

        params = super().params

        assert isinstance(
            params, model)

        return params


    @property
    def realm(
        self,
    ) -> Optional[str]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.params.realm


    @property
    def domain(
        self,
    ) -> Optional[str]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.params.domain


    @property
    def fqdn(
        self,
    ) -> str:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        returned = self.name
        domain = self.domain

        if domain is not None:
            returned += f'.{domain}'

        return returned


    @property
    def ansible(
        self,
    ) -> Optional[DictStrAny]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        ansible = self.params.ansible

        if ansible is not None:
            return ansible.endumped

        return NCNone


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
            'kind': self.kind,
            'realm': self.realm,
            'domain': self.domain,
            'fqdn': self.fqdn}
