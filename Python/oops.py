# Class definition for Car
class Car:
    # Method to simulate acceleration
    def accelerate(self):
        print("Car is speeding")  # Prints a message when the car accelerates

    # Method to simulate braking (note: corrected spelling from "brak" to "brake")
    def brake(self):
        print("Car is stopped")  # Prints a message when the car stops

# Creating an object (instance) of the Car class
c1 = Car()
c1.accelerate()  # Calls the accelerate method for c1

# Creating another instance of the Car class
c2 = Car()
c2.accelerate()  # Calls the accelerate method for c2

# Creating a third instance of the Car class
c3 = Car()
c3.accelerate()  # Calls the accelerate method for c3
c3.brake()  # Calls the brake method for c3

# Define a class named 'Bank'
class Bank:
    # Class attribute 'amount' which represents the initial balance of the bank account
    amount = 10000  

    # Method to deposit money into the account
    def deposit(self, amount_dep):
        print(f"I am depositing {amount_dep} money")  # Print deposit message
        self.amount = self.amount + amount_dep  # Add the deposited amount to the total balance

    # Method to withdraw money from the account
    def withdraw(self, amount_withdraw):
        self.amount = self.amount - amount_withdraw  # Subtract the withdrawn amount from the total balance
        print(f"I am withdrawing {amount_withdraw} money")  # Print withdrawal message

    # Method to check the remaining balance
    def remain(self):
        print(f"Available balance is {self.amount} money")  # Print the available balance

# Create an object (instance) of the 'Bank' class
b = Bank()

# Deposit 2000 into the bank account
b.deposit(2000)  # New balance = 10000 + 2000 = 12000
b.remain()  # Prints: Available balance is 12000 money

# Withdraw 2000 from the bank account
b.withdraw(2000)  # New balance = 12000 - 2000 = 10000
b.remain()  # Prints: Available balance is 10000 money

# Deposit 5000 into the bank account
b.deposit(5000)  # New balance = 10000 + 5000 = 15000

# Withdraw 3000 from the bank account
b.withdraw(3000)  # New balance = 15000 - 3000 = 12000

# Check remaining balance
b.remain()  # Prints: Available balance is 12000 money


# Class to perform operations on a list
class Listops:
    def __init__(self, l):
        # Initialize the class with a list
        self.l = l

    # Method to extract even numbers from a given list
    def extract_eve(self, l):
        l1 = []  # Create an empty list to store even numbers
        for i in l:  # Loop through each element in the list
            if i % 2 == 0:  # Check if the number is even
                l1.append(i)  # Add even number to the list
        return l1  # Return the list of even numbers

    # Method to extract odd numbers from a given list
    def extract_odd(self, l):
        l2 = []  # Create an empty list to store odd numbers
        for i in l:  # Loop through each element in the list
            if i % 2 != 0:  # Check if the number is odd
                l2.append(i)  # Add odd number to the list
        return l2  # Return the list of odd numbers

# Creating an object of Listops with a given list
ops = Listops([2, 3, 4, 5, 6, 7, 8, 9])

# Printing the original list
print("Original list:", ops.l)

# Extracting and printing even numbers from the list
print("Even numbers:", ops.extract_eve(ops.l))

# Extracting and printing odd numbers from the list
print("Odd numbers:", ops.extract_odd(ops.l))

# Extracting even numbers from another list
print("Even numbers from [2, 6, 9, 4, 1]:", ops.extract_eve([2, 6, 9, 4, 1]))

# Extracting even numbers from another list (incorrect function used, should be extract_odd)
print("Odd numbers from [5, 7, 9, 3, 1]:", ops.extract_odd([5, 7, 9, 3, 1]))  # Fixed function call

# Creating another object with a different list
ops1 = Listops([2, 3, 6, 7, 9, 9, 5])

# Printing the original list
print("Original list:", ops1.l)

# Extracting and printing even numbers from the new list
print("Even numbers:", ops1.extract_eve(ops1.l))

# Extracting and printing odd numbers from the new list
print("Odd numbers:", ops1.extract_odd(ops1.l))

# Defining a class Book to represent book details dynamically
class Book:
    def __init__(self, name, author, title):
        # Initializing attributes with dynamic values passed during object creation
        self.name_of_book = name  # Storing book name
        self.book_author = author  # Storing author name
        self.title_name = title  # Storing book title

    # Method to print book name and title
    def extract_name_and_details(self):
        print(self.name_of_book, self.title_name)

    # Method to print book name and author
    def extract_name_and_author(self):
        print(self.name_of_book, self.book_author)

# Creating an object of the Book class with specific book details
student1 = Book("ML", "Murphy", "Linear_regression")
student1.extract_name_and_details()  # Output: ML Linear_regression
student1.extract_name_and_author()   # Output: ML Murphy

# Creating another object of the Book class with different book details
student2 = Book("stats", "joss", "descriptive_stats")
student2.extract_name_and_author()   # Output: stats joss
student2.extract_name_and_details()  # Output: stats descriptive_stats
