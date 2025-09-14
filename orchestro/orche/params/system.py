"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Any
from typing import Callable
from typing import Literal
from typing import Optional

from pydantic import Field

from .child import OrcheChildParams
from .common import OrcheParamsModel



OrcheSystemRealms = Literal[
    'ansible',
    'psuedo']



class OrcheSystemAnsibleParams(OrcheParamsModel, extra='allow'):
    """
    Process and validate the Orche configuration parameters.
    """



class OrcheSystemParams(OrcheChildParams, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    realm: Annotated[
        OrcheSystemRealms,
        Field('ansible',
              description='Logical realm for the object')]

    domain: Annotated[
        Optional[str],
        Field(None,
              description='Domain to which child belongs',
              min_length=1)]

    ansible: Annotated[
        Optional[OrcheSystemAnsibleParams],
        Field(None,
              description='Variables provided to Ansible')]


    def __init__(
        # NOCVR
        self,
        /,
        _parse: Optional[Callable[..., Any]] = None,
        **data: Any,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """


        if _parse is not None:

            parsable = [
                'realm',
                'domain']

            for key in parsable:

                value = data.get(key)

                if value is None:
                    continue

                value = _parse(value)

                data[key] = value



        super().__init__(
            _parse=_parse,
            **data)
