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
    from ...orche.orche import Orche



def test_InvalidChild(
    orche: 'Orche',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    """

    childs = orche.childs
    systems = childs.systems

    system = systems['ensrv1t']

    name = system.name


    raises = InvalidChild(
        child=system,
        phase='runtime',
        about='about')


    attrs = lattrs(raises)

    assert attrs == [
        'child',
        'about']


    assert inrepr(
        'InvalidChild',
        raises)

    assert isinstance(
        hash(raises), int)

    assert instr(
        f'Child ({name})',
        raises)


    assert str(raises) == (
        f'Child ({name}) '
        'invalid within phase '
        '(runtime) (about)')



def test_InvalidChild_cover() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    raises = InvalidChild(
        child='invalid',
        phase='initial')

    assert str(raises) == (
        'Child (invalid) '
        'invalid within '
        'phase (initial)')
