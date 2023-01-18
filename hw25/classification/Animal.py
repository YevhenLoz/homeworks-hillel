from abc import ABC, abstractmethod


class Animals(ABC):

    @abstractmethod
    def get_info(self):
        pass
