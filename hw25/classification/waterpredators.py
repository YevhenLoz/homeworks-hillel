from hw25.classification.watermammals import WaterMammals


# Inheritance
class WaterPredator(WaterMammals):
    def __init__(self, genus: str, species: str, diet: str):
        super().__init__(genus, species, diet)

    @staticmethod
    def hunt():
        print("I can hunt fish")


if __name__ == '__main__':
    dolphin = WaterPredator('Dolphin', 'Whale', 'Fish')
    dolphin.get_info()
    dolphin.hunt()
    dolphin.movement()

