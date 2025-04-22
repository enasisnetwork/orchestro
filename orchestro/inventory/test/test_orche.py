"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from os import environ

from ansible.inventory.data import InventoryData  # type: ignore
from ansible.parsing.dataloader import DataLoader  # type: ignore

from encommon.types import DictStrAny

from ..orche import InventoryModule
from ... import EXAMPLES



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
        'engwf1g1p',
        'engwf1g2p',
        'engwf2g1p',
        'engwf2g2p',
        'ensrv1p',
        'ensrv2p',
        'localhost']

    assert sorted(groups) == [
        'all',
        'jupiter',
        'neptune',
        'orche',
        'roles_enhomie',
        'roles_enrobie',
        'systems',
        'systems_almalinux',
        'systems_openbsd',
        'systems_windows',
        'ungrouped']


    dumped = orche.dumped

    assert len(dumped['hosts']) == 7

    assert len(dumped['groups']) == 11
