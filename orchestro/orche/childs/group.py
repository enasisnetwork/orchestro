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
    from ..params import OrcheGroupParams



class OrcheGroup(OrcheChild):
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
    ) -> Literal['group']:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return 'group'


    @property
    def params(
        self,
    ) -> 'OrcheGroupParams':
        """
        Return the Pydantic model containing the configuration.

        :returns: Pydantic model containing the configuration.
        """

        model = (
            OrcheModels
            .group())

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
    def ansible(
        self,
    ) -> Optional[DictStrAny]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        ansible = self.params.ansible

        if ansible is not NCNone:
            return ansible.endumped

        return None


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
            'realm': self.realm}
