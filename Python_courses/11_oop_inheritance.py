"""
                            Explanation
Inheritance is a key concept in object-oriented programming (OOP).
It allows one class (called the child class or subclass) to inherit attributes and methods from another class (called the parent class or superclass).
This promotes code reuse, enables a hierarchical structure, and simplifies code maintenance.


                            Key Concepts
Parent Class (Superclass): The base class that provides attributes and methods to its subclasses.
Child Class (Subclass): A class that inherits from a parent class and can have additional attributes or methods.
super(): A function that allows access to the parent class’s methods or attributes,
often used to call the parent class constructor (__init__()).
"""

"""         EXAMPLE No_1        """


# Defining a class A, and two subclasses B and C of A
class A:
    # Initialize an object of class A with attributes att1 and att2
    def __init__(self, att1, att2):
        self.att1, self.att2 = att1, att2


# Defining subclass B of A
class B(A):
    # Initialize an object of class B with att1, att2, and att3
    def __init__(self, att1, att2, att3):
        super().__init__(att1, att2)  # Call the constructor of class A
        self.att3 = att3


# Defining subclass C of A
class C(A):
    # Initialize an object of class C with  att1, att2, and att4
    def __init__(self, att1, att2, att4):
        super().__init__(att1, att2)  # Call the constructor of class A
        self.att4 = att4


# Defining subclass D of C
class D(C):
    # Initialize an object of class D with att1, att2, att4, and att5
    def __init__(self, att1, att2, att4, att5):
        super().__init__(att1, att2, att4)  # Call the constructor of class C
        self.att5 = att5
