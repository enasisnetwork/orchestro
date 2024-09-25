"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING

from encommon.types import inrepr
from encommon.types import instr
from encommon.types import lattrs

from ..param import InvalidParam

if TYPE_CHECKING:
    from ...orche import Orche



def test_InvalidParam(
    orche: 'Orche',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    """

    childs = orche.childs
    systems = childs.systems

    system = systems['ensrv1p']


    raises = InvalidParam(
        error='invalid',
        about='about',
        child=system,
        param='param',
        value='value')


    attrs = lattrs(raises)

    assert attrs == [
        'error',
        'about',
        'child',
        'param',
        'value']


    assert inrepr(
        'InvalidParam',
        raises)

    assert isinstance(
        hash(raises), int)

    assert instr(
        'Error (invalid)',
        raises)


    assert str(raises) == (
        'Error (invalid) '
        'param (param) '
        'value (value) child '
        '(OrcheSystem/ensrv1p)'
        ' (about)')
