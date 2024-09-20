"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Any
from typing import Literal
from typing import Optional

from encommon.types import BaseModel

from pydantic import Field

from .child import OrcheChildParams



OrcheSystemRealms = Literal[
    'ansible',
    'psuedo']



class OrcheSystemAnsibleParams(BaseModel, extra='allow'):
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
        **data: Any,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        parse = data.get('_parse')


        if parse is not None:

            parsable = [
                'realm',
                'domain']

            for key in parsable:

                value = data.get(key)

                if value is None:
                    continue

                data[key] = (
                    parse(value))


        super().__init__(**data)
