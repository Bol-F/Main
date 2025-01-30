"""  While Loop  """

"""
Basic Structure of a while Loop
Here’s the basic syntax for a while loop:

while condition:
    # Code to execute repeatedly while the condition is true
"""


"""
               How It Works
The condition is checked.
If the condition is True, the code inside the loop is executed.
After the code block runs, the condition is checked again.
This repeats until the condition becomes False.
"""

i = 1

while i <= 5:
    print(i)
    i += 1  # This is the step to increment 'i' by 1 each time

"""
Explanation:
The condition is i <= 5, so as long as i is less than or equal to 5, the loop will keep running.
Inside the loop, it prints i and then increments i by 1.
"""

# Output
# 1
# 2
# 3
# 4
# 5


"""
Infinite Loop (Be Careful!)
An infinite loop happens when the condition never becomes False. Here’s an example:
"""

while True:
    print("This will run forever!")

"""
This loop will run endlessly and keep printing "This will run forever!" because True is always true.
To stop this, you would need to interrupt the program manually (like pressing Ctrl + C).

Avoiding Infinite Loops
To avoid infinite loops, always make sure that your loop has a way of breaking out of it when needed.
Usually, you’ll update the condition inside the loop so that it eventually becomes False.
"""






"""  Using break and continue with while Loops  """


"""
                            break Statement
The break statement is used to exit the loop before the condition becomes False.
It forces the loop to stop immediately.
"""

i = 1

while i <= 10:
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
    i += 1

# Output:
# 1
# 2
# 3
# 4



"""
                                continue Statement
The continue statement skips the current iteration and moves to the next iteration of the loop.
"""

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue  # Skip printing 3
    print(i)

# Output:
# 1
# 2
# 4
# 5



"""
      Using else with a while Loop
You can also use an else block with a while loop.
The else block runs after the loop finishes, 
but it will not run if the loop is exited using a break statement.
"""

i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print("Loop finished!")

"""
Explanation:
Once i becomes greater than 5, the loop ends,
and the else block is executed, printing "Loop finished!".
"""

# Output:
# 1
# 2
# 3
# 4
# 5
# Loop finished!

"""           Summary of while Loops
A while loop runs as long as a condition is True.
The loop’s body executes repeatedly, and you can control when the loop stops using break,
continue, and ensuring that the condition eventually becomes False.
The else block can be used with a while loop, but it runs only if the loop ends without a break.
"""






"""
                             Tasks
Task 1: Print All Even Numbers Between 1 and 20
Write a while loop that prints all even numbers between 1 and 20.

Task 2: Sum of Odd Numbers from 1 to 50
Write a while loop that calculates and prints the sum of all odd numbers between 1 and 50.

Task 3: Count Down from 10 to 1
Write a while loop that counts down from 10 to 1, printing each number on a new line.

Task 4: Factorial Calculation
Write a while loop that calculates the factorial of a number (e.g., 5!). The factorial of a number n is n * (n-1) * (n-2) * ... * 1.

Task 5: Print Multiples of 3 Until 100
Write a while loop that prints all multiples of 3 between 1 and 100.

Task 6: Ask User for Numbers Until They Enter Zero
Write a while loop that repeatedly asks the user to enter a number. The loop should stop when the user enters 0.

Task 7: Print Fibonacci Sequence
Write a while loop that prints the Fibonacci sequence up to the 10th number.
(The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two previous numbers.)

Task 8: Guess the Number Game
Write a while loop that asks the user to guess a number between 1 and 10.
The loop should keep running until the user guesses the correct number.

Task 9: Find the Largest Number in a List
Write a while loop that finds and prints the largest number in the list: numbers = [23, 45, 12, 56, 78, 34].

Task 10: Print a Square Pattern
Write a while loop that prints a square pattern of stars (*).
For example, for a size of 5, it should print:
*****
*****
*****
*****
*****
"""