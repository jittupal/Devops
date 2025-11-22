# Lambda Function: A short, anonymous function that can have multiple arguments but only one expression.

# Lambda function to calculate the square of a number
square_lambda = lambda x: x**2  # Takes 'x' as input and returns x squared

# Calling the square_lambda function with different values
ans = square_lambda(5)  
print(ans)  # Output: 25

ans = square_lambda(6)  
print(ans)  # Output: 36

ans = square_lambda(9)  
print(ans)  # Output: 81

# Lambda function to add two numbers
add = lambda a, b: a + b  # Takes 'a' and 'b' as inputs and returns their sum

# Calling the add function with different values
ans = add(3, 5)  
print(ans)  # Output: 8

ans = add(8, 5)  
print(ans)  # Output: 13

ans = add(8, 8)  
print(ans)  # Output: 16

# Lambda function to check if a number is even
even = lambda x: x % 2 == 0  # Returns True if 'x' is even, otherwise False

# Checking if the given numbers are even
ans = even(7)  
print(ans)  # Output: False (7 is odd)

ans = even(4)  
print(ans)  # Output: True (4 is even)

ans = even(9)  
print(ans)  # Output: False (9 is odd)

# A list of strings
lists = ["jittu", "pal", "cs", "final-year"]

# Sorting the list alphabetically
x = sorted(lists)
print(x)  # Output: ['cs', 'final-year', 'jittu', 'pal']

# Sorting the list based on the length of each element
sorted_by_length = sorted(x, key=lambda x: len(x))
print(sorted_by_length)  # Output: ['cs', 'pal', 'jittu', 'final-year']

# Another example: sorting names based on length
names = ['a', 'bc', 'b', 'der', 'ki', 'kamo', 'kii']

# Sorting the list of names based on their length
y = sorted(names, key=lambda name: len(name))
print(y)  # Output: ['a', 'b', 'bc', 'ki', 'der', 'kii', 'kamo']

# Lambda function to calculate Fibonacci series
fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)

# Generating the first 10 Fibonacci numbers using list comprehension
ans = [fib(i) for i in range(10)]
print(ans)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Function to calculate factorial using recursion
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))  # Output: 120 (5! = 5*4*3*2*1)

# Lambda function to calculate factorial
fact_num = lambda x: 1 if x == 0 else x * fact_num(x-1)
print(fact_num(7))  # Output: 5040 (7! = 7*6*5*4*3*2*1)

# Using map function to apply a function to each element of a list

# Function to calculate square
def sq(x):
    return x ** 2

l = [1, 2, 3, 4, 5, 6]

# Applying square function to each element in the list
square_list = list(map(sq, l))
print(square_list)  # Output: [1, 4, 9, 16, 25, 36]

# Function to add 10 to each element
def add(x):
    return x + 10

add_list = list(map(add, l))
print(add_list)  # Output: [11, 12, 13, 14, 15, 16]

# Function to multiply each element by 2
def mul(x):
    return x * 2

mul_list = list(map(mul, l))
print(mul_list)  # Output: [2, 4, 6, 8, 10, 12]


# Using lambda with map  
# map() applies a function to all items in an iterable (list, tuple, etc.)

l = [1, 2, 3, 4, 5]  # Sample list

# Squaring each element in the list
squ = list(map(lambda x: x**2, l))
print(squ)  # Output: [1, 4, 9, 16, 25]

# Adding 10 to each element in the list
add_lists = list(map(lambda x: x + 10, l))
print(add_lists)  # Output: [11, 12, 13, 14, 15]

# Multiplying each element by 10
mul_lists = list(map(lambda x: x * 10, l))
print(mul_lists)  # Output: [10, 20, 30, 40, 50]

# Adding corresponding elements of two lists
l1 = [10, 12, 14, 16, 18]
l2 = [20, 22, 24, 26, 28]
add_lists_num = list(map(lambda x, y: x + y, l1, l2))
print(add_lists_num)  # Output: [30, 34, 38, 42, 46]

