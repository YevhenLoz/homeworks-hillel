import datetime


dotation = 50000


class Human:
    population: int = 0
    money_in_country = 20000

    def __init__(self, name, surname, sex, birthday):
        """ Initialize self"""
        self.name = name
        self.surname = surname
        self.sex = sex
        self.__birthday = birthday
        self.money = dotation
        Human.total_cash(self.money)
        Human.increase_population()
        # self.__class__.increase_population()

    @property
    def birth_day(self):
        return self.__birthday

    @birth_day.setter
    def birth_day(self, date: list[int]):
        """Exspected date format [2000, 6, 28]"""
        if len(date) == 3 and type(date[0]) == int and type(date[1]) == int and type(date[2]) == int and date[0] >= 2000:
            self.__birthday = datetime.datetime(*date)

    @property
    def age(self):
        return (datetime.datetime.today() - self.birth_day).days // 365

    def __str__(self):
        return f'{self.name} {self.surname}, {self.birth_day}'

    def __del__(self):
        Human.decrease_population()
        print(self, 'I died', Human.population)

    @staticmethod
    def who_we_are():
        print("we are from Earth")

    def eat(self):
        print(self, 'eat')

    def money_landing(self, other, summa):
        """I borrow money"""
        if other.money >= summa:
            self.money += summa
            other.money -= summa
        else:
            self.money += other.money
            other.money = 0

    def __add__(self, other):
        return self.money + other.money

    @classmethod
    def total_cash(cls, summa):
        Human.money_in_country += summa

    @classmethod
    def increase_population(cls):
        Human.population += 1

    @classmethod
    def decrease_population(cls):
        Human.population -= 1


class Bank:
    def __init__(self):
        self.money = 1_000_000

    def money_landing(self, other, summa):
        """I borrow money"""
        if other.money >= summa:
            self.money += summa
            other.money -= summa
        else:
            self.money += other.money
            other.money = 0


mono = Bank()

alex = Human('Alex', 'Bush', 'male', datetime.datetime(2000, 5, 10))
tom = Human('Tom', 'Bush', 'male', datetime.datetime(2005, 5, 10))


alex.birth_day = [1955, 5, 10]
alex.money_landing(tom, 55000)

m = alex + tom
tom.money_landing(mono, 500_000)
tom.who_we_are()
