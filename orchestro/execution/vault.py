"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from argparse import ArgumentParser
from os import environ
from sys import argv as sys_argv
from sys import stdout
from typing import Optional

from encommon.types import DictStrAny

from ..orche import OrcheConfig



def arguments(
    args: Optional[list[str]] = None,
) -> DictStrAny:
    """
    Construct arguments which are associated with the file.

    :param args: Override the source for the main arguments.
    :returns: Construct arguments from command line options.
    """

    parser = ArgumentParser()

    args = args or sys_argv[1:]


    parser.add_argument(
        '--console',
        action='store_true',
        default=False,
        help=(
            'write log messages '
            'to standard output'))


    parser.add_argument(
        '--debug',
        action='store_true',
        default=False,
        help=(
            'increase logging level '
            'for standard output'))


    parser.add_argument(
        '--vault-id',
        required=True,
        dest='vault',
        help=(
            'name of secrets unique '
            'that will be dumped '))


    return vars(
        parser
        .parse_args(args))



def operation(
    # NOCVR
    config: OrcheConfig,
) -> None:
    """
    Perform whatever operation is associated with the file.

    :param config: Primary class instance for configuration.
    """

    sargs = config.sargs
    crypts = config.crypts
    params = crypts.params

    phrases = params.phrases

    vault = sargs['vault']

    phrase = (
        phrases[vault]
        .phrase)

    stdout.write(
        f'{phrase}\n')


def execution(
    # NOCVR
    args: Optional[list[str]] = None,
) -> None:
    """
    Perform whatever operation is associated with the file.

    :param args: Override the source for the main arguments.
    """

    orche_files = (
        environ
        .get('orche_files'))

    orche_paths = (
        environ
        .get('orche_paths'))

    config = OrcheConfig(
        sargs=arguments(),
        files=orche_files,
        paths=orche_paths)

    config.logger.start()

    config.logger.log_i(
        base='execution/vault',
        status='started')

    operation(config)

    config.logger.log_i(
        base='execution/vault',
        status='stopped')

    config.logger.stop()



if __name__ == '__main__':
    execution()  # NOCVR
