from hw25.classification.landmammals import LandMammals


# Inheritance
class Predator(LandMammals):
    def __init__(self, genus: str, species: str, diet: str):
        super().__init__(genus, species, diet)

    # encapsulation, hiding
    def __track_pray(self):
        print("I track pray")

    # encapsulation, hiding
    def __catch_pray(self):
        print("i catch pray")

    def hunt(self):
        self.__track_pray()
        self.__catch_pray()
        print("I can hunt")


if __name__ == '__main__':
    lion = Predator('lion', 'Felidae', 'meat')
    lion.get_info()
    lion.movement()
    lion.hunt()
