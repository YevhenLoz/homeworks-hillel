from abc import ABC, abstractmethod


# Abstraction
class Animals(ABC):

    @abstractmethod
    def movement(self): ...

    @abstractmethod
    def get_info(self): ...
