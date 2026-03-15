"try-except"

"""try:
    # code, which might cause an error
except:
    # code, which will work if error occurs
else:
    # code, which work if there is no error
finally:
    # code, which will work anyways"""



# except
#
# The except block runs if an error happens inside try.

try:
    x = 10 / 0
except:
    print("An error occurred")

# It is better to specify the exact error:
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")



# The else block runs only if there was NO error in try.

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("No error occurred")


# finally

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error")
finally:
    print("This always runs")

# example
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("You must enter numbers")
else:
    print("Result:", result)
finally:
    print("Program finished")

"""What happens here:

try
Python tries to run the code.

except ZeroDivisionError
Handles division by zero.

except ValueError
Handles wrong input (letters instead of numbers).

else
Runs if there was no error.

finally
Runs in every case."""

# also u'll mostly use this kind of style || except Exception as e:

# try:
#     # risky code
# except Exception as e:
#     print("Error:", e)

# a
try:
    x = 10 / 0
except Exception as e:
    print("Something went wrong:", e)

# b
try:
    num = int("hello")
except Exception as e:
    print("Error type message:", e)


"""
                TASKS    
Task 1

Write a program that asks the user to enter two numbers and divides the first number by the second.
Handle the division by zero error using except.

Task 2

Write a program that asks the user to enter an integer and multiplies it by 10.
Handle the error if the user enters text instead of a number.

Task 3

Write a program that asks the user to enter a number and divides 100 by that number.
Catch errors using:

except Exception as e

Print the error message stored in e.

Task 4

Write a program that asks the user to enter two numbers.
Divide them inside a try block.
Use else to print the result only if no error occurs.

Task 5

Write a program that asks the user to enter a number.
Convert the input to int.
Use finally to always print:

Program finished
Task 6

Write a program that asks the user for a number and divides 50 by it.
Catch errors using:

except Exception as e

Print:

the type of error

the error message

Task 7

Write a program that asks the user to enter two numbers and divides them.
Handle two types of exceptions:

ValueError

ZeroDivisionError

Print a different message for each error.

Task 8

Write a program that tries to open a file called data.txt.
If the file does not exist, handle the error and print:

File not found
Task 9

Write a program that uses all four blocks:

try
except
else
finally

The program should:

ask the user for a number

divide 20 by that number

print the result if successful

print an error if something goes wrong

always print "End of program"

Task 10

Write a program that works like a simple calculator.
The program should:

ask for two numbers

ask for an operation (+, -, *, /)

perform the calculation inside try

handle errors using except Exception as e

print the error message if something goes wrong.
"""