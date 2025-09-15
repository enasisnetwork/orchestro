"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Any
from typing import Callable
from typing import Optional

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

    macpref: Annotated[
        Optional[str],
        Field(None,
              description='Optional prefix for MAC address',
              min_length=2,
              max_length=2,
              pattern=r'^[\da-fA-F]+$')]

    gateway: Annotated[
        Optional[str],
        Field(None,
              description='Optional gateway for the subnet',
              min_length=1)]

    resolve: Annotated[
        Optional[list[str]],
        Field(None,
              description='Optional resolvers for subnet',
              min_length=1)]

    ntpsync: Annotated[
        Optional[list[str]],
        Field(None,
              description='Optional NTP server for subnet',
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
                'subnet',
                'macpref',
                'resolve',
                'ntpsync']

            for key in parsable:

                value = data.get(key)

                if value is None:
                    continue

                value = _parse(value)

                data[key] = value


        listable = [
            'resolve',
            'ntpsync']

        for key in listable:

            value = data.get(key)

            if value is None:
                continue

            if isinstance(value, list):
                continue

            data[key] = [value]


        super().__init__(
            _parse, **data)
