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



def test_OrchePerson_cover(
    orche: 'Orche',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    """

    childs = orche.childs
    persons = childs.persons


    person = persons[
        'robert_domain']


    attrs = lattrs(person)

    assert attrs == [
        '_OrcheChild__orche',
        '_OrcheChild__name',
        '_OrcheChild__params']


    assert inrepr(
        'person.OrchePerson',
        person)

    assert hash(person) > 0

    assert instr(
        'person.OrchePerson',
        person)


    person.validate()

    assert person.orche

    assert person.enable

    assert person.name == 'robert_domain'

    assert person.kind == 'person'

    assert person.params

    assert not person.groups

    assert person.dumped