# Converting each character of a string to uppercase
s = "jittupal"
upper_case = list(map(lambda x: x.upper(), s))
print(upper_case)  # Output: ['J', 'I', 'T', 'T', 'U', 'P', 'A', 'L']

# Capitalizing each word in a list
words = ["jittu", "python", "notnow"]
capi = list(map(str.capitalize, words))
print(capi)  # Output: ['Jittu', 'Python', 'Notnow']

# Converting grades to numerical values
grades = ["A", "B", "C", "D"]
ans = list(map(lambda grade: 4 if grade == "A" else (3 if grade == "B" else 2), grades))
print(ans)  # Output: [4, 3, 2, 2]


# Importing reduce function from functools module
from functools import reduce  

# Example 1: Sum of all elements in a list  
a = [2, 4, 6, 8, 9, 3]
answer = reduce(lambda x, y: x + y, a)  # Adds elements one by one
print(answer)  # Output: 32 (2+4+6+8+9+3)

# Example 2: Multiplication of all elements in a list  
answer = reduce(lambda x, y: x * y, a)  # Multiplies elements one by one
print(answer)  # Output: 10368 (2*4*6*8*9*3)

# Example 3: Concatenation of strings in a list  
strings = ["Data", "Science", "Course"]
answ = reduce(lambda x, y: x + " " + y, strings)  # Joins words with space
print(answ)  # Output: "Data Science Course"

# Example 4: Finding the maximum number in a list  
numbers = [1, 3, 5, 7, 99999, 100, 9, 3, 10000]
sol = reduce(lambda x, y: x if x > y else y, numbers)  # Keeps the larger value
print(sol)  # Output: 99999 (largest number in the list)

# Example 5: Calculating factorial of a number using reduce  
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))  # Multiplies all numbers from 1 to n

# Factorial of 5 (5! = 5*4*3*2*1)
anss = factorial(5)
print(anss)  # Output: 120

# Factorial of 9 (9! = 9*8*7*6*5*4*3*2*1)
anss = factorial(9)
print(anss)  # Output: 362880

# The `filter` function in Python is used to filter elements from an iterable based on a condition.
# It takes two arguments: a function and an iterable.
# The function should return True for elements that should be included in the result.

c = [2, 3, 5, 6, 8, 9, 1]

# Filtering even numbers from the list
even_no = list(filter(lambda x: x % 2 == 0, c))  
print(even_no)  # Output: [2, 6, 8]

# Filtering odd numbers from the list
odd_no = list(filter(lambda x: x % 2 != 0, c))  
print(odd_no)  # Output: [3, 5, 9, 1]

c1 = [-2, -1, 9, -3, -4, 6, 8]

# Filtering negative numbers from the list
neg_no = list(filter(lambda x: x < 0, c1))  
print(neg_no)  # Output: [-2, -1, -3, -4]

# Filtering positive numbers from the list
pos_no = list(filter(lambda x: x > 0, c1))  
print(pos_no)  # Output: [9, 6, 8]

s1 = ["jittu", "pal", "mittu", "neha", "sneha", "devkinandan"]

# Filtering strings with length greater than 4
gre_4 = list(filter(lambda x: len(x) > 4, s1))  
print(gre_4)  # Output: ['jittu', 'mittu', 'sneha', 'devkinandan']

# Using a normal function instead of a lambda function
def check_even(num):
    if num % 2 == 0:  # Checking if the number is even
        return True
    return False

num = [2, 3, 6, 4, 7, 9, 1, 8]

# Filtering even numbers using the defined function
check = list(filter(check_even, num))  
print(check)  # Output: [2, 6, 4, 8]


words = ["apple", "banana", "grape", "mango", "kiwi"]

# Filtering words that contain the letter 'a'
words_with_a = list(filter(lambda x: 'a' in x, words))
print(words_with_a)  # Output: ['apple', 'banana', 'grape', 'mango']

numbers = [10, 25, 30, 45, 50, 60]

# Filtering numbers that are divisible by 5
div_by_5 = list(filter(lambda x: x % 5 == 0, numbers))
print(div_by_5)  # Output: [10, 25, 30, 45, 50, 60]
