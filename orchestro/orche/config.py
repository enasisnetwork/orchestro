"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from copy import deepcopy
from typing import Optional
from typing import get_args

from encommon.config import Config
from encommon.config import Params
from encommon.types import DictStrAny
from encommon.types import dedup_list
from encommon.types import delate
from encommon.types import merge_dicts
from encommon.utils.common import PATHABLE

from .common import OrcheKinds
from .params import OrcheParams



class OrcheConfig(Config):
    """
    Contain the configurations from the arguments and files.

    :param sargs: Additional arguments on the command line.
    :param files: Complete or relative path to config files.
    :param paths: Complete or relative path to config paths.
    :param cargs: Configuration arguments in dictionary form,
        which will override contents from the config files.
    """


    def __init__(
        self,
        sargs: Optional[DictStrAny] = None,
        files: Optional[PATHABLE] = None,
        paths: Optional[PATHABLE] = None,
        cargs: Optional[DictStrAny] = None,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        sargs = dict(sargs or {})
        cargs = dict(cargs or {})


        _console = (
            sargs.get('console'))

        _debug = (
            sargs.get('debug'))

        key = 'enlogger/stdo_level'

        if _console is True:
            cargs[key] = 'info'

        if _debug is True:
            cargs[key] = 'debug'


        if 'config' in sargs:
            files = sargs['config']


        _dryrun = (
            sargs.get('dryrun'))

        if _dryrun is not None:
            cargs['dryrun'] = _dryrun


        super().__init__(
            files=files,
            paths=paths,
            cargs=cargs,
            sargs=sargs,
            model=OrcheParams)

        self.merge_params()


    @property
    def params(
        self,
    ) -> OrcheParams:
        """
        Return the Pydantic model containing the configuration.

        .. warning::
           This method completely overrides the parent but is
           based on that code, would be unfortunate if upstream
           changes meant this breaks or breaks something else.

        :returns: Pydantic model containing the configuration.
        """

        params = self.__params

        if params is not None:

            assert isinstance(
                params, OrcheParams)

            return params


        basic = self.basic

        enconfig = (
            basic.get('enconfig'))

        enlogger = (
            basic.get('enlogger'))

        encrypts = (
            basic.get('encrypts'))

        basic = {
            'enconfig': enconfig,
            'enlogger': enlogger,
            'encrypts': encrypts}

        params = (
            self.model(**basic))

        assert isinstance(
            params, OrcheParams)


        self.__params = params

        return self.__params


    def merge_params(
        self,
    ) -> None:
        """
        Update the Pydantic model containing the configuration.
        """

        merge = self.merge
        jinja2 = self.jinja2

        jinja2.set_static(
            'source', merge)

        parse = jinja2.parse

        params = self.model(
            parse, **merge)

        assert isinstance(
            params, OrcheParams)

        (jinja2
         .set_static('source'))


        dumped = params.endumped


        inheritance(dumped)


        params = (
            self.model(**dumped))

        assert isinstance(
            params, OrcheParams)


        self.__params = params


    @property
    def __params(
        self,
    ) -> Optional[Params]:
        """
        Return the Pydantic model containing the configuration.

        :returns: Pydantic model containing the configuration.
        """

        return self._Config__params


    @__params.setter
    def __params(
        self,
        value: Params,
    ) -> None:
        """
        Update the value for the attribute from class instance.
        """

        self._Config__params = value



def inheritance(
    dumped: DictStrAny,
) -> None:
    """
    Perform the inheritance after resolving the inheritance.

    :param dumped: Source contents which will be processed.
    """


    def _resolved(
        source: DictStrAny,
    ) -> None:

        names: list[str] = []

        inhrts = source['inherits']

        if inhrts is None:
            return None

        for name in inhrts:

            names.append(name)

            _inhrts = (
                dumped[key][name]
                .get('inherits'))

            if _inhrts is None:
                continue

            names.extend(_inhrts)

        final = (
            dedup_list(names)
            or None)

        source['inherits'] = final


    def _inherits(
        source: DictStrAny,
    ) -> None:

        inhrts = source['inherits']

        if inhrts is None:
            return None

        for name in inhrts:

            _inhrt = origin[name]

            inhrt = deepcopy(_inhrt)

            delate(inhrt, 'inherits')
            delate(inhrt, 'enable')

            merge_dicts(
                dict1=source,
                dict2=inhrt,
                force=None)

        dedup_list(
            source['inherits'])


    kinds = get_args(OrcheKinds)

    for kind in kinds:

        key = f'{kind}s'

        _dumped = dumped.get(key)

        if _dumped is None:
            continue

        origin = deepcopy(_dumped)

        items = _dumped.items()

        for name, source in items:
            _resolved(source)

        for name, source in items:
            _inherits(source)
