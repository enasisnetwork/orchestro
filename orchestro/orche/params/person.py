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



OrchePersonRealms = Literal[
    'domain',
    'local',
    'psuedo']



class OrchePersonParams(OrcheChildParams, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    realm: Annotated[
        OrchePersonRealms,
        Field('psuedo',
              description='Logical realm for the object')]

    domain: Annotated[
        Optional[str],
        Field(None,
              description='Domain to which child belongs',
              min_length=1)]

    first: Annotated[
        Optional[str],
        Field(None,
              description='First name for person account',
              min_length=1)]

    last: Annotated[
        Optional[str],
        Field(None,
              description='Last name for person account',
              min_length=1)]


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
                'domain',
                'first',
                'last']

            for key in parsable:

                value = data.get(key)

                if value is None:
                    continue

                value = _parse(value)

                data[key] = value


        super().__init__(
            _parse, **data)
