"""     Dict    """


"""
A dictionary in Python is a built-in data structure that stores data in key-value pairs. 
It’s like a real-world dictionary where you look up a word (key) and get its meaning (value).


        Syntax:
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}


Keys must be unique and immutable (strings, numbers, or tuples).
Values can be any data type (numbers, strings, lists, other dictionaries, etc.).
"""



"""             Dictionary Methods & Operations             """

my_dict = {"name": "Alice", "age": 30}

# Accessing values
print(my_dict["name"])  # Alice
print(my_dict.get("age"))  # 30

# Adding & updating values
my_dict["city"] = "London"
my_dict["age"] = 31  # Update value

# Removing items
del my_dict["age"]  # Removes 'age'
popped_value = my_dict.pop("city")  # Removes 'city' and returns its value

# Checking if key exists
if "name" in my_dict:
    print("Key exists!")




"""         Looping Through a Dictionary            """

for key, value in my_dict.items():
    print(f"{key}: {value}")


"""         Nested Dictionaries            """

users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
print(users["user1"]["name"])  # Alice



"""         Default Dictionary (collections.defaultdict)            """

from collections import defaultdict

default_dict = defaultdict(int)  # Default value is 0 for missing keys
default_dict["a"] += 1
print(default_dict["b"])  # Output: 0 (instead of KeyError)


"""
                TASKS              

Task 1: Create a Dictionary
Create a dictionary called student_info with the following keys and values:

"name" → "Alice"
"age" → 22
"major" → "Cybersecurity"
Print the dictionary.

Task 2: Access Dictionary Values Safely
Given the dictionary student_info from Task 1, 
print the value of "age" using the .get() method to avoid errors if the key is missing.

Task 3: Add and Update Dictionary Elements
Add a new key "GPA" with a value of 3.9 to student_info.
Update the "age" to 23.
Print the updated dictionary.

Task 4: Remove a Key from a Dictionary
Remove the "major" key from student_info 
using the .pop() method and print the modified dictionary.

Task 5: Loop Through a Dictionary
Given the dictionary:
prices = {"apple": 1.5, "banana": 0.75, "cherry": 2.0}
Write a loop that prints each item and its price in the format:

apple costs $1.5  
banana costs $0.75  
cherry costs $2.0  

Task 6: Count Word Frequency
Given the list of words:
words = ["apple", "banana", "apple", "cherry", "banana", "banana"]
Use a dictionary to count and print how many times each word appears.

Task 7: Merge Two Dictionaries
Given two dictionaries:
dict1 = {"x": 10, "y": 20}
dict2 = {"y": 30, "z": 40}
Merge dict2 into dict1 using the .update() method and print the result.

Task 8: Dictionary Comprehension
Create a dictionary where the keys are numbers from 1 to 5 and the values are their squares.

Example output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

Task 9: Modify a Nested Dictionary
Given the dictionary:

user_data = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
Write code to increase the age of each user by 1.

Task 10: Use defaultdict for Missing Keys
Use collections.defaultdict to create a dictionary where missing keys default to an empty list.

Add "apple" to the "fruits" key.
Add "carrot" to the "vegetables" key.
Print the dictionary.
"""
