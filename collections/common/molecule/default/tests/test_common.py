"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path
from os import environ
from sys import executable
from sys import path as sys_path

sys_path.append(
    f'{Path(executable).parents[1]}'
    '/lib/python3.12/site-packages')

from testinfra.host import Host  # type: ignore



def test_common(
    host: Host,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param molecule_scenario: Fixture for testing scenarios.
    :param capfd: pytest object for capturing print message.
    """

    assert host.check_output('hostname') == 'almalinux-9'
