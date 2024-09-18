"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Any
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field



class OrcheChildParams(BaseModel, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    enable: Annotated[
        bool,
        Field(False,
              description='Determine whether child enabled')]

    inherits: Annotated[
        Optional[list[str]],
        Field(None,
              description='Other configuration to inherit',
              min_length=1)]

    display: Annotated[
        Optional[str],
        Field(None,
              description='Friendly name value for child',
              min_length=1)]

    memberof: Annotated[
        Optional[list[str]],
        Field(None,
              description='Groups child is a member of',
              min_length=1)]


    def __init__(
        # NOCVR
        self,
        /,
        **data: Any,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        inherits = data.get('inherits')
        memberof = data.get('memberof')

        if isinstance(inherits, str):
            data['inherits'] = [inherits]

        if isinstance(memberof, str):
            data['memberof'] = [memberof]

        super().__init__(**data)
