from hw25.classification.mammal import Mammals


# Inheritance
class WaterMammals(Mammals):
    def __init__(self, species: str, genus: str, diet: str):
        super().__init__(species, genus, diet, 'ocean', 'milk')

    # polymorphism
    def movement(self):
        print("I can dive and swim")
