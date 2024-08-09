import abc
import logging
import math

from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty
from cells import BaseCell
from typing import Set, List, Dict, Tuple
from enum import Enum


class OrganismStates(Enum):
    HEALING = 0


class BaseOrganism(ABC):
    """
    This class is intended to describe the common functions/parameters used
    by all organisms
    """

    """ States """
    # A set of states to represent the active conditions on the cell
    states: Set = set()

    """ Meta-Data """
    # A dictionary of cell_id: Cells for storage and quick reference of the body's cells
    cells: Dict[str, BaseCell]

    """ Stats """

    @abstractmethod
    def move(self, p_location: Tuple[float, float]) -> None:
        """
        This function should take in a new location and handle all the steps of moving the organism.
        Moving all the cells, more TBD
        :param p_location:
        :return:
        """
        return

    @abstractmethod
    def harvest_resource(self) -> None:
        """
        This function should handle harvesting a resource
        :return:
        """

        return

    @abstractmethod
    def update(self):
        """
        This function should handle updating the states of the organism.
        :return:
        """
        return

