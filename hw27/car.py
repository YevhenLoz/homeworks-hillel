class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car: {{\n  make: {self.brand}\n  model: {self.model}\n  year: {self.year}\n}}"


if __name__ == '__main__':
    my_car = Car("Toyota", "Camry", 2023)
    print(my_car)
