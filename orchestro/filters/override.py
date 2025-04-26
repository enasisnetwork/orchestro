"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path

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

        return {'basename': basename}



def basename(
    path: Path | str,
    parents: int = 0,
) -> str:
    """
    Return the file name optionally including their parents.

    :param path: Complete or relative path for processing.
    :param parents: Optional include the additional parents.
    :returns: File name optionally including their parents.
    """

    if not path:
        raise Exception(
            'There was no path'
            'given to filter')

    path = Path(path)

    parts = list(
        path.parts)

    parts = [
        x for x in parts
        if x and x != '/']

    if not parts:
        raise Exception(
            'There is no file'
            ' within the path')

    count = min(
        parents + 1,
        len(parts))

    result = parts[-count:]

    return str(
        Path(*result))
