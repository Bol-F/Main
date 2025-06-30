"""List"""

"""
A list is an ordered collection of items.
Lists can contain items of different data types
and the elements are indexed, meaning you can access them by their position
"""


my_list = [1, 2, 3, 4, 5]

# Accessing items: You can access elements by their index (starting from 0)
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3


"""  Adding items  """

my_list.append(6)  # Adds 6 to the end of the list
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]


"""  Modifying items  """

my_list[1] = 10  # Changes the second element to 10
print(my_list)  # Output: [1, 10, 3, 4, 5, 6]


"""  Removing items  """

my_list.remove(3)  # Removes the element 3
print(my_list)  # Output: [1, 10, 4, 5, 6]


"""  List slicing  (also works for string)"""

sublist = my_list[1:4]  # Get elements from index 1 to 3
print(sublist)  # Output: [10, 4, 5]


"""       Tuple      """

"""
A tuple is an ordered, immutable collection of elements.
Like lists, tuples can store multiple items,
but unlike lists, once you create a tuple, you cannot modify its contents
(i.e., you can't add, remove, or change elements after the tuple is created).
"""

"""  
                  Key Features of Tuples  
Ordered: Elements in a tuple have a defined order, meaning the items will appear in the order they were inserted.
Immutable: Once created, you cannot modify, add, or remove elements from a tuple.
Can Contain Different Data Types: Tuples can hold elements of any data type (e.g., integers, strings, lists, etc.).
Indexed: You can access tuple elements using indexing (like lists).
"""

my_tuple = (1, 2, 3, 4)
print(my_tuple)  # Output: (1, 2, 3, 4)


# If you have a single element in a tuple, you need to add a comma after the element to make it a tuple
single_element_tuple = (5,)
print(single_element_tuple)  # Output: (5,)


""" Just like lists, you can slice tuples to get a range of elements """

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)  (from index 1 to 3)


"""  Combine to tuples (also can be used for list)  """

tuple1 = (1, 2)
tuple2 = (3, 4)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4)


"""  Repeating: You can repeat a tuple multiple times using the * operator  """

my_tuple = (1, 2)
repeated_tuple = my_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)


"""   Tuple Unpacking   """

my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a)  # Output: 10
print(b)  # Output: 20
print(c)  # Output: 30


"""   Nested Tuples   """

nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1])  # Output: (3, 4)
print(nested_tuple[1][0])  # Output: 3  (accessing inner tuple element)


""" 
                Advantages
Immutability:
Because tuples are immutable, they are hashable, which makes them useful as keys in dictionaries or elements in sets

Performance:
Tuples can be more memory-efficient and faster than lists when you have a fixed collection of elements that you don’t need to modify

Safety:
Using tuples ensures that the data remains unchanged, which can be useful in certain situations where immutability is required
"""


"""   
                                       Tasks
1. Create a list of 5 elements (can be integers or strings) and print the first, second, and last element using indexing.

2. Add a new element to the end of a list. How would you do that? What method or operator would you use?

3. Remove the second element from a list of 4 elements. How can you remove an element by its value and by its index?

4. Create a list of 6 numbers and use slicing to extract a sublist that contains the 3rd to 5th elements (inclusive).

5. Sort a list of 5 random integers in ascending order, and then reverse the sorted list.

6. Create a list comprehension that creates a new list with only the even numbers from 1 to 20.

7. How can you check if a list contains a specific element? Write a simple condition to check for the presence of a number in a list.

8. Create a tuple with 4 elements. Then, try to modify the second element. What happens, and why can’t you modify a tuple?

9. Create a tuple of tuples. Access and print the first element of the second tuple within the main tuple.

10. Unpack a tuple of 3 elements into 3 separate variables. Print out the values of the variables.
"""
