# Dunder (Magic) Methods in Python
# ----------------------------------
# Dunder (double underscore) methods are special methods in Python
# that allow us to customize object behavior. They start and end with '__'.

# Example 1: __add__ method (Overloading the '+' operator)
# This method defines how an object should behave when added to another.
a = "jittu"
b = " pal"
print(a.__add__(b))  # Equivalent to: print(a + b)

# __add__ also works for integers
c = 4
d = 7
print(c.__add__(d))  # Equivalent to: print(c + d)

# Example 2: __init__ method (Constructor)
# This method is called automatically when a new object is created.
class Student:
    def __init__(self, name):
        print(name, "This is the first thing that will execute when an object is created.")

# Creating instances (objects) of the Student class
obj1 = Student("Ajay")
obj2 = Student("Bijay")

# Example 3: __new__ method (Executed before __init__)
# This method is responsible for object creation before initialization.
class Car:
    def __new__(cls):
        print("This will be executed even before __init__")
        return super().__new__(cls)  # Required to allow object creation
    
    def __init__(self):
        print("This will be executed after __new__")

# Creating an instance of the Car class
obj3 = Car()

# Example 4: __str__ method (Custom String Representation)
# This method defines what should be returned when calling str() on an object.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

book1 = Book("Python Programming", "John Doe")
print(book1)  # Calls __str__() method

# Example 5: __len__ method (Custom Length Calculation)
# This method defines what should be returned when calling len() on an object.
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

my_playlist = Playlist(["Song1", "Song2", "Song3"])
print(len(my_playlist))  # Calls __len__() method

# Example 6: __eq__ method (Custom Equality Check)
# This method defines how two objects should be compared using '=='.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age  # Two persons are equal if their ages match

p1 = Person("Alice", 25)
p2 = Person("Bob", 25)
p3 = Person("Charlie", 30)

print(p1 == p2)  # True, because ages are the same
print(p1 == p3)  # False, because ages are different

# Example 7: __getitem__ method (Indexing Support)
# This method allows objects to be accessed using square brackets [].
class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

cart = ShoppingCart(["Apple", "Banana", "Cherry"])
print(cart[0])  # Returns "Apple"
print(cart[1])  # Returns "Banana"
