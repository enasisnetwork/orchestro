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
    from ..params import OrchePersonParams



class OrchePerson(OrcheChild):
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
    ) -> Literal['person']:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return 'person'


    @property
    def params(
        self,
    ) -> 'OrchePersonParams':
        """
        Return the Pydantic model containing the configuration.

        :returns: Pydantic model containing the configuration.
        """

        model = (
            OrcheModels
            .person())

        params = super().params

        assert isinstance(
            params, model)

        return params
