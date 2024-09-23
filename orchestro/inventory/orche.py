"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from copy import deepcopy
from os import environ
from os import path as os_path
from pathlib import Path
from sys import path as sys_path
from typing import Any

from ansible.inventory.data import InventoryData  # type: ignore
from ansible.parsing.dataloader import DataLoader  # type: ignore
from ansible.plugins.inventory import BaseInventoryPlugin  # type: ignore

from encommon.config import config_load
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


    def add_child(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Perform the operations related to the Ansible inventory.

        :param args: Positional arguments passed for downstream.
        :param kwargs: Keyword arguments passed for downstream.
        """

        self.inventory.add_child(*args, **kwargs)


    def add_group(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Perform the operations related to the Ansible inventory.

        :param args: Positional arguments passed for downstream.
        :param kwargs: Keyword arguments passed for downstream.
        """

        self.inventory.add_group(*args, **kwargs)


    def add_host(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Perform the operations related to the Ansible inventory.

        :param args: Positional arguments passed for downstream.
        :param kwargs: Keyword arguments passed for downstream.
        """

        self.inventory.add_host(*args, **kwargs)


    def set_value(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Perform the operations related to the Ansible inventory.

        :param args: Positional arguments passed for downstream.
        :param kwargs: Keyword arguments passed for downstream.
        """

        self.inventory.set_variable(*args, **kwargs)


    def parse(
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

        self.parse_orche()
        self.parse_paths()


    def build_orche(
        self,
    ) -> Orche:
        """
        Construct instances using the configuration parameters.
        """

        files = environ.get(
            'orche_files')

        paths = environ.get(
            'orche_paths')

        verbose = (
            self.display
            .verbosity)

        console = verbose >= 1
        debug = verbose >= 2

        sargs = {
            'console': console,
            'debug': debug}

        config = OrcheConfig(
            sargs, files, paths)

        config.logger.start()

        return Orche(config)


    def parse_orche(  # noqa: CFQ001
        self,
    ) -> None:
        """
        Process and update Ansible inventory from Orche objects.
        """

        orche = self.build_orche()

        childs = orche.childs


        self.add_host(
            host='localhost',
            group='all')

        self.add_group('orche')

        self.set_value(
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

            params = group.params

            if not group.enable:
                return True

            realm = params.realm

            if realm != 'ansible':
                return NCTrue

            return False


        for group in groups:

            if _invalid(group):
                continue

            self.add_group(
                group.name)


            ansbgrp = (
                group.params
                .ansible)

            if ansbgrp is not None:

                vars = (
                    ansbgrp.endumped
                    .items())

                for key, value in vars:

                    self.set_value(
                        group.name,
                        key, value)


        for group in groups:

            if _invalid(group):
                continue

            mmbrof = group.groups

            for _group in mmbrof:

                if _invalid(_group):
                    continue  # NOCVR

                self.add_child(
                    _group.name,
                    group.name)


        for system in systems:

            if _invalid(system):
                continue

            self.add_host(
                host=system.name,
                group='orche')


            ansbsys = (
                system.params
                .ansible)

            if ansbsys is not None:

                vars = (
                    ansbsys.endumped
                    .items())

                for key, value in vars:

                    self.set_value(
                        system.name,
                        key, value)


            mmbrof = system.groups

            for group in mmbrof:

                if _invalid(group):
                    continue  # NOCVR

                self.add_child(
                    group.name,
                    system.name)


    def parse_paths(
        self,
    ) -> None:
        """
        Process and update Ansible inventory from Orche objects.
        """

        gvars = (
            Path(__file__).parent
            / 'group_vars')

        hvars = (
            Path(__file__).parent
            / 'host_vars')

        files = (
            list(gvars.glob('*'))
            + list(hvars.glob('*')))


        def _add_group() -> None:

            self.add_group(  # NOCVR
                file.stem)


        def _add_host() -> None:

            self.add_host(
                host=file.stem,
                group='all')

            content = (
                config_load(file))

            _names = (
                self.inventory
                .groups)

            names = content.get(
                'orchestro_groups')

            if names is None:
                return None

            for name in names:  # NOCVR

                if name not in _names:
                    continue

                self.add_child(
                    name, file.stem)


        for file in files:

            name = file.name

            if name.startswith('.'):
                continue  # NOCVR

            parent = file.parent.name


            kind = (
                'host'
                if parent == 'host_vars'
                else 'group')

            if kind == 'group':
                _add_group()  # NOCVR

            elif kind == 'host':
                _add_host()



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
