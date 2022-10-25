import uuid
import datetime
from art import *


# Bank account class
class BankAccount:
    deposit_portfolio = 0

    # @classmethod
    # def deposit_money(cls, money):
    #      BankAccount.deposit += money
    #
    # @classmethod
    # def withdraw_money(cls, money):
    #     BankAccount.deposit -= money

    def __init__(self, name, initial_amount, interest: int):
        self.name = name
        self.balance = initial_amount
        self.__interest = interest
        self.__creation_date = datetime.date.today()
        self.account_id = uuid.uuid4()
        self.amount = 0
        BankAccount.deposit_portfolio += initial_amount

#створити геттер та сеттер для зміни ставки по рахунку
    @property
    def get_interest(self):
        return self.__interest

    @get_interest.setter
    def get_interest(self, percent):
        if type(percent) == int and 8 >= percent >= 2:
            self.__interest = percent

# перевизначте метод __str__ (наповнення - на ваш вибір)
    def __str__(self):
        return f'Account ID:{self.account_id}, Balance: {self.balance}, Name: {self.name},' \
               f'Rate: {self.__interest} Date: {self.__creation_date}'

# створіть методи для поповнення та зняття коштів з рахунку (рахунок не може мати негативний баланс)
    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

# створіть метод трансфер, який дозволяє переводити кошти з одного рахунку на інший
    def transfer_money(self, amount, account):
        self.balance -= amount
        account.balance += amount

    def __del__(self):
        print(f' {self.name}, your account is closed due to Bank liquidation, refund amount is {self.balance}')

#створіть метод get_todays_profit, задекорований через property
    @property
    def get_todays_profit(self):
        todays_profit = (self.__interest/365) * self.balance
        return todays_profit

#створіть метод, задекорований staticmethod
    @staticmethod
    def bank_slogan():
        tprint(''' WE are 
        your Monte Cristo
        island!''', font="cybermedium")



account1 = BankAccount('Tom Clean', 100, 7)
account1.get_interest = 2
account1.deposit(500.50)
account1.withdraw(100)
account2 = BankAccount('Tom Dirt', 100, 8)
account1.transfer_money(500, account2)
print(account1)
print(account2)
account3 = BankAccount('Tom Saint', 770, 7)
print(account3)
account3.withdraw(110)

BankAccount.bank_slogan()

