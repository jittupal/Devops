import math as m  # Importing the math module and giving it an alias 'm'

# Using the ceil function to get the nearest highest integer value
print(m.ceil(7.6))  # Output: 8
print(m.ceil(9.1))  # Output: 10

# Using the floor function to get the nearest lowest integer value
print(m.floor(8.9))  # Output: 8
print(m.floor(2.1))  # Output: 2

# Defining a simple function that prints a greeting message
def greeting():
    print("welcome to the office")

greeting()  # Function call

greeting()  # Calling the function again

# Defining a function with a parameter 'name'
def greeting(name):
    print("welcome to the office", name)

greeting("ajay")   # Passing "ajay" as an argument

greeting("jittu")  # Passing "jittu" as an argument

# Defining a function that returns a string
def func():
    return "this is my first function"

print(func())  # Printing the returned value from func
print(func() + " in python")  # Concatenating and printing two strings

# Storing the return value of func in a variable
a = func()
print(a)  # Printing the stored value
print(type(a))  # Checking the data type of the return value (string)

# Defining a function that returns multiple values
def new_func():
    return "this is second", 1, 2.3, 3+4j  # Returning multiple values

# Unpacking the returned values into different variables
a, b, c, d = new_func()

print(a)  # Printing the first returned value (string)
print(b)  # Printing the second returned value (integer)
print(c)  # Printing the third returned value (float)
print(d)  # Printing the fourth returned value (complex number)


def cal():
    # Perform a simple arithmetic calculation
    calcu = 2*3 + 3*3  # (2*3) + (3*3) = 6 + 9 = 15
    return calcu  # Return the calculated result

print(cal())  # Print the result of the cal() function


def square_no(a):
    # Calculate the square of a given number
    square = a * a
    print(f"Square of {a}: is ", square)  # Print the result

square_no(4)
square_no(5)
square_no(9)


def addition(a, b):
    # Function to add two values and return the result
    return a + b

print(addition(3, 6))  # 3 + 6 = 9
print(addition(6, 6))  # 6 + 6 = 12
print(addition(4, 9))  # 4 + 9 = 13

# Adding two strings (concatenation)
new_str = addition("jittu", " pal")
print(new_str)  # Output: jittu pal

# Adding two complex numbers
new_str = addition(3+4j, 2+5j)
print(new_str)  # Output: (5+9j)

# Adding two lists (list concatenation)
new_lst = addition([1, 3, 5], [2, 4, 6])
print(new_lst)  # Output: [1, 3, 5, 2, 4, 6]

# Adding two sets is not possible with `+`, so it's commented out
# new_set = addition({1, 2, 3,4, 5}, {2, 3, 1, 5, 6, 7})
# print(new_set)

# Adding two strings using keyword arguments
new_sum = addition(b="pal", a="jittu ")
print(new_sum)  # Output: jittu pal


def sum(a=4, b=3, c=4):
    # Function with default parameters, returns the sum of three values
    print("value of:", a, b, c)
    return a + b + c

sum1 = sum()  # Uses default values (4, 3, 4) -> 4+3+4 = 11
print(sum1)


def sum(a, b, c=5):
    # Function with one default parameter
    return a + b + c

sum2 = sum(2, 3)  # 2 + 3 + 5 = 10
print(sum2)


def sum(a, c, b=3):
    # Function with default parameter in between
    return a + b + c

sum3 = sum(2, 3)  # 2 + 3 + ? (Error: missing one argument)
print(sum3)

sum3 = sum(1, 2, 3)  # 1 + 3 + 2 = 6
print(sum3)


def sum(a=5, b=5, c=5):
    # Function with all default parameters
    return a + b + c

sum4 = sum(1, 2, 4)  # 1 + 2 + 4 = 7
print(sum4)


def add_two_num():
    # Function to take two user inputs and print their sum
    #a = int(input("Enter first number:  "))
    print()
    #b = int(input("Enter Second number: "))
    #print("Sum of a and b is:  ", a + b)

add_two_num()


def add_list(a):
    # Function to filter out only integers and floats from a given list
    n = []
    for i in a:
        if type(i) == int or type(i) == float:
            n.append(i)
    return n

n = add_list([1, 2, "jitttu", "pal", 3, 3+4j, 4])
print("The list of integer is:", n)  # Output: [1, 2, 3, 4]


def add_list(a):
    # Function to extract all integers and floats from nested lists
    n = []
    for i in a:
        if type(i) == list:
            for j in i:
                if type(j) == int or type(j) == float:
                    n.append(j)
        else:
            if type(i) == int or type(i) == float:
                n.append(i)
    return n

n = add_list([1, 3, 6, "jittu", 4, "pal", [5, 0, 3, 9]])
print(n)  # Output: [1, 3, 6, 4, 5, 0, 3, 9]

# Function to calculate the sum of any number of arguments
def any_sum(*args):
    sum = 0  # Initialize sum variable
    for i in args:  # Iterate through all arguments
        sum = sum + i  # Add each argument to sum
    return sum  # Return the final sum

# Calling the function with different sets of numbers
sum_of_arguments = any_sum(3, 4, 8, 2)
print(sum_of_arguments)  # Output: 17

sum_of_arguments = any_sum(3, 4, 2)
print(sum_of_arguments)  # Output: 9

sum_of_arguments = any_sum(3, 4)
print(sum_of_arguments)  # Output: 7


# Function to filter and return only the list arguments
def return_list(*args):
    l = []  # Initialize an empty list
    for i in args:  # Iterate through all arguments
        if type(i) == list:  # Check if the argument is of type list
            l.append(i)  # Append the list to 'l'
    return l  # Return the list containing only lists

# Calling the function with mixed types of arguments
lists = return_list(2, 4, [1, 2, 4, 6], "jittu", "pal", [4, 2, 8], {3, 4, 2}, {"jittu": "pal", "kittu": "pal"}, [3, 5, 8, 9])
print(lists)  # Output: [[1, 2, 4, 6], [4, 2, 8], [3, 5, 8, 9]]


# Function to calculate the sum of elements in a list
def total_sum(a):
    sum = 0  # Initialize sum variable
    for i in a:  # Iterate through the list
        sum = sum + i  # Add each element to sum
    return sum  # Return the total sum

# Function to calculate total marks from given subject marks
def marks_in_subject(**kwargs):  # Accepts keyword arguments (subject=marks)
    def total_marks(marks_list):
        return total_sum(marks_list)  # Calls total_sum to get the sum of marks
    
    marks_list = []  # Initialize an empty list to store marks
    for sub, marks in kwargs.items():  # Iterate through subjects and marks
        marks_list.append(marks)  # Append marks to the list
    
    return total_marks(marks_list)  # Return the total marks

# Calling the function with subject marks
ans = marks_in_subject(a=10, b=40)
print(ans)  # Output: 50

ans = marks_in_subject(a=10, b=40, c=60)
print(ans)  # Output: 110
