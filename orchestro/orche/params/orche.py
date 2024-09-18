"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Optional

from encommon.config import Params

from pydantic import Field

from .group import OrcheGroupParams
from .person import OrchePersonParams
from .subnet import OrcheSubnetParams
from .system import OrcheSystemParams



class OrcheParams(Params, extra='forbid'):
    """
    Process and validate the core configuration parameters.
    """

    database: Annotated[
        str,
        Field('sqlite:///:memory:',
              description='Database connection string',
              min_length=1)]

    dryrun: Annotated[
        bool,
        Field(False,
              description='Determine if changes applied')]

    systems: Annotated[
        Optional[dict[str, OrcheSystemParams]],
        Field(None,
              description='Parameters for Orche systems',
              min_length=1)]

    persons: Annotated[
        Optional[dict[str, OrchePersonParams]],
        Field(None,
              description='Parameters for Orche persons',
              min_length=1)]

    subnets: Annotated[
        Optional[dict[str, OrcheSubnetParams]],
        Field(None,
              description='Parameters for Orche subnets',
              min_length=1)]

    groups: Annotated[
        Optional[dict[str, OrcheGroupParams]],
        Field(None,
              description='Parameters for Orche groups',
              min_length=1)]
