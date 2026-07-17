from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, owner, balance):
        self.owner = owner  
        self.__balance = balance  

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Error: Balance cannot be negative!")

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited. New balance: {self.__balance}")

    @abstractmethod
    def get_account_type(self):
        pass

class SavingsAccount(BankAccount):
    def get_account_type(self):
        return "Savings Account"

    def apply_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"Interest applied. New balance: {self.balance}")



my_account = SavingsAccount("Ali", 1000)

print(f"Owner: {my_account.owner}")
print(f"Type: {my_account.get_account_type()}")



print(f"Current Balance: {my_account.balance}")

my_account.balance = 2000
my_account.balance = -500  

my_account.deposit(500)
my_account.apply_interest()
