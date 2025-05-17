"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Any
from typing import Optional

from ansible.plugins.lookup import LookupBase  # type: ignore

from encommon.types import DictStrAny
from encommon.types import LDictStrAny

from orchestro.orche import Orche
from orchestro.orche import OrcheConfig



class LookupModule(LookupBase):  # type: ignore
    """
    Provide information when called within Ansible routines.
    """

    __orche: Optional[Orche] = None


    def run(
        # NOCVR
        self,
        terms: Optional[LDictStrAny] = None,
        variables: Optional[DictStrAny] = None,
        **kwargs: Any,
    ) -> list[Orche]:
        """
        Perform whatever operation is associated with the file.

        :param terms: Positional arguments passed to the lookup.
        :param variables: All variables from within the playrun.
        :param kwargs: Keyword arguments passed to the lookup.
        """

        if self.__orche:
            return [self.__orche]

        assert variables is not None

        sargs = variables['orche_sargs']
        files = variables['orche_files']
        paths = variables['orche_paths']
        cargs = variables['orche_cargs']

        config = OrcheConfig(
            sargs or None,
            files or None,
            paths or None,
            cargs or None)

        config.logger.start()

        self.__orche = Orche(config)

        return [self.__orche]
