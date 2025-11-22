#dictionaries are un-ordered collections of key, value pairs
#each key must be unique
#dictionaries are mutable

#creation of dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"} 
print(my_dict)

print(type(my_dict))  #this will print dict

#accessing value in dictionary
name = my_dict["name"] 
print(name)  # Output: Alice

age = my_dict.get("age") 
print(age)   # Output: 30

#adding or modifing value in dictionary
my_dict["occupation"] = "Engineer"  # Add a new key-value pair
my_dict["age"] = 31                  # Modify an existing value
print(my_dict)

#removing value in dictionary
del my_dict["city"]  # Remove the "city" key-value pair
city = my_dict.pop("occupation")  # Remove and return the value of "occupation"
print(my_dict)
print(city)

#iterating through a dictionary
for key in my_dict:
    print(key, ":", my_dict[key]) 

for key, value in my_dict.items():
    print(key, ":", value)

print(my_dict.values())  #it will only print the value of dictionary 
print(my_dict.keys()) #it will only print the keys of dictionary

# Creating a dictionary named 'details' with some personal information
details = {"name": "jittu", "age": 21, "phone": 21212121, "email": "jittupal@yahho.com"}

# Printing the entire dictionary
print(details)

# Accessing and printing specific values using their keys
print(details["name"])   # Prints the value associated with the key "name"
print(details["email"])  # Prints the value associated with the key "email"

# Adding new key-value pairs to the dictionary
details["address"] = "mp"   # Adding an address field
details["student"] = "yes"  # Indicating if the person is a student

# Modifying an existing value in the dictionary
details["name"] = "kittu"   # Changing the name from "jittu" to "kittu"

# Printing the updated dictionary
print(details)

# Creating another dictionary with different key types (float, boolean, complex number, and string)
new_dict = {1.2: "jittu", True: "student", 2+3j: "complex", "elgible": "yes"}

# Accessing and printing values using their respective keys
print(new_dict[1.2])    # Prints the value for key 1.2 (float)
print(new_dict[True])   # Prints the value for key True (boolean)

# The below line is commented out because it would cause an error.
# Dictionary keys must be immutable (unchangeable types like strings, numbers, or tuples),
# but sets are mutable, so they cannot be used as dictionary keys.
# new_dict = {{1, 2, 3}: "ajay"}

# Printing the dictionary
print(new_dict)

# Creating a dictionary named 'books' with three keys: "name", "book", and "date"
books = {"name":["jittu", "kittu", "mittu"], 
         "book":["myworld", "world", "star"], 
         "date":[1, 2, 3]}

# Printing all names from the "name" key
print(books["name"])  

# Printing all dates from the "date" key
print(books["date"])  

# Printing the second element from the "name" list (index 1)
print(books["name"][1])  

# Printing the second element from the "book" list (index 1)
print(books["book"][1])  

# Attempting to clear 'new_dict' (but 'new_dict' is not defined yet, which will cause an error)
new_dict.clear()  
print(new_dict)  # This will cause an error because 'new_dict' is not defined

# Deleting the "date" key from the 'books' dictionary
del books["date"]  
print(books)  

# Adding the "date" key back to 'books' with its original values
books["date"] = [1, 2, 3]  
print(books)  

# Printing the total number of keys in the dictionary
print(len(books))  

# Printing all keys of the dictionary
print(books.keys())  

# Removing the "book" key from 'books' using the pop() method
books.pop("book")  
print(books)  

# Creating a new dictionary 'd1' and updating 'books' with 'd1'
d1 = {"book":["world", "star", "moon"]}  
books.update(d1)  
print(books)  

# Creating a new dictionary 'd1' using fromkeys() with keys (1,2,3,4) and the same value ("a", "b", "c", "d") for each key
d1 = d1.fromkeys((1, 2, 3, 4), ("a", "b", "c", "d"))  
print(d1)  

