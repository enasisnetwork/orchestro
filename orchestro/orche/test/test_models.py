"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from ..models import OrcheModels



def test_OrcheModels_cover() -> None:
    """
    Perform various tests associated with relevant routines.
    """

    models = OrcheModels

    assert models.orche()

    assert models.child()
    assert models.system()
    assert models.person()
    assert models.subnet()
    assert models.group()
