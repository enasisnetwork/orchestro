"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from os import environ

from ansible.inventory.data import InventoryData  # type: ignore
from ansible.parsing.dataloader import DataLoader  # type: ignore

from encommon.types import DictStrAny

from .. import EXAMPLES
from ..inventory.orche import InventoryModule



def test_InventoryModule(
    replaces: DictStrAny,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param replaces: Mapping of what to replace in samples.
    """

    environ['orche_paths'] = (
        str(EXAMPLES))

    orche = InventoryModule()

    orche.parse(
        InventoryData(),
        DataLoader(),
        str(EXAMPLES))

    ansinv = orche.inventory
    hosts = ansinv.hosts
    groups = ansinv.groups

    assert sorted(hosts) == [
        'aegaeon',
        'engwf1x1t',
        'engwf1x2t',
        'engwf2x1t',
        'engwf2x2t',
        'ensrv1t',
        'ensrv2t',
        'localhost',
        'meropis']

    assert sorted(groups) == [
        'all',
        'orche',
        'roles_enhomie',
        'roles_enrobie',
        'roles_sslca',
        'saturn',
        'systems',
        'systems_almalinux',
        'systems_fedora',
        'systems_openbsd',
        'systems_windows',
        'ungrouped',
        'uranus']


    dumped = orche.dumped

    assert len(dumped['groups']) == 13

    assert len(dumped['hosts']) == 9
