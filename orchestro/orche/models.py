"""
Functions and routines associated with Enasis Network Orche Automate.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING
from typing import Type

if TYPE_CHECKING:
    from .params import OrcheParams
    from .params import OrcheChildParams
    from .params import OrcheSystemParams
    from .params import OrchePersonParams
    from .params import OrcheGroupParams
    from .params import OrcheSubnetParams



class OrcheModels:
    """
    Return the class object that was imported within method.
    """


    @classmethod
    def orche(
        cls,
    ) -> Type['OrcheParams']:
        """
        Return the class object that was imported within method.

        :returns: Class object that was imported within method.
        """

        from .params import (
            OrcheParams)

        return OrcheParams


    @classmethod
    def child(
        cls,
    ) -> Type['OrcheChildParams']:
        """
        Return the class object that was imported within method.

        :returns: Class object that was imported within method.
        """

        from .params import (
            OrcheChildParams)

        return OrcheChildParams


    @classmethod
    def system(
        cls,
    ) -> Type['OrcheSystemParams']:
        """
        Return the class object that was imported within method.

        :returns: Class object that was imported within method.
        """

        from .params import (
            OrcheSystemParams)

        return OrcheSystemParams


    @classmethod
    def person(
        cls,
    ) -> Type['OrchePersonParams']:
        """
        Return the class object that was imported within method.

        :returns: Class object that was imported within method.
        """

        from .params import (
            OrchePersonParams)

        return OrchePersonParams


    @classmethod
    def subnet(
        cls,
    ) -> Type['OrcheSubnetParams']:
        """
        Return the class object that was imported within method.

        :returns: Class object that was imported within method.
        """

        from .params import (
            OrcheSubnetParams)

        return OrcheSubnetParams


    @classmethod
    def group(
        cls,
    ) -> Type['OrcheGroupParams']:
        """
        Return the class object that was imported within method.

        :returns: Class object that was imported within method.
        """

        from .params import (
            OrcheGroupParams)

        return OrcheGroupParams
