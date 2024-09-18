"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING

from _pytest.logging import LogCaptureFixture

from encommon.types import inrepr
from encommon.types import instr
from encommon.types import lattrs

if TYPE_CHECKING:
    from ...orche import Orche



def test_OrcheLogger(
    orche: 'Orche',
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    """

    logger = orche.logger


    attrs = lattrs(logger)

    assert attrs == [
        '_OrcheLogger__orche']


    assert inrepr(
        'logger.OrcheLogger',
        logger)

    assert hash(logger) > 0

    assert instr(
        'logger.OrcheLogger',
        logger)



def test_OrcheLogger_message(
    orche: 'Orche',
    caplog: LogCaptureFixture,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    :param caplog: pytest object for capturing log message.
    """

    logger = orche.logger


    logger.start()

    logger.log_d(about='pytest')
    logger.log_c(about='pytest')
    logger.log_e(about='pytest')
    logger.log_i(about='pytest')
    logger.log_w(about='pytest')

    logger.log(
        level='debug',
        about='pytest')

    logger.stop()

    output = caplog.record_tuples

    assert len(output) == 6

    logger.log_d(about='pytest')
    logger.log_c(about='pytest')
    logger.log_e(about='pytest')
    logger.log_i(about='pytest')
    logger.log_w(about='pytest')

    output = caplog.record_tuples

    assert len(output) == 6



def test_OrcheLogger_cover(
    orche: 'Orche',
    caplog: LogCaptureFixture,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param orche: Primary class instance for Orchestrations.
    :param caplog: pytest object for capturing log message.
    """

    logger = orche.logger
    childs = orche.childs
    systems = childs.systems


    system = systems['ensrv1p']


    logger.log_i(base=orche)
    logger.log_i(item=orche)
    logger.log_i(name=system)
