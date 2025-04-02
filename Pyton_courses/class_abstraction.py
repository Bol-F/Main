"""
                        EXPLANATION
Abstraction is the concept of hiding unnecessary details and showing only relevant features to the user.

Think of a car:
You just press the gas pedal, and it moves.
You don’t need to know how the engine, fuel injection, or transmission work.
The complex details are hidden behind an easy-to-use interface.
"""

"""         EXAMPLE No_1        """

from abc import ABC, abstractmethod  # Import Abstract Base Class module


# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass  # Abstract method (must be implemented in subclasses)


# Concrete class (child class)
class Car(Vehicle):
    def start(self):
        print("Car engine started 🚗")


class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle engine started 🏍️")


# Usage
car = Car()
bike = Motorcycle()

car.start()  # Output: Car engine started 🚗
bike.start()  # Output: Motorcycle engine started 🏍️

"""         EXAMPLE No_2        """

from abc import ABC, abstractmethod  # Import Abstract Base Class module


# Abstract class
class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance  # Protected attribute

    @abstractmethod
    def deposit(self, amount):
        pass  # Must be implemented in child classes

    @abstractmethod
    def withdraw(self, amount):
        pass  # Must be implemented in child classes


# Concrete class (Savings Account)
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")


# Concrete class (Checking Account)
class CheckingAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount < -500:  # Checking account allows overdraft of $500
            print("Overdraft limit reached!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")


# Usage
savings = SavingsAccount(1000)
savings.deposit(500)  # Deposited 500. New Balance: 1500
savings.withdraw(2000)  # Insufficient funds!

checking = CheckingAccount(1000)
checking.withdraw(1400)  # Withdrew 1400. New Balance: -400
checking.withdraw(200)  # Overdraft limit reached!

"""         EXAMPLE No_2        """

# Import ABC and abstractmethod from the abc module
from abc import ABC, abstractmethod


# Define an abstract base class FileHandler
class FileHandler(ABC):
    # Abstract method read, which must be implemented by any subclass
    @abstractmethod
    def read(self, file_path):
        pass

    # Abstract method write, which must be implemented by any subclass
    @abstractmethod
    def write(self, file_path, data):
        pass


# Define a concrete class TextFileHandler inheriting from FileHandler
class TextFileHandler(FileHandler):
    # Implementation of the read abstract method
    def read(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    # Implementation of the write abstract method
    def write(self, file_path, data):
        with open(file_path, 'w') as file:
            file.write(data)


# Define a concrete class BinaryFileHandler inheriting from FileHandler
class BinaryFileHandler(FileHandler):
    # Implementation of the read abstract method
    def read(self, file_path):
        with open(file_path, 'rb') as file:
            return file.read()

    # Implementation of the write abstract method
    def write(self, file_path, data):
        with open(file_path, 'wb') as file:
            file.write(data)


# Using the abstract interface
# Create an instance of TextFileHandler and call write and read
text_handler = TextFileHandler()
text_handler.write('sample.txt', 'Hello, World!')
print(text_handler.read('sample.txt'))  # Output: Hello, World!

# Create an instance of BinaryFileHandler and call write and read
binary_handler = BinaryFileHandler()
binary_handler.write('sample.bin', b'\x00\xFF')
print(binary_handler.read('sample.bin'))  # Output: b'\x00\xff'
