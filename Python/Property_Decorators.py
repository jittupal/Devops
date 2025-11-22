# Property Decorators
# Property decorators in Python allow us to define methods that can be accessed like attributes.
# The `@property` decorator is used to define a getter method, and `@<property_name>.setter` is used to define a setter.

class Student:
    """
    This class represents a student with a name and branch.
    The @property decorator is used to access student details without calling it explicitly as a method.
    """
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    @property
    def access(self):
        """Getter method to display student details."""
        print("Name:", self.name)
        print("Branch:", self.branch)

# Creating an instance of Student class
stud = Student("Jittu", "CS")
stud.access  # Accessing the property like an attribute


class Radius:
    def __init__(self, radius):
        self._radius = radius  # Using _radius to avoid recursion issues

    @property
    def show(self):
        """Getter method to display the radius."""
        print("Radius:", self._radius)

    @show.setter
    def show(self, value):
        """Setter method to modify the radius."""
        if value >= 0:
            self._radius = value
        else:
            print("Radius cannot be negative!")

    def area(self):
        """Method to calculate and display the area of the circle."""
        print("Area:", 3.14 * self._radius * self._radius)

# Creating an instance of Radius class
rad = Radius(7)
rad.show  # Accessing the radius
rad.show = 10  # Modifying the radius
rad.show  # Accessing the modified radius
rad.area()  # Calculating area


# Additional Example: Using Property Decorators for Employee Salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Using _salary to avoid recursion issues

    @property
    def salary(self):
        """Getter method for salary."""
        return self._salary

    @salary.setter
    def salary(self, value):
        """Setter method to update salary with validation."""
        if value >= 0:
            self._salary = value
        else:
            print("Salary cannot be negative!")

# Creating an instance of Employee class
emp = Employee("Alice", 50000)
print("Initial Salary:", emp.salary)  # Accessing salary using property
emp.salary = 60000  # Updating salary
print("Updated Salary:", emp.salary)  # Accessing updated salary
emp.salary = -10000  # Trying to set a negative salary (Invalid)
