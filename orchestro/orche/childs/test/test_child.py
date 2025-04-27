"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...orche import Orche



def test_OrcheChild_cover(
    orche: 'Orche',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    """

    childs = orche.childs
    subnets = childs.subnets

    child1 = subnets[
        'uranus_domesnet']

    child2 = subnets[
        'saturn_domesnet']


    sort = [child1, child2]

    assert sorted(sort) == [
        child2, child1]
