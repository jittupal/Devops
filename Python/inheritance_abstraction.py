# Inheritance in Python

## Definition
#Inheritance is an object-oriented programming (OOP) concept where a class (child class) derives properties and behaviors from another class (parent class). It helps in code reusability and establishing a relationship between different classes.

# Single Inheritance Example 1
## Definition
#Single inheritance is a type of inheritance where a child class inherits from only one parent class. This allows the child class to reuse the properties and methods of the parent class.

### Example 1: Parent and Child Relationship
# Parent class
class Father:
    def father_property(self):
        print("This is father's property")

# Child class inheriting from Father
class Son(Father):
    def job(self):
        print("Son has property from job")

# Creating an instance of the Son class
child_obj = Son()

# Calling methods from both child and parent classes
child_obj.job()  # Calls the method defined in Son class
child_obj.father_property()  # Calls the inherited method from Father class

# Creating an instance of the Father class
father_obj = Father()
father_obj.father_property()  # Father can only access its own methods

print("\n")  # Just for separating outputs

# Single Inheritance Example 2
## Definition
#This example demonstrates single inheritance where a child class inherits properties from a parent class representing fruits.

### Example 2: Fruit and Apple Relationship
# Parent class
class Fruit:
    def fruit_info(self):
        print("It is a parent class representing general fruits")

# Child class inheriting from Fruit
class Apple(Fruit):
    def apple_info(self):
        print("It is a child class representing a specific type of fruit: Apple")

# Creating an instance of Apple class
obj = Apple()

# Calling methods from both child and parent classes
obj.apple_info()  # Calls the method from Apple class
obj.fruit_info()  # Calls the inherited method from Fruit class


# Method Overriding Example in Python

# Parent class
class Fruit:
    # Method in parent class
    def fruit_info(self):
        print("Inside Parent Class")

# Child class inheriting from Fruit
class Apple(Fruit):
    # Overriding the fruit_info method from the parent class
    def fruit_info(self):
        # Calling the parent class method using super()
        super().fruit_info()
        print("Inside Child Class of Fruit Info")
    
    # Additional method specific to Apple class
    def apple_info(self):
        print("Inside Child Class - Apple Specific Info")

# Creating an object of Apple class
objs = Apple()
objs.fruit_info()  # Calls overridden method

# Example 2: Another subclass demonstrating method overriding
class Mango(Fruit):
    def fruit_info(self):
        super().fruit_info()
        print("Inside Mango Class - Fruit Info")

    def mango_info(self):
        print("Mango is known as the king of fruits.")

# Creating an object of Mango class
mango_obj = Mango()
mango_obj.fruit_info()  # Calls overridden method
mango_obj.mango_info()  # Calls class-specific method


# Multilevel Inheritance Example

# Base class (GrandFather)
class GrandFather:
    """
    This class represents the GrandFather level in the inheritance hierarchy.
    It has a method to display GrandFather's property.
    """
    def prop_grandfather(self):
        print("This is Grandfather's property")

# Intermediate class (Father) inheriting from GrandFather
class Father(GrandFather):
    """
    This class represents the Father level in the inheritance hierarchy.
    It inherits from GrandFather and adds its own property method.
    """
    def prop_father(self):
        print("This is Father's property. It includes both Father and Grandfather's property")

# Derived class (Son) inheriting from Father
class Son(Father):
    """
    This class represents the Son level in the inheritance hierarchy.
    It inherits from Father (which already inherits from GrandFather),
    thus gaining access to all ancestor properties.
    """
    def prop_son(self):
        print("This is Son's property. It includes Son, Father, and Grandfather's property")

# Creating an instance of Son and accessing properties
son = Son()
son.prop_father()      # Accessing Father's property
son.prop_grandfather() # Accessing GrandFather's property
son.prop_son()         # Accessing Son's property

print("\n--- Father Instance ---")
# Creating an instance of Father and accessing properties
fath = Father()
fath.prop_father()      # Accessing Father's property
fath.prop_grandfather() # Accessing GrandFather's property

print("\n--- GrandFather Instance ---")
# Creating an instance of GrandFather and accessing properties
graf = GrandFather()
graf.prop_grandfather() # Accessing GrandFather's property

# Another Example: Multilevel Inheritance in Vehicles

