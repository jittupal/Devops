# Definition: A decorator is a function that takes another function as an argument
# and extends its behavior without modifying the original function's structure.

# Example 1: A basic decorator that prints messages before and after the function execution.
def my_decorator(func):
    def wrapper():
        print("Before Computation:")  # This runs before the function execution
        func()  # Calling the original function
        print("After Computation:")  # This runs after the function execution
    return wrapper  # Returning the inner function

# Using the decorator with a simple function
@my_decorator
def say_hello():
    print("Hello World")

say_hello()

# Another example using the same decorator
@my_decorator
def sum_numbers():
    print("3 + 4:", 3 + 4)  # Simple arithmetic operation

sum_numbers()

# Example 2: A decorator to measure execution time of functions
import time  # Importing time module for performance measurement

def time_decorator(func):
    def timer():
        start = time.time()  # Start time before function execution
        func()  # Execute the function
        end = time.time()  # End time after function execution
        print("The time for executing the code:", end - start)  # Calculate elapsed time
    return timer

# Using the execution time decorator
@time_decorator    
def func_test():
    print("11 * 1000:", 11 * 1000)  # Multiplication operation

func_test()

# Another function using the time decorator
@time_decorator
def print_name():
    print("My name is Jittu")

print_name()

# Additional Example: Decorator to convert output to uppercase

def uppercase_decorator(func):
    def wrapper():
        result = func()  # Call the function
        return result.upper()  # Convert result to uppercase
    return wrapper

@uppercase_decorator
def greet():
    return "Hello, welcome to decorators!"

print(greet())  # Output will be in uppercase

"""
Definition:
A decorator in Python is a design pattern that allows the modification of a function or class method's behavior without changing its structure. 
Decorators wrap a function, execute code before and after it, and return the modified function.
"""

# Class Decorator Example
class Class_decorator:
    """
    A class-based decorator that wraps a function call and adds additional behavior
    before and after the function execution.
    """
    def __init__(self, func):
        self.func = func
    
    def __call__(self):
        print("Something is happening before function execution")
        self.func()
        print("Something is happening after function execution")

# Applying class decorator
@Class_decorator
def say_hello():
    print("Hello World")

say_hello()

# Another variation of Class Decorator
class Class_decorator:
    """
    Another example of a class decorator without a function reference,
    used to modify behavior when an instance is called.
    """
    def __init__(self):
        print("Inside Init Method")
    
    def __call__(self):
        print("Something is happening before function execution")
        print("Something is happening after function execution")

# Creating an instance and calling it like a function
obj1 = Class_decorator()
obj1()

# Built-in Decorators
class Math:
    """
    Example of using the @classmethod decorator
    """
    @classmethod
    def add(cls, x, y):
        print(cls.__name__, "sum:", x + y)

Math.add(3, 4)

class Math:
    """
    Example of using the @staticmethod decorator
    """
    @staticmethod
    def add(x, y):
        print("Sum:", x + y)

Math.add(3, 4)

# Additional Examples of Built-in Decorators
class Circle:
    """
    Example of @property decorator, used for defining getters in a Pythonic way.
    """
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

c = Circle(5)
print("Radius:", c.radius)  # Calls the getter
c.radius = 10  # Calls the setter
print("Updated Radius:", c.radius)
