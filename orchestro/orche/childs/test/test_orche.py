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



def test_OrcheChilds(
    orche: 'Orche',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    """

    childs = orche.childs


    attrs = lattrs(childs)

    assert attrs == [
        '_OrcheChilds__orche',
        '_OrcheChilds__systems',
        '_OrcheChilds__persons',
        '_OrcheChilds__subnets',
        '_OrcheChilds__groups']


    assert inrepr(
        'orche.OrcheChilds',
        childs)

    assert isinstance(
        hash(childs), int)

    assert instr(
        'orche.OrcheChilds',
        childs)


    childs.validate()

    assert childs.systems

    assert childs.persons

    assert childs.subnets

    assert childs.groups
