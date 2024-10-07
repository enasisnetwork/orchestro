"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path

from encommon.types import DictStrAny
from encommon.utils import save_text

from pytest import fixture

from . import EXAMPLES
from . import PROJECT
from .orche import Orche
from .orche import OrcheConfig



def config_factory(
    tmp_path: Path,
) -> OrcheConfig:
    """
    Construct the instance for use in the downstream tests.

    :param tmp_path: pytest object for temporal filesystem.
    :returns: Newly constructed instance of related class.
    """

    content = (
        f"""

        enconfig:
          paths:
            - {EXAMPLES}
            - {tmp_path}/orche

        enlogger:
          stdo_level: info

        database: >-
          sqlite:///{tmp_path}/db

        """)

    config_path = (
        tmp_path / 'config.yml')

    save_text(
        config_path, content)

    sargs = {
        'config': config_path,
        'dryrun': False,
        'console': True,
        'debug': True}

    return OrcheConfig(sargs)



@fixture
def config(
    tmp_path: Path,
) -> OrcheConfig:
    """
    Construct the instance for use in the downstream tests.

    :param tmp_path: pytest object for temporal filesystem.
    :returns: Newly constructed instance of related class.
    """

    return config_factory(tmp_path)



@fixture
def replaces(
    tmp_path: Path,
) -> DictStrAny:
    """
    Return the complete mapping of what replaced in sample.

    :param tmp_path: pytest object for temporal filesystem.
    :returns: Complete mapping of what replaced in sample.
    """

    return {
        'PROJECT': PROJECT,
        'TMPPATH': tmp_path}



def orche_factory(
    config: OrcheConfig,
) -> Orche:
    """
    Construct the instance for use in the downstream tests.

    :param config: Primary class instance for configuration.
    :returns: Newly constructed instance of related class.
    """

    return Orche(config)



@fixture
def orche(
    config: OrcheConfig,
) -> Orche:
    """
    Construct the instance for use in the downstream tests.

    :param config: Primary class instance for configuration.
    :returns: Newly constructed instance of related class.
    """

    return orche_factory(config)
