import uuid
import datetime
from art import *


class BankAccount:
    total_deposit = 0

    def __init__(self, name, summa, interest: int):
        """ Initialize self"""
        self.name = name
        self.balance = summa
        self.__interest = interest
        self.__creation_date = datetime.date.today()
        self.account_id = uuid.uuid4()
        self.amount = 0
        BankAccount.accounting(summa, income=True)

    @property
    def get_interest(self):
        """
        Getter to get protected interest rate
        """
        return self.__interest

    @get_interest.setter
    def get_interest(self, percent):
        """
        Expected interest range from 2 to 8
        """
        if type(percent) == int and 8 >= percent >= 2:
            self.__interest = percent

    def __str__(self):
        return f'Account ID:{self.account_id}, Balance: {self.balance}, Name: {self.name},' \
               f'Rate: {self.__interest} Date: {self.__creation_date}'

    def __del__(self):
        BankAccount.accounting(self.balance, income=False)
        print(f' {self.name}, your account will be  closed due to Bank liquidation, refund amount is {self.balance}')
        self.balance -= self.balance

    @classmethod
    def accounting(cls, summ, /, *, income: bool):
        if income:
            BankAccount.total_deposit += summ
        else:
            BankAccount.total_deposit -= summ

    def deposit(self, amount):
        """
        This metod provides functionality to deposit money to account
        """
        self.balance += amount
        BankAccount.accounting(amount, income=True)

    def withdraw(self, amount):
        """
        This metod provides functionality to withdraw money from account
        """
        if self.balance >= amount:
            self.balance -= amount
            BankAccount.accounting(amount, income=False)

    def transfer_money(self, amount, account):
        """
        This metod provides functionality to trasfer money form account to account
        """
        if self.balance >= amount:
            self.balance -= amount
            BankAccount.accounting(amount, income=False)
            account.balance += amount
            BankAccount.accounting(amount, income=True)

    @property
    def get_todays_profit(self):
        """
        This metod returns daily profit
        """
        todays_profit = (self.__interest / 365) * self.balance
        return todays_profit

    @staticmethod
    def bank_slogan():
        """
        This metod prints Bank Slogan
        """
        tprint(''' WE are 
        your Monte Cristo
        island!''', font="cybermedium")


account1 = BankAccount('Tom Clean', 100, 7)
account1.get_interest = 2
account1.deposit(100)
account1.withdraw(50)
account2 = BankAccount('Tom Dirt', 100, 8)
account1.transfer_money(50, account2)
account3 = BankAccount('Tom Saint', 770, 7)
account3.withdraw(110)
BankAccount.bank_slogan()
