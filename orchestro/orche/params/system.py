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



OrcheSystemRealms = Literal[
    'ansible',
    'psuedo']



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
