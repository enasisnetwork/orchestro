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



def test_OrcheGroup(
    orche: 'Orche',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    """

    childs = orche.childs
    groups = childs.groups


    group = groups['jupiter']


    attrs = lattrs(group)

    assert attrs == [
        '_OrcheChild__orche',
        '_OrcheChild__name',
        '_OrcheChild__params']


    assert inrepr(
        'group.OrcheGroup',
        group)

    assert isinstance(
        hash(group), int)

    assert instr(
        'group.OrcheGroup',
        group)


    group.validate()

    assert group.orche

    assert group.enable

    assert group.display

    assert group.name == 'jupiter'

    assert group.kind == 'group'

    assert group.params

    assert not group.groups

    assert group.dumped


    assert group.realm

    assert not group.ansible
