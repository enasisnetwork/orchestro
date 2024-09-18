"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from ..vault import arguments



def test_arguments() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    sargs = arguments([
        '--vault-id', 'vault'])

    assert sargs == {
        'console': False,
        'debug': False,
        'vault': 'vault'}
