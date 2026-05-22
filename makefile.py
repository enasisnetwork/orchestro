"""
Operation recipes for managing the projects and execution environment.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.

This file is present within multiple projects, simplifying dependency.
"""



from glob import glob
from pathlib import Path
from typing import Optional

from enbasics import makefile
from enbasics import makeout



def children(
    color: Optional[int] = 7,
) -> None:
    """
    Locate and enumerate Makefiles from recipe directories.

    :param color: Optional color override default ANSI gray.
    """

    makefiles = sorted(
        glob(
            'collections/'
            'ansible_collections'
            '/*/*/playbooks/Makefile')
        + glob(
            'collections/'
            'ansible_collections'
            '/*/*/playbooks/*.mk'))


    for file in makefiles:

        parent = Path(file).parent

        role = (
            parent.parent.name
            if 'collections' in file
            else parent.name)

        if str(file).endswith('.mk'):
            name = Path(file).name
            role += f'/{name[:-3]}'

        makeout(
            f'\n <c37>recipes/'
            f'<c90>{role}<c0>')

        makefile(file, color=color)
