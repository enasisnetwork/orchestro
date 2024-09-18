"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
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
