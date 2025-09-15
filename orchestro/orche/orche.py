"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from copy import deepcopy
from functools import cached_property
from typing import Any
from typing import Optional
from typing import TYPE_CHECKING

from encommon.types import DictStrAny
from encommon.types import clsname
from encommon.types import sort_dict

from .addons import OrcheJinja2
from .addons import OrcheLogger
from .childs import OrcheChilds

if TYPE_CHECKING:
    from .config import OrcheConfig
    from .params import OrcheParams



class Orche:
    """
    Interact with chat networks and integrate using plugins.

    :param config: Primary class instance for configuration.
    """

    __config: 'OrcheConfig'

    __logger: OrcheLogger
    __jinja2: OrcheJinja2

    __childs: OrcheChilds


    def __init__(
        self,
        config: 'OrcheConfig',
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        config.logger.log_d(
            base=clsname(self),
            status='initial')

        self.__config = config

        self.__logger = (
            OrcheLogger(self))

        self.__jinja2 = (
            OrcheJinja2(self))

        self.__childs = (
            OrcheChilds(self))

        self.childs.validate()

        config.logger.log_d(
            base=clsname(self),
            status='created')


    @property
    def config(
        self,
    ) -> 'OrcheConfig':
        """
        Return the Config instance containing the configuration.

        :returns: Config instance containing the configuration.
        """

        return self.__config


    @property
    def logger(
        self,
    ) -> OrcheLogger:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__logger


    @property
    def jinja2(
        self,
    ) -> OrcheJinja2:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__jinja2


    @property
    def childs(
        self,
    ) -> OrcheChilds:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.__childs


    @property
    def params(
        self,
    ) -> 'OrcheParams':
        """
        Return the Pydantic model containing the configuration.

        :returns: Pydantic model containing the configuration.
        """

        return self.config.params


    @property
    def dryrun(
        self,
    ) -> bool:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.params.dryrun


    @cached_property
    def kvparsed(
        self,
    ) -> dict[str, Any]:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        params = self.params
        jinja2 = self.jinja2

        values = jinja2.parse(
            params.kvparsed,
            {'orche': self})

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
    def dumped(
        self,
    ) -> DictStrAny:
        """
        Return the facts about the attributes from the instance.

        :returns: Facts about the attributes from the instance.
        """

        params = deepcopy(
            self.params.endumped)

        childs = deepcopy(
            self.childs.dumped)

        items = childs.items()

        for key, value in items:
            params[key] = value

        return params


    def j2parse(
        self,
        value: Any,  # noqa: ANN401
        statics: Optional[DictStrAny] = None,
        literal: bool = True,
    ) -> Any:  # noqa: ANN401
        """
        Return the provided input using the Jinja2 environment.

        :param value: Input that will be processed and returned.
        :param statics: Additional values available for parsing.
        :param literal: Determine if Python objects are evaled.
        :returns: Provided input using the Jinja2 environment.
        """

        return self.__jinja2.parse(
            value, statics, literal)
