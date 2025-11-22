# use of predefined keywords in Python


num = 10

if num > 0:
    print("Positive number")  
elif num < 0:
    print("Negative number")  
else:
    print("Zero")  


for i in range(5):
    print(i)  

count = 0
while count < 3:
    print(count)  
    count += 1

for i in range(5):
    if i == 3:
        break  
    print(i)

for i in range(5):
    if i == 2:
        continue  
    print(i)

my_list = [1, 2, 3]
print("Before modification:", my_list)

my_list[0] = 10  # Modifies the first element
print("After modification:", my_list)

my_dict = {'name': 'Alice', 'age': 25}
print("Before modification:", my_dict)

my_dict['age'] = 26  # Changing value of an existing key
my_dict['city'] = 'New York'  # Adding a new key-value pair
print("After modification:", my_dict)

my_set = {1, 2, 3}
print("Before modification:", my_set)

my_set.add(4)  # Adding a new element
my_set.remove(2)  # Removing an element
print("After modification:", my_set)


my_string = "Hello"
print("Original string:", my_string)

# Trying to modify a string
# my_string[0] = 'h'  #This will cause an error

my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)

# my_tuple[0] = 10  # This will cause an error

print("\n")
# 1. Arithmetic Operators
a, b = 10, 5
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("\n")

# 2. Comparison Operators
print("Comparison Operators:")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or Equal to:", a >= b)
print("Less than or Equal to:", a <= b)
print("\n")

# 3. Logical Operators
print("Logical Operators:")
print("AND Operator:", a > 5 and b < 10)
print("OR Operator:", a > 10 or b < 10)
print("NOT Operator:", not (a > b))
print("\n")

# 4. Bitwise Operators
print("Bitwise Operators:")
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT of a:", ~a)
print("Left Shift a by 1:", a << 1)
print("Right Shift a by 1:", a >> 1)
print("\n")

# 5. Assignment Operators
print("Assignment Operators:")
c = a
print("Initial c:", c)
c += 2
print("After +=:", c)
c -= 2
print("After -=:", c)
c *= 2
print("After *=:", c)
c /= 2
print("After /=:", c)
c //= 2
print("After //=:", c)
c **= 2
print("After **=:", c)
print("\n")

# 6. Membership Operators
print("Membership Operators:")
my_list = [1, 2, 3, 4, 5]
print("Is 2 in list:", 2 in my_list)
print("Is 10 not in list:", 10 not in my_list)
print("\n")

# 7. Identity Operators
print("Identity Operators:")
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("Is x the same as y:", x is y)
print("Is x the same as z:", x is z)
print("Is x different from y:", x is not y)

print("\n")

# 1. Implicit Type Casting
# Python automatically converts smaller data types to larger ones to prevent data loss
print("Implicit Type Casting:")
int_num = 10
float_num = 10.5
result = int_num + float_num
print("Result:", result)
print("Type of result:", type(result))
print("\n")

# 2. Explicit Type Casting
# The programmer manually converts one data type into another using functions like int(), float(), str(), list(), tuple(), set()
print("Explicit Type Casting:")
num_str = "100"
num_int = int(num_str)
print("String to Integer:", num_int)
print("Type:", type(num_int))

num_float = float(num_int)
print("Integer to Float:", num_float)
print("Type:", type(num_float))

num_list = list(num_str)
print("String to List:", num_list)
print("Type:", type(num_list))

num_tuple = tuple(num_str)
print("String to Tuple:", num_tuple)
print("Type:", type(num_tuple))

num_set = set(num_str)
print("String to Set:", num_set)
print("Type:", type(num_set))

print("\n")

# 1. if Statement
print("if Statement:")
age = 18
if age >= 18:
    print("You are eligible to vote.")
print("\n")

# 2. if-else Statement
print("if-else Statement:")
n = 10
if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")
print("\n")

# 3. if-elif-else Statement
print("if-elif-else Statement:")
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")
print("\n")

# 4. Nested if Statement
print("Nested if Statement:")
num = 15
if num > 0:
    print("Positive number")
    if num % 5 == 0:
        print("Divisible by 5")
print("\n")


# 1. for Loop
print("for Loop:")
for i in range(5):
    print("Iteration:", i)
print("\n")

# 2. while Loop
print("while Loop:")
n = 5
while n > 0:
    print("Countdown:", n)
    n -= 1
print("\n")

# 3. Nested Loops
print("Nested Loops:")
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)
print("\n")

# 4. Loop Control Statements
print("Loop Control Statements:")
print("Using break:")
for i in range(5):
    if i == 3:
        break
    print(i)
print("\n")

print("Using continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)
print("\n")

print("Using pass:")
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(i)