# Base class (Vehicle)
class Vehicle:
    """
    This class represents a general vehicle.
    """
    def vehicle_info(self):
        print("Inside Vehicle class")

# Intermediate class (Car) inheriting from Vehicle
class Car(Vehicle):
    """
    This class represents a Car, which is a type of Vehicle.
    It inherits from Vehicle and adds its own method.
    """
    def car_info(self):
        print("Inside Car class")

# Derived class (SportsCar) inheriting from Car
class SportsCar(Car):
    """
    This class represents a SportsCar, which is a specific type of Car.
    It inherits from Car (which inherits from Vehicle),
    thus gaining access to all ancestor methods.
    """
    def sports_car_info(self):
        print("Inside SportsCar class")

# Creating an instance of SportsCar and accessing methods
print("\n--- SportsCar Instance ---")
s1 = SportsCar()
s1.car_info()        # Accessing Car class method
s1.sports_car_info() # Accessing SportsCar class method
s1.vehicle_info()    # Accessing Vehicle class method

#multiple inheritance
# Multiple Inheritance in Python
# Definition: Multiple inheritance is a feature where a class can inherit 
# attributes and methods from more than one parent class.

# Example 1: Basic Multiple Inheritance

# Parent Class 1
class Parent1:
    """This is the first parent class with a method."""
    def method1(self):
        print("Method from Parent1")

# Parent Class 2
class Parent2:
    """This is the second parent class with a method."""
    def method2(self):
        print("Method from Parent2")

# Child Class inheriting from both Parent1 and Parent2
class Child(Parent1, Parent2):
    """This child class inherits from both Parent1 and Parent2."""
    def method3(self):
        print("Method from Child")

# Creating an object of Child class
obj = Child()

# Calling methods from both parent classes and child class
obj.method1()  # Inherited from Parent1
obj.method2()  # Inherited from Parent2
obj.method3()  # Defined in Child class

print("\n")

# Example 2: Using super() with Multiple Inheritance

# Parent Class 1
class Animal:
    """This class represents animals with a sound method."""
    def sound(self):
        print("Animals make sounds")

# Parent Class 2
class Bird:
    """This class represents birds with a fly method."""
    def fly(self):
        print("Birds can fly")

# Child Class inheriting from both Animal and Bird
class Bat(Animal, Bird):
    """This child class inherits from both Animal and Bird."""
    def info(self):
        print("Bats are mammals but can fly")

# Creating an object of Bat class
bat = Bat()
bat.sound()  # Inherited from Animal
bat.fly()    # Inherited from Bird
bat.info()   # Defined in Bat class

print("\n")

# Example 3: Handling Name Conflicts in Multiple Inheritance

# Parent Class 1
class ClassA:
    """This is the first parent class with a show method."""
    def show(self):
        print("ClassA method")

# Parent Class 2
class ClassB:
    """This is the second parent class with a show method."""
    def show(self):
        print("ClassB method")

# Child Class inheriting from both ClassA and ClassB
class ClassC(ClassA, ClassB):
    """This child class inherits from both ClassA and ClassB."""
    pass

# Creating an object of ClassC
obj = ClassC()
obj.show()  # Resolves based on the Method Resolution Order (MRO)

print("\n")

# Example 4: Using super() in Multiple Inheritance to Call Methods

# Parent Class 1
class Parent1:
    """First parent class using super()."""
    def show(self):
        print("Parent1 method")
        super().show()  # Calls next method as per MRO

# Parent Class 2
class Parent2:
    """Second parent class with a show method."""
    def show(self):
        print("Parent2 method")

# Child Class inheriting from both Parent1 and Parent2
class Child(Parent1, Parent2):
    """This child class inherits from both Parent1 and Parent2."""
    def show(self):
        print("Child method")
        super().show()  # Calls Parent1's method

# Creating an object of Child class
obj = Child()
obj.show()

# Hierarchical Inheritance Example

# Definition:
# Hierarchical inheritance is a type of inheritance where multiple child classes inherit from a single parent class.
# In this case, `Car` and `Truck` are both inheriting from the `Vehicle` class.

# Base class (Parent class)
class Vehicle:
    def info(self):
        print("This is a vehicle")

# Derived class (Child class 1)
class Car(Vehicle):
    def car_info(self, name):
        print("This is car info:", name)

