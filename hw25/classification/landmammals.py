from hw25.classification.mammal import Mammals


class LandMammals(Mammals):
    def __init__(self, species: str, genus: str, diet: str):
        super().__init__(species, genus, diet, 'land', 'milk')

    def run(self):
        print("I can run")

    def jump(self):
        print("I can jump")
