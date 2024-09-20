"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from copy import deepcopy
from os import environ
from os import path as os_path
from sys import path as sys_path

from ansible.inventory.data import InventoryData  # type: ignore
from ansible.parsing.dataloader import DataLoader  # type: ignore
from ansible.plugins.inventory import BaseInventoryPlugin  # type: ignore

from encommon.types import DictStrAny
from encommon.types import NCTrue
from encommon.types import sort_dict

sys_path.insert(0, os_path.abspath('.'))

from orchestro.orche import Orche
from orchestro.orche import OrcheConfig
from orchestro.orche.childs import OrcheGroup
from orchestro.orche.childs import OrcheSystem



_ISVALID = OrcheSystem | OrcheGroup



class InventoryModule(BaseInventoryPlugin):  # type: ignore
    """
    Process and update Ansible inventory from Orche objects.
    """


    def verify_file(
        # NOCVR
        self,
        path: str,
    ) -> bool:
        """
        Perform advanced validation on the parameters provided.

        :param path: Complete or relative path to the YAML file.
        :returns: Boolean indicating the parameters are valid.
        """

        return True


    def parse(  # noqa: CFQ001
        self,
        inventory: InventoryData,
        loader: DataLoader,
        path: str,
        cache: bool = True,
    ) -> None:
        """
        Process and update Ansible inventory from Orche objects.

        :param inventory: Reference to Ansible inventory object.
        :param loader: Reference for the Ansible loader object.
        :param path: Value which represents source of inventory.
        :param cache: Indicates taht internal cache is enabled.
        """

        super().parse(
            inventory,
            loader=loader,
            path=path,
            cache=cache)


        add_group = (
            self.inventory
            .add_group)

        set_value = (
            self.inventory
            .set_variable)

        add_child = (
            self.inventory
            .add_child)

        add_host = (
            self.inventory
            .add_host)


        files = environ.get(
            'orche_files')

        paths = environ.get(
            'orche_paths')

        verbose = (
            self.display
            .verbosity)

        sargs = {
            'console': (
                verbose >= 1),
            'debug': (
                verbose >= 2)}

        config = OrcheConfig(
            sargs, files, paths)

        config.logger.start()

        orche = Orche(config)

        childs = orche.childs


        add_host(
            host='localhost',
            group='all')

        add_group('orche')

        set_value(
            entity='orche',
            varname='orche',
            value=orche)


        groups = (
            childs.groups
            .values())

        systems = (
            childs.systems
            .values())


        def _invalid(
            group: _ISVALID,
        ) -> bool:

            if not group.enable:
                return True

            realm = (
                group.params
                .realm)

            if realm != 'ansible':
                return NCTrue

            return False


        for group in groups:

            if _invalid(group):
                continue

            add_group(group.name)


        for group in groups:

            if _invalid(group):
                continue

            mmbrof = group.groups

            for _group in mmbrof:

                if _invalid(_group):
                    continue  # NOCVR

                add_child(
                    group.name,
                    _group.name)


        for system in systems:

            if _invalid(system):
                continue

            add_host(
                host=system.name,
                group='orche')


            ansible = (
                system.params
                .ansible)

            if ansible is not None:

                vars = (
                    ansible.endumped
                    .items())

                for key, value in vars:

                    set_value(
                        system.name,
                        varname=key,
                        value=value)


            mmbrof = system.groups

            for group in mmbrof:

                if _invalid(group):
                    continue  # NOCVR

                add_host(
                    system.name,
                    _group.name)


    @property
    def dumped(
        self,
    ) -> DictStrAny:
        """
        Return the facts about the attributes from the instance.

        :returns: Facts about the attributes from the instance.
        """

        dumped: DictStrAny = {
            'hosts': {},
            'groups': {}}


        hosts = (
            self.inventory
            .hosts.items())

        _hosts = dumped['hosts']

        for name, host in hosts:

            _hosts[name] = (
                host.serialize())


        groups = (
            self.inventory
            .groups.items())

        _groups = dumped['groups']

        for name, group in groups:

            _groups[name] = (
                group.serialize())


        dumped = deepcopy(dumped)

        return sort_dict(dumped)
