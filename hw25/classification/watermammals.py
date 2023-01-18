from hw25.classification.mammal import Mammals


class WaterMammals(Mammals):
    def __init__(self, species: str, genus: str, diet: str):
        super().__init__(species, genus, diet, 'ocean', 'milk')

    def dive(self):
        print("I can dive")

    def swim(self):
        print("I can swim")




