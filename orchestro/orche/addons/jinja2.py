"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING

from encommon.parse import Jinja2
from encommon.parse.jinja2 import FILTERS
from encommon.types import DictStrAny

if TYPE_CHECKING:
    from ..orche import Orche



class OrcheJinja2(Jinja2):
    """
    Parse the provided input and intelligently return value.

    :param orche: Primary class instance for Orchestrations.
    """


    def __init__(
        self,
        orche: 'Orche',
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        statics: DictStrAny = {
            'orche': orche}

        filters: FILTERS = {}

        super().__init__(
            statics=statics,
            filters=filters)
