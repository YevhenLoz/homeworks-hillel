from abc import abstractmethod

from hw25.classification.Animal import Animals


# Inheritance
class Mammals(Animals):
    def __init__(self, species: str, genus: str, diet: str, habitat: str, feed_young_with: str):
        # encapsulation, hiding
        self.__genus = genus
        self.__species = species
        self.__diet = diet
        self.__habitat = habitat
        self.__feed_young_with = feed_young_with

    # polymorphism
    # abstraction
    @abstractmethod
    def movement(self): ...

    def get_info(self):
        print(f"{self.__species} is from genus {self.__genus}, this animal eats {self.__diet}, "
              f"leaves on {self.__habitat} and feeds young with {self.__feed_young_with} ")
