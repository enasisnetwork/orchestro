"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Optional

from ansible.plugins.action import ActionBase  # type: ignore

from encommon.types import DictStrAny
from encommon.types import sort_dict

from orchestro.orche.params.common import OrcheParamsModel

from pydantic import Field



class RoleParams(OrcheParamsModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    unique: Annotated[
        str,
        Field(...,
              description='Unique name for the deployment')]

    directory: Annotated[
        str,
        Field('/opt/enhomie',
              description='Base directory for the package')]

    user: Annotated[
        str,
        Field('enhomie',
              description='Local system user for deployment')]

    group: Annotated[
        str,
        Field('enhomie',
              description='Local system group for deployment')]

    python: Annotated[
        str,
        Field('python3',
              description='Python for creating virtual env')]

    package: Annotated[
        str,
        Field('enhomie',
              description='Installation package or path')]

    version: Annotated[
        Optional[str],
        Field(None,
              description='Which version instead of latest')]

    repo_path: Annotated[
        Optional[str],
        Field(None,
              description='Clone configuration repository')]

    repo_version: Annotated[
        Optional[str],
        Field(None,
              description='Clone configuration repository')]

    config: Annotated[
        Optional[DictStrAny],
        Field(None,
              description='Clone configuration repository')]

    logging: Annotated[
        Optional[bool],
        Field(False,
              description='Enable logging to the log file')]

    console: Annotated[
        Optional[bool],
        Field(False,
              description='Enable logging to the console')]

    autostart: Annotated[
        Optional[bool],
        Field(False,
              description='Automatic startup with system')]



class ActionModule(ActionBase):  # type: ignore
    """
    Perform whatever operation is associated with the file.
    """


    def run(
        # NOCVR
        self,
        tmp: Optional[str] = None,
        task_vars: Optional[DictStrAny] = None,
    ) -> DictStrAny:
        """
        Perform whatever operation is associated with the file.

        :param tmp: Deprecated paramter, not longer being used.
        :param task_vars: Variables associated around this task.
        :returns: Dictionary of results for the module process.
        """

        result: DictStrAny = {
            'params': None,
            'changed': False}

        source = self._task.args


        try:

            params = (
                RoleParams(**source)
                .endumped)

            result['params'] = (
                sort_dict(params))


        except Exception as reason:
            result |= {
                'failed': True,
                'exception': reason}


        return sort_dict(result)
