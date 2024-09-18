"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
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
