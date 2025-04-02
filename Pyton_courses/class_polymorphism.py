"""
                    Explanation
Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass.
It enables a single interface to represent different types, which can be particularly powerful when working with inheritance.

In simpler terms, polymorphism allows you to define methods in a base class and have those methods be overridden by subclasses to provide specific behavior.
This allows for flexibility and extensibility in code, where the same method can behave differently depending on the object calling it.
"""

"""         EXAMPLE No_1        """


# Define the Grandparent class
class Grandparent:
    # Method speak for the Grandparent class
    def speak(self):
        print('Grandparent says, "Back in my day..."')


# Define the Parent class inheriting from Grandparent
class Parent(Grandparent):
    # Method speak overridden in Parent class
    def speak(self):
        print('Parent says, "When I was your age..."')


# Define the Child class inheriting from Parent
class Child(Parent):
    # Method speak overridden in Child class
    def speak(self):
        print('Child says, "Can I have some money?"')


# Define the Grandchild class inheriting from Child
class Grandchild(Child):
    # Method speak overridden in Grandchild class
    def speak(self):
        print('Grandchild says, "I love my Lego set!"')


# Create instances of each class
grandparent = Grandparent()
parent = Parent()
child = Child()
grandchild = Grandchild()

# Demonstrating polymorphism
for person in (grandparent, parent, child, grandchild):
    person.speak()

"""         EXAMPLE No_2        """


# Define the Animal class
class Animal:
    # Method sound for the Animal class
    def sound(self):
        print('Some generic animal sound')


# Define the Mammal class inheriting from Animal
class Mammal(Animal):
    # Method sound overridden in Mammal class
    def sound(self):
        print('Mammal makes a sound')


# Define the Bird class inheriting from Animal
class Bird(Animal):
    # Method sound overridden in Bird class
    def sound(self):
        print('Bird chirps')


# Create instances of each class
animal = Animal()
mammal = Mammal()
bird = Bird()

# Demonstrating polymorphism
for creature in (animal, mammal, bird):
    # Call the sound method on each object
    creature.sound()
