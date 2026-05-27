from abc import ABC, abstractmethod

class bank(ABC):
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def _update_balance(self,amount):
        self.__balance = amount
        
    @abstractmethod
    def acount_type(self):
        pass

class SavingAccount(BankAccount):
    def account_type(self):
        return "saving account"
    def deposit(self,amount):
        new_balance = self.getbalance() + amount
        self._update_balance(new_balance)
        print("deposited:", amount)
        
    def withdraw(self,amount):
        if amount <= self.get_balance():
            new_balace = self.get_balance() - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")