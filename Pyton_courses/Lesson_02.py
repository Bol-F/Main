"""Variables and Data Types"""

first_name = "John"  # String
my_age = 25  # Integer
height = 5.9  # Float
is_student = True  # Boolean


"""Basic Operations with Variables and Data Types
            Integer and Float Operations           """

a = 10
b = 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division (result is float)
print(a // b)  # Integer division (floor division)
print(a % b)  # Modulo (remainder)
print(a**b)  # Exponentiation (a raised to the power of b)

"""                String Operations               """

greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name  # Concatenation
print(full_greeting)  # Hello, Alice

repeat_greeting = greeting * 3  # Repeat the string 3 times
print(repeat_greeting)  # HelloHelloHello

"""                Boolean Operations              """
# The Boolean data type in Python has only two possible values: True or False.
"""AND (and):
This operator returns True if both conditions are True. Otherwise, it returns False.
Example:
True and True will return True, but True and False will return False.

OR (or):
This operator returns True if at least one of the conditions is True. It only returns False if both conditions are False.
Example:
True or False will return True, and False or False will return False.

NOT (not):
This operator inverts the Boolean value. If the value is True, it will return False, and if it's False, it will return True.
Example:
not True will return False, and not False will return True."""

a = True
b = False
print(a and b)  # False because one condition is False

x = 5
y = 10
print(x < 10 and y > 5)  # True because both conditions are True


a = True
b = False
print(a or b)  # True because at least one condition is True

x = 5
y = 2
print(x < 10 or y > 5)  # True because the first condition is True


a = True
b = False
print(not a)  # False because "a" is True, so "not a" is False
print(not b)  # True because "b" is False, so "not b" is True

"""Combining Multiple Boolean Operations"""

x = 7
y = 10
z = 5
print(
    x < 10 and (y > 5 or z == 5)
)  # True because both parts of the expression are true


"""
                                Tasks
1. Print Personal Information
Write a program that stores your first name, age, and height in variables.
Then, print them out in a sentence like: "My name is [first_name], I am [age] years old, and my height is [height] meters."

2. Basic Arithmetic Operations
Write a program that asks the user for two numbers and performs the following operations:

Addition
Subtraction
Multiplication
Division (resulting in float)
Integer Division
Modulo (remainder) Then, print the results of each operation.

3. Check Even or Odd
Ask the user for a number. Use an if-else statement to check if the number is even or odd. Print the result.

4. String Concatenation and Repetition
Write a program that:

Combines two strings (e.g., "Good" and "Morning") using concatenation.
Repeats a string (e.g., "Python") 5 times using the multiplication operator and prints the result.

5. Grade Classification
Write a program that takes a numeric score from the user and classifies it into a grade:

A: 90–100
B: 80–89
C: 70–79
D: 60–69
F: Below 60 Display the grade.

6. Age Category Check
Ask the user for their age. Use if-else statements to check and print whether they are:

a minor (under 18)
an adult (18–64)
a senior citizen (65 and above)

7. Multiplication Table
Write a program that asks the user for a number and then prints its multiplication table from 1 to 10. For example, if the user enters 3, print:

3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30 

8. Check Voting Eligibility
Ask the user for their age. Print whether they are eligible to vote (age 18 or older). If not, tell them how many years are left until they can vote.

9. Multiple Boolean Operations
Write a program that checks multiple conditions:

Ask the user for two numbers.
Check if the first number is greater than 10 AND the second number is less than 20. Print whether both conditions are true.
Check if the first number is greater than 10 OR the second number is less than 20. Print whether at least one condition is true.
Check if neither number is equal to 5 using the NOT operator and print the result.

10. Largest of Three Numbers
Ask the user for three numbers and print the largest number using if-elif-else statements.
"""
