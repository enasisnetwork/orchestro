"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING

from encommon.types import inrepr
from encommon.types import instr
from encommon.types import lattrs

from ..child import InvalidChild

if TYPE_CHECKING:
    from ...orche import Orche



def test_InvalidChild() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    raises = InvalidChild(
        child='invalid',
        phase='initial')


    attrs = lattrs(raises)

    assert attrs == [
        'child',
        'about']


    assert inrepr(
        'InvalidChild',
        raises)

    assert hash(raises) > 0

    assert instr(
        'Child (invalid)',
        raises)


    assert str(raises) == (
        'Child (invalid) '
        'invalid within '
        'phase (initial)')



def test_InvalidChild_cover(
    orche: 'Orche',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    """

    childs = orche.childs
    systems = childs.systems

    system = systems['ensrv1p']


    raises = InvalidChild(
        child=system,
        phase='runtime',
        about='about')

    name = system.name

    assert str(raises) == (
        f'Child ({name}) '
        'invalid within phase '
        '(runtime) (about)')
