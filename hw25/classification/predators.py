from hw25.classification.landmammals import LandMammals


class Predator(LandMammals):
    def __init__(self, genus: str, species: str, diet: str):
        super().__init__(genus, species, diet)

    def hunt(self):
        print("I can hunt")


if __name__ == '__main__':
    lion = Predator('lion', 'Felidae', 'meat')
    lion.get_info()
    lion.run()
    lion.hunt()
    lion.jump()
