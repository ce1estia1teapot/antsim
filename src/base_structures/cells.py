import abc
import logging
import math

from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty
from typing import Set, List, Dict, Tuple
from uuid import uuid4
from enum import Enum

main_logger: logging.Logger = logging.getLogger('main')


class CellType(Enum):
    BASE = 0
    ARMOR = 1
    CONNECTIVE = 2
    NERVE = 3
    BRAIN = 4
    MUSCLE = 5
    STORAGE = 6


class CellEnergyState(Enum):
    CRITICAL = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class CellStates(Enum):
    INVINCIBLE = 0
    STARVING = 1
    MOVING = 2


class BaseCell(ABC):
    """
    This class is intended to describe the common functions/parameters used
    by all cells, no matter their type.
    """
    """ States """
    # A set of states to represent the active conditions on the cell
    states: Set = set()

    """ Meta-Data """
    # An enum value representing the type of cell
    _cell_type: CellType = CellType.BASE
    # A set to represent neighboring cells
    neighbors: Set = set()

    """ Stats """
    # A unique identifier for this cell
    _id: str
    # An int to represent the armor value of the cell
    _armor: int = 0
    # The level of energy in the cell
    _energy: int = 10
    # An int to represent the current health of the cell
    _health: int = 100
    # An int to represent the maximum health of the cell
    _max_health: int = 100
    # An int to represent the amount of damage dealt by the cell if it participates in an attack
    _damage: int = 1
    # A float to represent the fraction of received damage that is radiated to neighboring cells on receiving damage
    _damage_radiation: float = 0.25
    location: Tuple[float, float]



    def __init__(self, p_cell_type: CellType = CellType.BASE, p_initial_energy: int = 10, p_max_health: int = 100,
                 p_health: int = None, p_neighbors: Set = None, p_damage: int = 1, p_damage_radiation: float = 0.25,
                 p_location: Tuple[float, float] = None):
        main_logger.debug('Creating new cell...')

        # Check all argument types
        if not isinstance(p_cell_type, CellType) and p_cell_type is not None:
            main_logger.error(
                f'Error creating Cell: p_cell_type argument must be None or CellType. Setting to default...')
        if not isinstance(p_initial_energy, int) and p_initial_energy is not None:
            main_logger.error(
                f'Error creating Cell: p_initial_energy argument must be None or int. Setting to default...')
        if not isinstance(p_max_health, int) and p_max_health is not None:
            main_logger.error(f'Error creating Cell: p_max_health argument must be None or int. Setting to default...')
        if not isinstance(p_health, int) and p_health is not None:
            main_logger.error(f'Error creating Cell: p_health argument must be None or int. Setting to default...')
        if not isinstance(p_neighbors, Set) and p_neighbors is not None:
            main_logger.error(f'Error creating Cell: p_neighbors argument must be None or Set. Setting to default...')
        if not isinstance(p_damage, int) and p_damage is not None:
            main_logger.error(f'Error creating Cell: p_damage argument must be None or int. Setting to default...')
        if not isinstance(p_damage_radiation, float) and p_damage_radiation is not None:
            main_logger.error(
                f'Error creating Cell: p_damage_radiation argument must be None or float. Setting to default...')
        if not isinstance(p_location, Tuple) and p_location is not None:
            main_logger.error(
                f'Error creating Cell: p_location argument must be Tuple, cannot be None.')
            return

        # Initialize the uninitialized attributes
        self.neighbors = set()

        # Set attributes according to arguments
        self._id = str(uuid4())
        self.armor = 0
        self.cell_type = p_cell_type if isinstance(p_cell_type, CellType) else CellType(self._cell_type)
        self.energy = p_initial_energy if (isinstance(p_initial_energy, int)) else int(self.energy)
        self.max_health = p_max_health if (isinstance(p_max_health, int)) else int(self.max_health)
        self.health = p_max_health if (p_health is None or not isinstance(p_health, int)) else p_health
        self.neighbors = self.neighbors.update(p_neighbors) if (isinstance(p_neighbors, Set)) else set()
        self.damage = p_damage if isinstance(p_damage, int) else self.damage
        self.damage_radiation = p_damage_radiation if isinstance(p_damage_radiation, float) else int(self.damage_radiation)

        return

    def update(self) -> None:
        """
        Reassess adjacency bonuses, changes energy state based on energy level, more TBD
        :return:
        """
        raise NotImplementedError()

    def move(self, p_new_location: Tuple[float, float] = None) -> None:
        """
        Implements the movement of the cell. Consumes energy
        :param p_new_location:
        :return:
        """
        if not isinstance(p_new_location, Tuple):
            main_logger.error(f'Error moving cell: p_new_location must be Tuple[float, float]')
            return

        self.energy -= self.energy
        self.location = p_new_location
        self.update()
        return

    """ Attribute Getters """

    @property
    def armor(self):
        return self._armor

    @property
    def energy(self):
        return self._energy

    @property
    def health(self):
        return self._health

    @property
    def max_health(self):
        return self._max_health

    @property
    def damage(self):
        return self._damage

    @property
    def damage_radiation(self):
        return self._damage_radiation

    """ Attribute Setters """

    @armor.setter
    def armor(self, p_armor: int = None):
        if p_armor is None or not isinstance(p_armor, int):
            new_exception = ValueError(f'Error setting armor for {self} using provided value: {p_armor}')
            main_logger.error(new_exception)
            return
        else:
            self._armor = p_armor

    @energy.setter
    def energy(self, p_energy: int = None):
        if p_energy is None or not isinstance(p_energy, int):
            new_exception = ValueError(f'Error setting energy for {self} using provided value: {p_energy}')
            main_logger.error(new_exception)
            return
        else:
            self._energy = p_energy

    @health.setter
    def health(self, p_health: int = None):
        if p_health is None or not isinstance(p_health, int):
            new_exception = ValueError(f'Error setting health for {self} using provided value: {p_health}')
            main_logger.error(new_exception)
            return
        else:
            self._health = p_health

    @max_health.setter
    def max_health(self, p_max_health: int = None):
        if p_max_health is None or not isinstance(p_max_health, int):
            new_exception = ValueError(f'Error setting max_health for {self} using provided value: {p_max_health}')
            main_logger.error(new_exception)
            return
        else:
            self._max_health = p_max_health

    @damage.setter
    def damage(self, p_damage: int = None):
        if p_damage is None or not isinstance(p_damage, int):
            new_exception = ValueError(f'Error setting damage for {self} using provided value: {p_damage}')
            main_logger.error(new_exception)
            return
        else:
            self._damage = p_damage

    @damage_radiation.setter
    def damage_radiation(self, p_damage_radiation: int = None):
        if p_damage_radiation is None or not isinstance(p_damage_radiation, float):
            new_exception = ValueError(
                f'Error setting damage_radiation for {self} using provided value: {p_damage_radiation}')
            main_logger.error(new_exception)
            return
        else:
            self._damage_radiation = p_damage_radiation

    """ Common methods """

    def apply_damage(self, p_damage: int = None) -> None:
        """
        Checks armor value, reduces damage according to consequent resistence, updates health
        :param p_damage: An int representing the damage to be applied
        :return: None
        """
        if p_damage < 1 or p_damage is None:
            return

        # Applying damage resist due to armor...
        updated_damage = round((1 - (self.armor / 100)) * p_damage, 1)
        main_logger.debug(f'Updated damage: {updated_damage}')

        # Updating health...
        main_logger.debug(f'Invincible: {CellStates.INVINCIBLE in self.states}')
        if not CellStates.INVINCIBLE in self.states:
            main_logger.debug('Applying damage to health...')
            self.health = self.health - updated_damage

        # Updating armor due to ware caused by damage...
        # ???

        # Forwarding damage to adjacent cells
        self.states.add(CellStates.INVINCIBLE)
        for cell in self.neighbors:
            cell.apply_damage(p_damage=updated_damage * self.damage_radiation)
        self.states.remove(CellStates.INVINCIBLE)


class ArmorCell(BaseCell):
    """
    Acts as an armored but otherwise inert cell to reduce incoming damage
    """

    def __init__(self, p_armor: int = 10, *args, **kwargs):
        super(ArmorCell, self).__init__(*args, **kwargs)

        self.cell_type = CellType.ARMOR
        self.armor = p_armor


class ConnectiveCell(BaseCell):
    pass


class NerveCell(BaseCell):
    pass


class BrainCell(BaseCell):
    pass
    """
    At least one is required for an organism to be alive. Sends/receives inter-cell communications,
    sends commands to other cells via nerve cells, more TBD
    """


class MuscleCell(BaseCell):
    pass


class StorageCell(BaseCell):
    """
    This type of cell should handle the input/output storage of an organism's resources.
    """
    pass
