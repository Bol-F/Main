"""  For loop  """

"""
Basic Structure of a for Loop
The for loop is used to iterate over a sequence (such as a list, tuple, string, or range).
Here's a simple syntax for it:

for item in sequence:
    # Code to execute for each item in the sequence
"""

"""
item: 
A variable that represents each element in the sequence.
It will take the value of each item in the sequence one by one.

sequence:
A collection of values you want to loop through (could be a list, string, etc.).
"""


"""  Looping a list  """

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry


"""  Looping a srting  """

word = "hello"

for letter in word:
    print(letter)

# Output:
# h
# e
# l
# l
# o



"""   Using range() with a for Loop   """

"""Sometimes, you don’t need a specific collection like a list or string.
You might just want to repeat something a certain number of times.
You can do that with range().

What is range()? range() is a built-in function that creates a sequence of numbers.
By default, it starts at 0 and goes up to a number you specify (but does not include that number)."""

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


for i in range(2, 7):
    print(i)

"""
Explanation:
range(2, 7) starts at 2 and stops before 7.
It will print 2, 3, 4, 5, 6.
"""

# Output:
# 2
# 3
# 4
# 5
# 6

"""  range() with Step  """

for i in range(1, 10, 2):
    print(i)

"""
range(1, 10, 2) starts at 1, stops before 10, and increments by 2 each time.
It will print 1, 3, 5, 7, 9
"""

# Output
# 1
# 3
# 5
# 7
# 9


"""   Nested for Loops   """
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()  # To print a new line after each row

"""
Explanation:
The outer loop goes through each list (row) in the matrix.
The inner loop goes through each number in the current row.
end=" " makes sure the numbers are printed on the same line, separated by spaces.
"""

# Output:
# 1 2 3
# 4 5 6
# 7 8 9




"""          
                          Tasks       
Task 1: Print Each Character of a String
Write a for loop that prints each character of the string "Python" on a new line.

Task 2: Print Numbers from 1 to 10
Write a for loop that prints the numbers from 1 to 10 (inclusive).

Task 3: Print Even Numbers from 1 to 20
Write a for loop that prints only the even numbers from 1 to 20.

Task 4: Sum of Numbers from 1 to 100
Write a for loop that calculates and prints the sum of numbers from 1 to 100.

Task 5: Loop Through a List of Fruits
You have a list of fruits: fruits = ["apple", "orange", "banana", "kiwi"].
Write a for loop that prints each fruit in the list in uppercase (e.g., APPLE, ORANGE, etc.).

Task 6: Create a Multiplication Table
Write a for loop that prints the multiplication table for the number 5 (from 5x1 to 5x10). For example:

Task 7: Find the Largest Number in a List
Write a for loop that finds and prints the largest number in the list: numbers = [12, 56, 34, 89, 23, 45].

Task 8: Create a List of Squares
Write a for loop that creates and prints a new list containing the squares of numbers from 1 to 10.
For example, the list should contain [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].

Task 9: Reverse a String
Write a for loop that prints the reverse of the string "programming". The output should be "gnimmargorp".

Task 10: Count How Many Times a Character Appears in a String
Write a for loop that counts how many times the letter 'o' appears in the string "hello world",
and print the result.
"""