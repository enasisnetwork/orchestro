"""
Functions and routines associated with Enasis Network System Monitor.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Literal
from typing import TYPE_CHECKING

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
        """


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
