class Train:
    def __init__(self, locomotive):
        self.locomotive = locomotive
        self.wagons = []

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        train = "<=" + f"[HEAD <{self.locomotive}>]-"
        for wagon in self.wagons:
            train += f"{wagon}-"
        return train[:-1]


class TrainCar:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            print(f"Sorry, the train wagon [{self.number}] is full.")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f"[{self.number}]"


if __name__ == '__main__':
    my_train = Train('Intercity')
    wagon_1 = TrainCar(1)
    wagon_2 = TrainCar(2)
    wagon_3 = TrainCar(3)
    wagon_4 = TrainCar(4)
    wagon_5 = TrainCar(5)
    my_train.add_wagon(wagon_1)
    my_train.add_wagon(wagon_2)
    my_train.add_wagon(wagon_3)
    my_train.add_wagon(wagon_4)
    my_train.add_wagon(wagon_5)

    wagon_1.add_passenger("John")
    wagon_1.add_passenger("Orest")
    wagon_2.add_passenger("Bogdan")
    wagon_2.add_passenger("Roman")
    wagon_3.add_passenger("Yevhen")
    wagon_3.add_passenger("Margo")
    wagon_3.add_passenger("Leo")
    wagon_3.add_passenger("Ethan")
    wagon_3.add_passenger("Sergiy")
    wagon_3.add_passenger("Mykola")
    wagon_3.add_passenger("Ariel")
    wagon_3.add_passenger("Sol")
    wagon_3.add_passenger("Dr. Watson")
    wagon_3.add_passenger("Sherlock Holms")
    wagon_3.add_passenger("Hercule Poirot")
    wagon_5.add_passenger("Harry Potter")

    print(wagon_1)
    print(wagon_2)
    print(wagon_3)
    print(wagon_4)
    print(wagon_5)
    print(my_train)
    print(len(wagon_1))
    print(len(wagon_2))
    print(len(wagon_3))
    print(len(wagon_4))
    print(len(wagon_5))
    print(len(my_train))
    print(wagon_3.passengers)
