# 1
"""<”O’zbekiston Vatan”im meni!!!>
so’zini console’ga chiqaramiz."""

print('<"O\'zbekiston Vatan"im meni!!!>')

# 2
"""Code to find the time of the trip.
Where distance and velocity was given."""
v = int(input("Enter a velocity (kilometers/hour) : "))
d = int(input("Enter a distance (kilometers) : "))

t = d / v
print(f"{t} time takes to finish the road")


# 4
"""Writ a code in a proper way"""
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \\ and the letter n")


# 5
"""change the values of the variables"""

a = float(input("Enter a first num : "))
b = float(input("Enter a second num : "))
a, b = b, a
print(f"printing a - {a}")
print(f"printing b - {b}")

# 6
"""Working with the f-strings"""

kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

new_str = f"{kocha} ko'chasi, {mahalla} mahallsi, {tuman} tumani, {viloyat} viloyati"

print(new_str.title())
print(new_str.upper())
print(new_str.lower())
print(new_str.capitalize())

# 7
"""Working with th the arithmetic expressions"""

a = float(input("Enter a first num : "))
b = float(input("Enter a second num : "))

print(a + b)  # plus
print(a - b)  # minus
print(a * b)  # multiplication
print(a / b)  # division
print(a // b)  # division (shows only whole part)
print(a % b)  # #division (shows only remainder)
