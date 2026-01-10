#!/usr/bin/python3
# a nodule that carries out encapsulation

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        """ Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
            return True
        return False
    def withdraw (self, amount):
        """ Public method to withdraw money"""
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
     # getter method for balance
    def balance(self):
        """retrive the balance attribute"""
        return self.__balance

    


if __name__ == "__main__":
    bankaccount = BankAccount("0123456789", 5000)
    print(bankaccount.balance())
    bankaccount.withdraw(2000)
    print(bankaccount.balance())
    bankaccount.deposit(10000)
    print(bankaccount.balance())