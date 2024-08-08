import abc
import logging
import math

from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty
from typing import Set, List, Dict
from enum import Enum

main_logger: logging.Logger = logging.getLogger('main')


class CellType(Enum):
    armor = 1
    connective = 2
    nerve = 3
    brain = 4


class BaseCell(ABC):
    """
    This class is intended to describe the common functions/parameters used
    by all cells, no matter their type.
    """

    """ Stats """
    # An int to represent the armor value of the cell
    _armor = 0
    # The level of energy in the cell
    _energy: int
    # An int to represent the current health of the cell
    _health: int
    # An int to represent the maximum health of the cell
    _max_health: int

    """ Meta-Data """
    # An enum value representing the type of cell
    _cell_type: CellType
    # A set to represent neighboring cells
    neighbors: Set

    def __init__(self, p_cell_type: CellType = None, p_initial_energy: int = 10, p_max_health:int=100, p_health:int=None, p_neighbors: Set = None):
        main_logger.debug('Creating new cell...')

        # Check all argument types
        if p_cell_type is None or not isinstance(p_cell_type, CellType):
            main_logger.error(f'Error creating Cell: p_cell_type argument cannot be None, must be CellType')
            return
        if p_initial_energy is not isinstance(p_initial_energy, int):
            main_logger.error(f'Error creating Cell: p_initial_energy argument must be None or int')
            return
        if p_max_health is not isinstance(p_max_health, int):
            main_logger.error(f'Error creating Cell: p_max_health argument must be None or int')
            return
        if p_health is not isinstance(p_health, int) or p_health is None:
            main_logger.error(f'Error creating Cell: p_health argument must be None or int')
            return
        if p_neighbors is not isinstance(p_neighbors, Set):
            main_logger.error(f'Error creating Cell: p_neighbors argument must be None or Set')
            return

        # Initialize the uninitialized attributes
        self.neighbors = set()

        # Set attributes according to arguments
        self._armor = 0
        self.cell_type = p_cell_type
        self.energy = p_initial_energy
        self.max_health = p_max_health
        self.health = p_max_health if p_health is None else p_health
        self.neighbors = self.neighbors.update(p_neighbors) if p_neighbors is not None else self.neighbors

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

    """ Attribute Setters """
    @armor.setter
    def armor(self, p_armor: int = None):
        if p_armor is None or not isinstance(p_armor, int):
            main_logger.error(f'Error setting Armor for {self} using provided value: {p_armor}')
            return
        else:
            self._armor = p_armor

    @energy.setter
    def energy(self, p_energy: int = None):
        if p_energy is None or not isinstance(p_energy, int):
            main_logger.error(f'Error setting Health for {self} using provided value: {p_energy}')
            return
        else:
            self._energy = p_energy

    @health.setter
    def health(self, p_health: int = None):
        if p_health is None or not isinstance(p_health, int):
            main_logger.error(f'Error setting Health for {self} using provided value: {p_health}')
            return
        else:
            self._health = p_health

    @max_health.setter
    def max_health(self, p_max_health: int = None):
        if p_max_health is None or not isinstance(p_max_health, int):
            main_logger.error(f'Error setting Health for {self} using provided value: {p_max_health}')
            return
        else:
            self._max_health = p_max_health

    def apply_damage(self, p_damage: int = None):
        """
        Checks armor value, reduces damage according to consequent resistence, updates health
        :param p_damage: An int representing the damage to be applied
        :return: None
        """

        # Applying damage resist due to armor...
        updated_damage = math.floor((1-(self.armor/100)) * p_damage)

        # Updating health...
        self.health = self.health - updated_damage

        # Updating armor due to ware caused by damage...



class ArmorCell(BaseCell):

    def __init__(self, armor: int = 10, *args, **kwargs):
        super(ArmorCell, self).__init__(*args, **kwargs)


class ConnectiveCell(BaseCell):
    pass


class NerveCell(BaseCell):
    pass


class BrainCell(BaseCell):
    pass
