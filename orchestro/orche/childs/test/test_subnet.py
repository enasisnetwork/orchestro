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



def test_OrcheSubnet_cover(
    orche: 'Orche',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    """

    childs = orche.childs
    subnets = childs.subnets


    subnet = subnets[
        'jupiter_domesnet']


    attrs = lattrs(subnet)

    assert attrs == [
        '_OrcheChild__orche',
        '_OrcheChild__name',
        '_OrcheChild__params']


    assert inrepr(
        'subnet.OrcheSubnet',
        subnet)

    assert hash(subnet) > 0

    assert instr(
        'subnet.OrcheSubnet',
        subnet)


    subnet.validate()

    assert subnet.orche

    assert subnet.enable

    assert subnet.name == 'jupiter_domesnet'

    assert subnet.kind == 'subnet'

    assert subnet.params

    assert subnet.groups

    assert subnet.dumped
