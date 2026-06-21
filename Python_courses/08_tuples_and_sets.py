"""tuple"""

"""
A tuple is an ordered, immutable collection of elements.

Ordered: Elements have a fixed position (index).

Immutable: Once created, it cannot be modified (no adding, removing, or changing elements).

Syntax: Defined with parentheses ( ).
"""

point = (10, 20)  # (x, y) coordinates

location_map = {(35.7, 139.7): "Tokyo", (40.7, -74.0): "New York"}


# functions
# count()

t = (1, 2, 3, 2, 2)
print(t.count(2))  # Output: 3


# index()

t = ("a", "b", "c", "b")
print(t.index("b"))  # Output: 1


"""set """

"""
A set is an unordered, mutable collection of unique elements.

Unordered: No fixed position (no indexing).

Mutable: Elements can be added/removed after creation.

Unique Elements: Automatically removes duplicates.

Syntax: Defined with curly braces { } or set().
"""

numbers = [1, 2, 2, 3, 4, 4]
unique = set(numbers)  # {1, 2, 3, 4}


# Unions (|), intersections (&), differences (-), etc.

admins = {"alice", "bob"}
users = {"bob", "dave"}
admins & users  # Intersection: {"bob"}


# functions

# add()

s = {1, 2, 3}
s.add(4)  # {1, 2, 3, 4}

# update()

s = {1, 2}
s.update([3, 4], (5,))  # {1, 2, 3, 4, 5}

# remove() / discard()

s = {1, 2, 3}
s.remove(3)  # {1, 2}
s.discard(99)  # No error

# issubset() / issuperset()

a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True
print(b.issuperset(a))  # True

# isdisjoint()
# Check if sets have no common elements.

a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True
