"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from encommon.types import DictStrAny
from encommon.types import inrepr
from encommon.types import instr
from encommon.types import lattrs
from encommon.utils import load_sample
from encommon.utils import prep_sample
from encommon.utils.sample import ENPYRWS

from . import SAMPLES
from ..config import OrcheConfig
from ..orche import Orche



def test_Orche(
    orche: Orche,
    replaces: DictStrAny,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    :param replaces: Mapping of what to replace in samples.
    """


    attrs = lattrs(orche)

    assert attrs == [
        '_Orche__config',
        '_Orche__logger',
        '_Orche__childs']


    assert inrepr(
        'orche.Orche',
        orche)

    assert isinstance(
        hash(orche), int)

    assert instr(
        'orche.Orche',
        orche)


    assert orche.config

    assert orche.logger

    assert orche.childs

    assert orche.params

    assert not orche.dryrun


    sample_path = (
        SAMPLES / 'dumped.json')

    sample = load_sample(
        path=sample_path,
        update=ENPYRWS,
        content=orche.dumped,
        replace=replaces)

    expect = prep_sample(
        content=orche.dumped,
        replace=replaces)

    assert expect == sample



def test_Orche_cover(
) -> None:
    """
    Perform various tests associated with relevant routines.
    """

    Orche(OrcheConfig())
