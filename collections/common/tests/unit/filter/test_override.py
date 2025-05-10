"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pytest import raises

from ....plugins.filter.override import basename



def test_basename() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    path = '/foo/bar/baz/bop.txt'


    base = basename(path)

    assert base == 'bop.txt'


    base = basename(path, 1)

    assert base == 'baz/bop.txt'


    base = basename(path, 9)

    assert base == path.lstrip('/')



def test_basename_raises() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    _raises = raises(Exception)


    with _raises as reason:
        basename('')

    _reason = str(reason.value)

    assert _reason[:5] == 'There'


    with _raises as reason:
        basename('/')

    _reason = str(reason.value)

    assert _reason[:5] == 'There'
