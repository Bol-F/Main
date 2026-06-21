"""Functions

Functions help you split a program into small reusable parts.
A good function has one clear job, a clear name, inputs, and usually a return value.
"""


"""Basic function"""


def greet():
    print("Hello, Python student!")


greet()


"""Parameters"""


def greet_user(name):
    print(f"Welcome, {name}!")


greet_user("Alice")


"""Return values"""


def add_numbers(a, b):
    return a + b


total = add_numbers(5, 7)
print(total)


"""Default parameter values"""


def introduce(name, country="Uzbekistan"):
    return f"My name is {name}. I am from {country}."


print(introduce("Ali"))
print(introduce("Sara", "Canada"))


"""Keyword arguments"""


def calculate_price(price, quantity, discount=0):
    subtotal = price * quantity
    return subtotal - discount


print(calculate_price(price=10, quantity=3, discount=5))


"""Scope"""

message = "I am outside the function"


def show_scope():
    message = "I am inside the function"
    print(message)


show_scope()
print(message)


"""Avoid mutable default arguments

Do not use a list or dictionary as a default value if the function will change it.
Use None, then create a new list inside the function.
"""


def add_grade(grade, grades=None):
    if grades is None:
        grades = []
    grades.append(grade)
    return grades


print(add_grade(90))
print(add_grade(75))


"""*args and **kwargs"""


def sum_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(sum_all(1, 2, 3, 4))


def print_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


print_profile(name="Bob", job="Developer", city="Tashkent")


"""Functions make code easier to test"""


def is_even(number):
    return number % 2 == 0


print(is_even(10))
print(is_even(7))


"""
                                Tasks

Task 1: Greeting Function
Write a function called greet_person that takes a name and prints "Hello, [name]!".

Task 2: Add Two Numbers
Write a function that takes two numbers and returns their sum.

Task 3: Area of a Rectangle
Write a function that takes width and height and returns the rectangle area.

Task 4: Even or Odd
Write a function that returns "even" if a number is even and "odd" if it is odd.

Task 5: Maximum of Three Numbers
Write a function that takes three numbers and returns the largest one.

Task 6: Count Vowels
Write a function that takes a word and returns how many vowels it contains.

Task 7: Reverse a String
Write a function that takes a string and returns the reversed string.

Task 8: List Average
Write a function that takes a list of numbers and returns the average.

Task 9: Safe Division
Write a function that divides two numbers. If the second number is zero, return "Cannot divide by zero".

Task 10: Student Grade
Write a function that takes a score from 0 to 100 and returns A, B, C, D, or F.
"""
