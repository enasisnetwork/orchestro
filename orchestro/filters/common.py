"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from encommon.parse.jinja2 import DEFAULT
from encommon.parse.jinja2 import FILTERS



class FilterModule:
    """
    Define filter functions available with Ansible routines.
    """


    def filters(
        # NOCVR
        self,
    ) -> FILTERS:
        """
        Return the filter functions for use in Ansible routines.

        :returns: Filter functions for use in Ansible routines.
        """

        return DEFAULT
