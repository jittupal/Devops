'''
Class Method:
        - A class method is a method that operates on the class itself rather than an instance.
        - It is defined using the `@classmethod` decorator.
        - It takes `cls` (class reference) as its first parameter instead of `self`.
        - It can modify class-level attributes but cannot access instance attributes directly.
'''



class Student:
    school_name = "ABC High School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name  # Modifies the class attribute

    @classmethod
    def from_string(cls, student_info):
        name, age = student_info.split("-")
        return cls(name, int(age))  # Creates and returns a new instance

# Using the class method to modify class attribute
print("Before:", Student.school_name)
Student.change_school("XYZ Academy")
print("After:", Student.school_name)

# Using the class method as an alternative constructor
student = Student.from_string("John-18")
print(f"Student: {student.name}, Age: {student.age}, School: {student.school_name}")

class User:
    count = 0  # Class attribute to track the number of instances

    def __init__(self, name):
        self.name = name
        User.count += 1

    @classmethod
    def get_instance_count(cls):
        """Returns the number of instances created."""
        return cls.count

# Creating instances
u1 = User("John")
u2 = User("Emily")

# Getting count using class method
print("Total Users:", User.get_instance_count())


class Animal:
    species = "Unknown"

    @classmethod
    def set_species(cls, new_species):
        """Sets the species for the class."""
        cls.species = new_species

class Dog(Animal):
    pass

# Before modification
print("Before:", Dog.species)

# Using class method in subclass
Dog.set_species("Canine")

# After modification
print("After:", Dog.species)


class Circle:
    def __init__(self, radius):
        """Constructor for Circle class."""
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        """Factory method to create a Circle instance from diameter."""
        return cls(diameter / 2)

# Creating instance using factory method
c = Circle.from_diameter(10)
print("Radius:", c.radius)
