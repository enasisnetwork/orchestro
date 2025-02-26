"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from encommon.parse.jinja2 import DEFAULT
from encommon.parse.jinja2 import FILTERS



class FilterModule:
    """
    Define the filter plugin functions available to the Ansible routines.
    """


    def filters(
        # NOCVR
        self,
    ) -> FILTERS:
        """
        Return the filter plugin functions available to Ansible routines.

        :returns: Filter plugin functions available to Ansible routines.
        """

        return DEFAULT
