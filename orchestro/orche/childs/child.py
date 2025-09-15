"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from functools import cached_property
from typing import Any
from typing import Optional
from typing import TYPE_CHECKING

from encommon.types import DictStrAny
from encommon.types import sort_dict

from ...utils import InvalidParam

if TYPE_CHECKING:
    from .group import OrcheGroup
    from ..common import OrcheKinds
    from ..orche import Orche
    from ..params import OrcheChildParams



class OrcheChild:
    """
    Parent object for child objects within the project base.

    :param orche: Primary class instance for Orchestrations.
    :param name: Name of the object within the Orche config.
    :param params: Parameters used to instantiate the class.
    """

    __orche: 'Orche'

    __name: str
    __params: 'OrcheChildParams'


    def __init__(
        self,
        orche: 'Orche',
        name: str,
        params: 'OrcheChildParams',
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        orche.logger.log_d(
            base=self,
            name=name,
            status='initial')

        self.__orche = orche
        self.__name = name
        self.__params = params

        self.__post__()

        orche.logger.log_d(
            base=self,
            name=name,
            status='created')


    def __post__(
        self,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
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

        orche = self.orche
        params = self.params
        mmbrof = params.memberof
        groups = (
            orche.params
            .groups or {})


        def _memberof() -> None:

            assert mmbrof is not None

            for name in mmbrof:

                if name in groups:
                    continue

                raise InvalidParam(
                    param='memberof',
                    value=name,
                    error='noexist')


        if mmbrof is not None:
            _memberof()


    def __lt__(
        self,
        other: 'OrcheChild',
    ) -> bool:
        """
        Built-in method for comparing this instance with another.

        .. note::
           Useful with sorting to influence consistent output.

        :param other: Other value being compared with instance.
        :returns: Boolean indicating outcome from the operation.
        """

        name = self.name
        _name = other.name

        return name < _name


    @property
    def orche(
        self,
    ) -> 'Orche':
        """
        Return the Orche instance to which the instance belongs.

        :returns: Orche instance to which the instance belongs.
        """

        return self.__orche


    @property
    def enable(
        self,
    ) -> bool:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.params.enable


    @property
    def name(
        self,
    ) -> str:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__name


    @property
    def kind(
        self,
    ) -> 'OrcheKinds':
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        raise NotImplementedError


    @property
    def params(
        self,
    ) -> 'OrcheChildParams':
        """
        Return the Pydantic model containing the configuration.

        :returns: Pydantic model containing the configuration.
        """

        return self.__params


    @property
    def inherits(
        self,
    ) -> Optional[list[str]]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.params.inherits


    @property
    def display(
        self,
    ) -> str:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        params = self.params
        display = params.display

        return (
            display if display
            else self.name)


    @property
    def about(
        self,
    ) -> Optional[str]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.params.about


    @property
    def memberof(
        self,
    ) -> Optional[list[str]]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.params.memberof


    @cached_property
    def kvparsed(
        self,
    ) -> dict[str, Any]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        orche = self.orche
        params = self.params
        jinja2 = orche.jinja2

        kind = f'orche_{self.kind}'

        values = jinja2.parse(
            params.kvparsed,
            {kind: self})

        assert isinstance(values, dict)

        return sort_dict(values)


    @cached_property
    def kvopaque(
        self,
    ) -> dict[str, Any]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        params = self.params
        values = params.kvopaque

        assert isinstance(values, dict)

        return sort_dict(values)


    @property
    def groups(
        self,
    ) -> list['OrcheGroup']:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        params = self.params
        names = params.memberof

        groups = (
            self.orche.childs
            .groups)

        childs: set['OrcheGroup'] = set()

        if names is None:
            return list(childs)

        for name in names:

            child = groups[name]

            if not child.enable:
                continue

            childs.add(child)

        return list(childs)


    @property
    def dumped(
        self,
    ) -> DictStrAny:
        """
        Return the facts about the attributes from the instance.

        :returns: Facts about the attributes from the instance.
        """

        return {
            'enable': self.enable,
            'kind': self.kind,
            'name': self.name,
            'inherits': self.inherits,
            'display': self.display,
            'about': self.about,
            'memberof': self.memberof,
            'kvparsed': self.kvparsed,
            'kvopaque': self.kvopaque}


    @property
    def ansibout(
        self,
    ) -> DictStrAny:
        """
        Return the facts about the attributes from the instance.

        :returns: Facts about the attributes from the instance.
        """

        dumped = self.dumped

        return {
            k: v for k, v
            in dumped.items()
            if k != 'params'}
