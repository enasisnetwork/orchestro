"""
Functions and routines associated with Enasis Network Orchestrations.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from copy import deepcopy
from typing import TYPE_CHECKING

from encommon.types import DictStrAny

from .group import OrcheGroup
from .person import OrchePerson
from .subnet import OrcheSubnet
from .system import OrcheSystem

if TYPE_CHECKING:
    from ..orche import Orche




OrcheSystems = dict[str, OrcheSystem]

OrchePersons = dict[str, OrchePerson]
OrcheSubnets = dict[str, OrcheSubnet]

OrcheGroups = dict[str, OrcheGroup]



class OrcheChilds:
    """
    Contain the object instances for related Orche children.

    :param orche: Primary class instance for Orchestrations.
    """

    __orche: 'Orche'

    __systems: OrcheSystems

    __persons: OrchePersons
    __subnets: OrcheSubnets

    __groups: OrcheGroups


    def __init__(
        self,
        orche: 'Orche',
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        orche.logger.log_d(
            base=self,
            status='initial')

        self.__orche = orche

        self.__systems = {}

        self.__persons = {}
        self.__subnets = {}

        self.__groups = {}

        self.build_objects()

        orche.logger.log_i(
            base=self,
            status='created')


    def build_objects(
        self,
    ) -> None:
        """
        Construct instances using the configuration parameters.
        """

        self.__build_systems()

        self.__build_persons()
        self.__build_subnets()

        self.__build_groups()


    def __build_systems(
        self,
    ) -> None:
        """
        Construct instances using the configuration parameters.
        """

        orche = self.__orche
        params = orche.params
        systems = params.systems

        if systems is None:
            return None

        model = OrcheSystem


        childs: OrcheSystems = {}


        items = systems.items()

        for name, system in items:

            object = model(
                orche, name, system)

            childs[name] = object


        self.__systems = childs


    def __build_persons(
        self,
    ) -> None:
        """
        Construct instances using the configuration parameters.
        """

        orche = self.__orche
        params = orche.params
        persons = params.persons

        if persons is None:
            return None

        model = OrchePerson


        childs: OrchePersons = {}


        items = persons.items()

        for name, person in items:

            object = model(
                orche, name, person)

            childs[name] = object


        self.__persons = childs


    def __build_subnets(
        self,
    ) -> None:
        """
        Construct instances using the configuration parameters.
        """

        orche = self.__orche
        params = orche.params
        subnets = params.subnets

        if subnets is None:
            return None

        model = OrcheSubnet


        childs: OrcheSubnets = {}


        items = subnets.items()

        for name, subnet in items:

            object = model(
                orche, name, subnet)

            childs[name] = object


        self.__subnets = childs


    def __build_groups(
        self,
    ) -> None:
        """
        Construct instances using the configuration parameters.
        """

        orche = self.__orche
        params = orche.params
        groups = params.groups

        if groups is None:
            return None

        model = OrcheGroup


        childs: OrcheGroups = {}


        items = groups.items()

        for name, group in items:

            object = model(
                orche, name, group)

            childs[name] = object


        self.__groups = childs


    def validate(
        self,
    ) -> None:
        """
        Perform advanced validation on the parameters provided.
        """


        systems = (
            self.__systems
            .values())

        for system in systems:
            system.validate()


        persons = (
            self.__persons
            .values())

        for person in persons:
            person.validate()


        subnets = (
            self.__subnets
            .values())

        for subnet in subnets:
            subnet.validate()


        groups = (
            self.__groups
            .values())

        for group in groups:
            group.validate()


    @property
    def systems(
        self,
    ) -> OrcheSystems:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        systems = self.__systems

        return dict(systems)


    @property
    def persons(
        self,
    ) -> OrchePersons:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        persons = self.__persons

        return dict(persons)


    @property
    def subnets(
        self,
    ) -> OrcheSubnets:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        subnets = self.__subnets

        return dict(subnets)


    @property
    def groups(
        self,
    ) -> OrcheGroups:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        groups = self.__groups

        return dict(groups)


    @property
    def dumped(
        self,
    ) -> DictStrAny:
        """
        Return the facts about the attributes from the instance.

        :returns: Facts about the attributes from the instance.
        """

        systems = self.systems
        persons = self.persons
        subnets = self.subnets
        groups = self.groups

        dumped: DictStrAny = {

            'systems': {
                k: v.dumped for k, v
                in systems.items()},

            'persons': {
                k: v.dumped for k, v
                in persons.items()},

            'subnets': {
                k: v.dumped for k, v
                in subnets.items()},

            'groups': {
                k: v.dumped for k, v
                in groups.items()}}

        return deepcopy(dumped)
