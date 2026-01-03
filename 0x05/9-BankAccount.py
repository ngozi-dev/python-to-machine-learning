#!/usr/bin/python3
# a module that creates a class of BankAccount with public instance
# attributes account_number and balance as private instance attribute

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number # public instance attribute account_number
        self.__balance = balance # private instance attribute balance
    
    def deposit(self, amount):
        """public method to deposit amount to the account"""
        if amount > 0:
            self.__balance += amount
            return True
        return False
    def withdraw(self, amount):
        """public method to withdraw amount from the account"""
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    def get_balance(self):
        """public method to get the current balance"""
        return self.__balance


if __name__ == "__main__":
    bankaccount = BankAccount("123456789", 20000)
    print(bankaccount.account_number)
    try:
        print(bankaccount.__balance)
    except Exception as e:
        print("Account Balance is a private instance attribute")
    print(bankaccount.get_balance())
    print(bankaccount.deposit(5000))
    print(bankaccount.withdraw(10000))
    print(bankaccount.get_balance())    
    