"""
                        Explanation
Encapsulation is one of the fundamental principles of object-oriented programming (OOP).
It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class.
Encapsulation also involves restricting direct access to some of an object's components, which is a way of preventing accidental interference and misuse of the data.

In simpler terms, encapsulation helps to hide the internal state of an object from the outside world and only expose a controlled interface.
This can be achieved through the use of access modifiers like protected (_) and private (__).
"""

"""         EXAMPLE No_1        """


# Define the BankAccount class
class BankAccount:
    def __init__(self, owner, balance=0):
        # Public attribute: owner
        self.owner = owner

        # Private attribute: balance (indicated by double underscores)
        self.__balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'{amount} deposited. New balance: {self.__balance}')
        else:
            print('Deposit amount must be positive')

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'{amount} withdrawn. New balance: {self.__balance}')
        else:
            print('Insufficient balance or invalid withdrawal amount')

    # Method to get the current balance
    def get_balance(self):
        return self.__balance


# Create a BankAccount object
account = BankAccount('Alice', 1000)

# Accessing public attribute
print(account.owner)  # Output: Alice

# Attempting to access private attribute directly (raises AttributeError)
# print(account.__balance)

# Using public methods to interact with private attribute
account.deposit(500)  # Output: 500 deposited. New balance: 1500
account.withdraw(200)  # Output: 200 withdrawn. New balance: 1300

# Getting the balance using a public method
print(f'Current balance: {account.get_balance()}')  # Output: 1300

"""         EXAMPLE No_2        """


# Define the Student class
class Student:
    def __init__(self, name, grades=[]):
        # Public attribute: name
        self.name = name

        # Private attribute: grades (indicated by double underscores)
        self.__grades = grades

    # Method to add a grade
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f'Grade {grade} added.')
        else:
            print('Invalid grade')

    # Method to get the grades
    def get_grades(self):
        return self.__grades

    # Method to calculate the average grade
    def get_average_grade(self):
        return sum(self.__grades) / len(self.__grades) if self.__grades else 0


# Create a Student object
student = Student('John')

# Adding grades using public method
student.add_grade(85)
student.add_grade(92)

# Attempting to access private attribute directly (raises AttributeError)
# print(student.__grades)

# Using public methods to interact with private attribute
print(f'Grades: {student.get_grades()}')  # Output: [85, 92]
print(f'Average Grade: {student.get_average_grade()}')  # Output: 88.5

"""         EXAMPLE No_3        """


# Define the Car class
class Car:
    def __init__(self, make, model):
        # Public attributes: make and model
        self.make = make
        self.model = model

        # Private attribute: engine_running (indicated by double underscores)
        self.__engine_running = False

    # Method to start the engine
    def start_engine(self):
        if not self.__engine_running:
            self.__engine_running = True
            print(f'{self.make} {self.model} engine started.')
        else:
            print(f'{self.make} {self.model} engine is already running.')

    # Method to stop the engine
    def stop_engine(self):
        if self.__engine_running:
            self.__engine_running = False
            print(f'{self.make} {self.model} engine stopped.')
        else:
            print(f'{self.make} {self.model} engine is not running.')

    # Method to check if the engine is running
    def is_engine_running(self):
        return self.__engine_running


# Create a Car object
car = Car('Toyota', 'Camry')

# Starting the engine using public method
car.start_engine()  # Output: Toyota Camry engine started.

# Checking engine state
print(f'Is engine running? {car.is_engine_running()}')  # Output: True

# Stopping the engine using public method
car.stop_engine()  # Output: Toyota Camry engine stopped.

# Attempting to access private attribute directly (raises AttributeError)
# print(car.__engine_running)
