"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Optional

from ansible.plugins.action import ActionBase  # type: ignore

from encommon.types import BaseModel
from encommon.types import DictStrAny
from encommon.types import sort_dict

from pydantic import Field



class RoleParams(BaseModel, extra='ignore'):
    """
    Process and validate the Orche configuration parameters.
    """

    enrobie_unique: Annotated[
        str,
        Field(...,
              description='Unique name for the deployment')]

    enrobie_directory: Annotated[
        str,
        Field('/opt/enrobie',
              description='Base directory for the package')]

    enrobie_user: Annotated[
        str,
        Field('enrobie',
              description='Local system user for deployment')]

    enrobie_group: Annotated[
        str,
        Field('enrobie',
              description='Local system group for deployment')]

    enrobie_python: Annotated[
        str,
        Field('python3',
              description='Python for creating virtual env')]

    enrobie_package: Annotated[
        str,
        Field('enrobie',
              description='Installation package or path')]

    enrobie_version: Annotated[
        Optional[str],
        Field(None,
              description='Which version instead of latest')]

    enrobie_repo_path: Annotated[
        Optional[str],
        Field(None,
              description='Clone configuration repository')]

    enrobie_repo_version: Annotated[
        Optional[str],
        Field(None,
              description='Clone configuration repository')]

    enrobie_config: Annotated[
        Optional[DictStrAny],
        Field(None,
              description='Clone configuration repository')]

    enrobie_logging: Annotated[
        Optional[bool],
        Field(False,
              description='Enable logging to the log file')]

    enrobie_console: Annotated[
        Optional[bool],
        Field(False,
              description='Enable logging to the console')]



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

        source = (
            self._task.args
            ['params'])


        try:

            params = (
                RoleParams(**source)
                .endumped)

            params = {
                k[8:]: v for k, v
                in params.items()}

            result['params'] = (
                sort_dict(params))


        except Exception as reason:
            result |= {
                'failed': True,
                'exception': reason}


        return sort_dict(result)
