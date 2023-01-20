from hw25.classification.landmammals import LandMammals


# Inheritance
class Herbivore(LandMammals):
    def __init__(self, genus: str, species: str, diet: str):
        super().__init__(genus, species, diet)

    @staticmethod
    def graze():
        print("I can graze")


if __name__ == '__main__':
    cow = Herbivore('Cow', 'Bowinae', 'grass')
    cow.get_info()
    cow.graze()
    cow.movement()
