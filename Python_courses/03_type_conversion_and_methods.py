# converting data types to another
# this also works for boolean

x = "42"
print(int(x))  # Output: 42

y = 3.9
print(int(y))  # Output: 3 (truncates the decimal part)


x = 5
print(float(x))  # Output: 5.0 (converts integer to float)

y = "3.14"
print(float(y))  # Output: 3.14 (converts string to float)


x = 5
print(str(x))  # Output: "5" (converts integer to string)

y = 3.14
print(str(y))  # Output: "3.14" (converts float to string)


"""                Methods  (integer and floating)                       """

"""         abs() - Absolute Value
Returns the absolute (positive) value of a number."""

x = -10
print(abs(x))  # Output: 10

"""             pow() - Power
Returns x raised to the power of y (x^y).
You can also use three arguments to perform modulo with power:
pow(x, y, z) computes (x**y) % z.
"""

x = 3
y = 4
print(pow(x, y))  # Output: 81 (3^4)

z = 5
print(pow(x, y, z))  # Output: 1 (81 % 5)

"""                   divmod() - Division and Modulo
Returns a tuple containing the quotient and the remainder when dividing x by y.
"""

x = 10
y = 3
print(divmod(x, y))  # Output: (3, 1) -> 10 // 3 = 3 (quotient), 10 % 3 = 1 (remainder)

""" round() (for floating point numbers but also works with integers)
Rounds a number to the nearest integer, or you can specify the number of decimal places"""

x = 5.67
print(round(x))  # Output: 6 (rounds to the nearest integer)

y = 3.14159
print(round(y, 2))  # Output: 3.14 (rounds to 2 decimal places)


"""                 Methods (string)             """

"""                 len()
Returns the length of the string (how many characters it contains)"""

my_string = "hello"
print(len(my_string))  # Output: 5

"""                 .lower()
Converts the entire string to lowercase"""

my_string = "HELLO"
print(my_string.lower())  # Output: 'hello'

"""                 .upper()
Converts the entire string to uppercase"""

my_string = "hello"
print(my_string.upper())  # Output: 'HELLO'

"""                 .title()
capitalizes the first letter of each word in a string.
It’s useful when you want to format a string like a title,
where the first letter of each word should be capitalized"""

my_string = "hello world from python"
print(my_string.title())  # Output: 'Hello World From Python'


"""                 .strip()
Removes spaces (or other characters) from the beginning and end of the string"""

my_string = "  hello  "
print(my_string.strip())  # Output: 'hello'

"""                 .replace(old, new)
Replaces all occurrences of a substring with a new one"""

my_string = "hello world"
print(my_string.replace("world", "Python"))  # Output: 'hello Python'

"""                 .split()
Splits the string into a list at each space (or other separator)"""

my_string = "hello world"
print(my_string.split())  # Output: ['hello', 'world']

"""                 .find(sub)
Finds the position of a substring. If not found, it returns -1"""

my_string = "hello world"
print(my_string.find("world"))  # Output: 6
print(my_string.find("Python"))  # Output: -1


"""
                       Tasks

1. Integer to Float Conversion
Ask the user to input an integer, convert it to a float, and print the result

2. String to Integer Conversion
Ask the user to input a number as a string (e.g., "42"). Convert it to an integer and print the result

3. Rounding a Number
Ask the user to input a floating-point number. Round the number to the nearest integer and print the result

4. Power of a Number
Ask the user to input two integers: x and y. Use the pow() function to compute x raised to the power of y, and print the result

5. Division and Modulo with divmod()
Ask the user to input two numbers, x and y. Use the divmod() function to find the quotient and remainder of x / y and print the result

6. String Lowercase and Uppercase
Ask the user to input a string. Print the string in both lowercase and uppercase

7. String Title Case
Ask the user to input a sentence. Convert and print the sentence with each word's first letter capitalized using the title() method

8. String Stripping
Ask the user to input a string with spaces at the beginning and end (e.g., " hello "). Remove the spaces using strip() and print the cleaned-up string

9. String Replacement
Ask the user to input a string. Replace all occurrences of the word "apple" with "orange" and print the modified string

10. String Slicing
Ask the user to input a string. Print a substring containing only the first 3 characters, and a substring from the 2nd to the 4th character
"""
