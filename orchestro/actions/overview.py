"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Optional

from ansible.plugins.action import ActionBase  # type: ignore
from ansible.utils.display import Display  # type: ignore

from encommon.types import DictStrAny
from encommon.utils import array_ansi
from encommon.utils import make_ansi



PARAMETERS: DictStrAny = {
    'input': {
        'type': 'dict',
        'required': True}}



class ActionModule(ActionBase):  # type: ignore
    """
    Perform whatever operation is associated with the file.
    """

    argument_spec = PARAMETERS
    supports_check_mode = True


    def run(
        # NOCVR
        self,
        tmp: Optional[str] = None,
        task_vars: Optional[DictStrAny] = None,
    ) -> DictStrAny:
        """
        Perform whatever operation is associated with the file.

        .. note::
           Parameters intentioanlly undefined for this method.

        :returns: Returned following parent super instantiation.
        """

        params = self._task.args

        assert task_vars is not None

        display = Display()

        dumped = array_ansi(
            params['input'],
            indent=2)

        dashes = '─' * 60

        hostname = task_vars[
            'inventory_hostname']

        output = make_ansi(
            f'<c32>{dashes}<c0>\n'
            f'<c32>{hostname}<c0>'
            f'\n{dumped}\n'
            f'<c32>{dashes}<c0>')

        display.display(
            msg=output,
            screen_only=True)

        result = super().run(
            tmp, task_vars)

        result['changed'] = False

        assert isinstance(
            result, dict)

        return result
