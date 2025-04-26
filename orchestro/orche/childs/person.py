"""
Functions and routines associated with Enasis Network System Monitor.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Literal
from typing import Optional
from typing import TYPE_CHECKING

from encommon.types.strings import SPACED

from .child import OrcheChild
from ..models import OrcheModels

if TYPE_CHECKING:
    from ..params import OrchePersonParams



class OrchePerson(OrcheChild):
    """
    Contain the properties regarding the actual user person.
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
            returned += f'@{domain}'

        return returned


    @property
    def display(
        self,
    ) -> str:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        params = self.params
        default = super().display

        first = params.first
        last = params.last

        names: list[str] = []

        if first is not None:
            names.append(first)

        if last is not None:
            names.append(last)

        return (
            SPACED.join(names)
            if len(names)
            else default)
