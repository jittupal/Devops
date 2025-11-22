# Iterators are used to get the values of an iterable one by one.
# They allow traversing through the elements without using indexing.
# An iterable is any object that can return its elements one at a time.
# Examples of iterables: strings, lists, tuples, sets, dictionaries.

# Example 1: Using a for loop to iterate over a string (iterable)
s = "jittupal"
for i in s:  
    print(i)  # Prints each character of the string one by one

print("\nUsing iter() and next() function:")

# Example 2: Using iter() and next() function on a string
a = iter(s)  # Creating an iterator from the string
print(next(a))  # Prints 'j'
print(next(a))  # Prints 'i'
print(next(a))  # Prints 't'
print(next(a))  # Prints 't'

# Example 3: Using iter() on a tuple
t = iter((1, 2, 3, 4, 5))  # Creating an iterator from a tuple
print(next(t))  # Prints 1
print(next(t))  # Prints 2
print(next(t))  # Prints 3

# Example 4: Using iter() on a set
# Note: Sets are unordered, so the output order may vary.
ss = iter({1, 4, 6, 8, 9, 0})  
print(next(ss))  # Prints a random value from the set
print(next(ss))  # Prints another random value
print(next(ss))  # Prints another random value

# Example 5: Using iter() on a dictionary
# Iterating over a dictionary returns keys by default.
d = iter({"jittu": "pal", "kittu": "pal"})  
print(next(d))  # Prints the first key (e.g., "jittu")
print(next(d))  # Prints the second key (e.g., "kittu")

# Function to square each number in a list
def square_number(n):
    result = []  # Create an empty list to store results
    for i in n:  # Iterate through the given list
        result.append(i ** 2)  # Square each number and add to the result list
    return result  # Return the list of squared numbers

answer = square_number([8, 9, 3, 5, 7])
print(answer)  # Output: [64, 81, 9, 25, 49]

# Function to generate a list of squares from 0 to n-1
def square_number(n):
    result = []  # Create an empty list
    for i in range(n):  # Loop through numbers from 0 to n-1
        result.append(i ** 2)  # Square each number and add to the list
    return result  # Return the list of squares

answer = square_number(8)
print(answer)  # Output: [0, 1, 4, 9, 16, 25, 36, 49]

# Generator function to yield squares one by one (saves memory)
def square_number_generators(n):
    for i in range(n):
        yield i ** 2  # Yielding instead of returning, creates a generator

square = square_number_generators(13)  # Create generator object
print(next(square))  # Output: 0 (First square)
print(next(square))  # Output: 1 (Second square)
print(next(square))  # Output: 4
print(next(square))  # Output: 9
print(next(square))  # Output: 16

# Generator function for Fibonacci series
def fibo(n):
    a, b = 0, 1  # Initialize first two numbers
    for i in range(n):
        yield a  # Yield the current number
        a, b = b, a + b  # Update values for the next iteration

fib = fibo(7)  # Create Fibonacci generator
print(next(fib))  # Output: 0 (First Fibonacci number)
print(next(fib))  # Output: 1
print(next(fib))  # Output: 1
print(next(fib))  # Output: 2
print(next(fib))  # Output: 3
print(next(fib))  # Output: 5
print(next(fib))  # Output: 8
