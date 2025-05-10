"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""


from pathlib import Path
from os import environ
from sys import executable

from encommon.utils.stdout import strip_ansi

from _pytest.capture import CaptureFixture
from pytest_ansible.molecule import MoleculeScenario

from . import SAMPLES



def test_common(
    molecule_scenario: MoleculeScenario,
    capfd: CaptureFixture[str],
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param molecule_scenario: Fixture for testing scenarios.
    :param capfd: pytest object for capturing print message.
    """

    environ['PATH'] = (
        f'{Path(executable).parent}'
        f':{environ["PATH"]}')

    proc = molecule_scenario.test()

    assert proc.returncode == 0


    stdout, stderr = (
        capfd.readouterr())

    stdout = strip_ansi(stdout)

    expect = (
        (SAMPLES / 'overview.txt')
        .read_text())

    assert expect in stdout
