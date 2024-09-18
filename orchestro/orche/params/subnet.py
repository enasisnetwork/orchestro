"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated

from pydantic import Field

from .child import OrcheChildParams



class OrcheSubnetParams(OrcheChildParams, extra='forbid'):
    """
    Process and validate the Orche configuration parameters.
    """

    subnet: Annotated[
        str,
        Field(...,
              description='IPv4 or IPv6 network subnet',
              min_length=1)]
