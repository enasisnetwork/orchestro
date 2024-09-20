"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Any
from typing import Literal

from pydantic import Field

from .child import OrcheChildParams



OrcheGroupRealms = Literal[
    'domain',
    'local',
    'site',
    'zone',
    'ansible',
    'psuedo']



class OrcheGroupParams(OrcheChildParams, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    realm: Annotated[
        OrcheGroupRealms,
        Field('ansible',
              description='Logical realm for the object')]


    def __init__(
        # NOCVR
        self,
        /,
        **data: Any,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        parse = data.get('_parse')


        if parse is not None:

            parsable = ['realm']

            for key in parsable:

                value = data.get(key)

                if value is None:
                    continue

                data[key] = (
                    parse(value))


        super().__init__(**data)
