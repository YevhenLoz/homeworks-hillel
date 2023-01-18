from hw25.classification.Animal import Animals


class Mammals(Animals):
    def __init__(self, species: str, genus: str, diet: str, habitat: str, feed_young_with: str):
        self.genus = genus
        self.species = species
        self.diet = diet
        self.habitat = habitat
        self.feed_young_with = feed_young_with

    def get_info(self):
        print(f"{self.species} is from genus {self.genus}, this animal eats {self.diet}, leaves on {self.habitat} "
              f"and feeds young with {self.feed_young_with} ")