# Creating two lists: 'students' and 'marks'
students = ["ajay", "jittu", "kittu"]
marks = [84, 98, 43]

# Using zip() to pair students with their respective marks and printing the pairs as tuples
for i in zip(students, marks):  
    print(i)  

# Creating an empty dictionary to store student marks
student_mark = {}  

# Populating 'student_mark' by zipping students and marks
for student, mark in zip(students, marks):  
    student_mark[student] = mark  

# Printing the final dictionary mapping students to their marks
print(student_mark)  

# Creating two lists: 'students' and 'marks'
students = ["ajay", "jittu", "kittu"]
marks = [84, 98, 43]

# Using dictionary comprehension to create a dictionary mapping students to their marks
new_student_mark = {student: mark for student, mark in zip(students, marks)}
print(new_student_mark)  # Output: {'ajay': 84, 'jittu': 98, 'kittu': 43}

# Creating user ID and user name lists
use_id = [1, 2, 4, 5]
use_name = ["abc1", "abc2", "abc3", "abc3"]

# Using dictionary comprehension to create a dictionary mapping user IDs to user names
use_date = {user_id: user_name for user_id, user_name in zip(use_id, use_name)}
print(use_date)  # Output: {1: 'abc1', 2: 'abc2', 4: 'abc3', 5: 'abc3'}

# Retrieving values using the get() method
print(use_date.get(1))  # Output: 'abc1' (User ID 1 is associated with 'abc1')
print(use_date.get(4))  # Output: 'abc3' (User ID 4 is associated with 'abc3')

# Demonstrating keys(), values(), and items() with a real-world example

# Creating a dictionary to represent a student's details
student_info = {
    "name": "John Doe",
    "age": 21,
    "grade": "A",
    "city": "New York",
    "email": "johndoe@example.com"
}

# Printing all keys in the dictionary
print(student_info.keys())  
# Output: dict_keys(['name', 'age', 'grade', 'city', 'email'])

# Printing all values in the dictionary
print(student_info.values())  
# Output: dict_values(['John Doe', 21, 'A', 'New York', 'johndoe@example.com'])

# Printing all key-value pairs in the dictionary
print(student_info.items())  
# Output: dict_items([('name', 'John Doe'), ('age', 21), ('grade', 'A'), ('city', 'New York'), ('email', 'johndoe@example.com')])

# Iterating over keys and values using items()
for key, value in student_info.items():
    print(f"{key}: {value}")

# Output:
# name: John Doe
# age: 21
# grade: A
# city: New York
# email: johndoe@example.com
# Creating a restaurant menu dictionary with dish names as keys and their prices as values
restaurant_menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "French Fries": 100,
    "Cold Drink": 50
}

# Printing all dish names (keys)
print("Menu Items:", restaurant_menu.keys())  
# Output: dict_keys(['Burger', 'Pizza', 'Pasta', 'French Fries', 'Cold Drink'])

# Printing all prices (values)
print("Prices:", restaurant_menu.values())  
# Output: dict_values([120, 250, 180, 100, 50])

# Printing all menu items with prices (key-value pairs)
print("Complete Menu:", restaurant_menu.items())  
# Output: dict_items([('Burger', 120), ('Pizza', 250), ('Pasta', 180), ('French Fries', 100), ('Cold Drink', 50)])

# Iterating through the menu and printing each dish with its price
print("\nRestaurant Menu:")
for dish, price in restaurant_menu.items():
    print(f"{dish}: ₹{price}")

# Checking the price of a specific dish using get()
dish_name = "Pizza"
print(f"\nThe price of {dish_name} is ₹{restaurant_menu.get(dish_name)}")  
# Output: The price of Pizza is ₹250

dish_name = "Ice Cream"  # A dish that is not in the menu
print(f"The price of {dish_name} is {restaurant_menu.get(dish_name, 'Not Available')}")  
# Output: The price of Ice Cream is Not Available