# Derived class (Child class 2)
class Truck(Vehicle):
    def truck_info(self, name):
        print("This is truck info:", name)

# Example 1: Creating an object of Car class
c1 = Car()
c1.info()  # Calling method from parent class
c1.car_info("BMW")  # Calling method from child class

# Example 2: Creating an object of Truck class
t1 = Truck()
t1.info()  # Calling method from parent class
t1.truck_info("TATA")  # Calling method from child class

# Additional Example: Another derived class inheriting from Vehicle
class Bike(Vehicle):
    def bike_info(self, name):
        print("This is bike info:", name)

# Example 3: Creating an object of Bike class
b1 = Bike()
b1.info()  # Calling method from parent class
b1.bike_info("Yamaha")  # Calling method from child class

# Hybrid Inheritance in Python
# Hybrid inheritance is a combination of two or more types of inheritance.
# It helps in reusing code but can introduce complexity due to multiple inheritance.

# Base class
class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle Class")

# Derived class inheriting from Vehicle (Single Inheritance)
class Car(Vehicle):
    def car_info(self):
        print("Inside Car Class")

# Another derived class inheriting from Vehicle (Single Inheritance)
class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck Class")

# Hybrid Inheritance:
# Sports_car inherits from Car (which already inherits from Vehicle)
# This creates a Hybrid Inheritance scenario where Vehicle is an indirect parent of Sports_car.
class Sports_car(Car):
    def sports_car_info(self):
        print("Inside Sports Car Class")

# Creating an object of Sports_car
obj1 = Sports_car()

# Calling methods
obj1.car_info()        # Calls method from Car class
obj1.vehicle_info()    # Calls method from Vehicle class (inherited by Car)
obj1.sports_car_info() # Calls method from Sports_car class

# Additional Example

# Another class that inherits from both Car and Truck (Multiple Inheritance)
class MultiPurposeVehicle(Car, Truck):
    def mpv_info(self):
        print("Inside Multi-Purpose Vehicle Class")

# Creating an object of MultiPurposeVehicle
obj2 = MultiPurposeVehicle()

# Calling methods from all parent classes
obj2.mpv_info()        # Calls method from MultiPurposeVehicle class
obj2.car_info()        # Calls method from Car class
obj2.truck_info()      # Calls method from Truck class
obj2.vehicle_info()    # Calls method from Vehicle class (inherited by Car and Truck)


# Abstraction in Python
# Abstraction is a concept in object-oriented programming that hides the implementation details 
# and only shows the necessary functionality. It is achieved using abstract classes and methods.

import abc  # Importing the abc module to work with abstract classes

# Creating an Abstract Class
class Rgpv:
    @abc.abstractmethod  # Declaring an abstract method
    def student_details(self):
        pass

    @abc.abstractmethod
    def student_assignments(self):
        pass

    @abc.abstractmethod
    def student_marks(self):
        pass

# Concrete Class that Implements the Abstract Class
class Jittu(Rgpv):
    def student_details(self):
        print("Student Name: Jittu Pal")
    
    def student_assignments(self):
        print("Assignments: Submitted on time")

    def student_marks(self):
        print("Marks: Jittu got 89%")

# Another Concrete Class Implementing the Abstract Class
class Friend(Rgpv):
    def student_details(self):
        print("Student Name: Ajay")
    
    def student_assignments(self):
        print("Assignments: Not submitted")
    
    def student_marks(self):
        print("Marks: He got 88%")

# Creating objects and calling methods
j = Jittu()
j.student_details()
j.student_assignments()
j.student_marks()

f = Friend()
f.student_details()
f.student_assignments()
f.student_marks()

# Another example of Abstraction using Shapes
class Shape:
    @abc.abstractmethod  # Abstract method for calculating area
    def calculate_area(self):
        pass

# Rectangle class implementing the abstract method
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def calculate_area(self):
        print(f"Area of Rectangle: {self.length * self.breadth}")

# Circle class implementing the abstract method
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        print(f"Area of Circle: {3.14 * self.radius ** 2}")

# Triangle class as an additional example
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        print(f"Area of Triangle: {0.5 * self.base * self.height}")

# Creating objects and calling methods
rect = Rectangle(10, 5)
rect.calculate_area()

c = Circle(7)
c.calculate_area()

tri = Triangle(6, 4)
tri.calculate_area()
