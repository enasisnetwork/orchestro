"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING

from encommon.types import inrepr
from encommon.types import instr
from encommon.types import lattrs

if TYPE_CHECKING:
    from ...orche import Orche



def test_OrcheSystem_cover(
    orche: 'Orche',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    """

    childs = orche.childs
    systems = childs.systems


    system = systems['ensrv1p']


    attrs = lattrs(system)

    assert attrs == [
        '_OrcheChild__orche',
        '_OrcheChild__name',
        '_OrcheChild__params']


    assert inrepr(
        'system.OrcheSystem',
        system)

    assert isinstance(
        hash(system), int)

    assert instr(
        'system.OrcheSystem',
        system)


    system.validate()

    assert system.orche

    assert system.enable

    assert system.name == 'ensrv1p'

    assert system.kind == 'system'

    assert system.params

    assert system.groups

    assert system.dumped


    assert system.domain
