import abc

from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty
from typing import Set


class BaseLimb(ABC):
    pass


class BaseAnimal(ABC):
    """
    For this class, consider a Spore approach
    """
    # Core Attributes
    limbs: Set[BaseLimb] = {}

    # Derived Attributes
    weight: float
