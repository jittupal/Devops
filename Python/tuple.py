#tuples are immutable, it can not be change or modified after creation
#tuple is used to protect the data which we not want to change later
#tuple can also store multiple data types in it
#accessing of elements works same like list

new = (2, 3) 
print(type(new)) #it will print tuple

new_list = (2, 3.3, "jittu", (3+4j), False)
print(type(new_list)) #the type is list

print(new_list[3]) #it will print 3+4j
print(new_list[-3]) #it will print jittu

# new_list[4] = True #it will give error because we can't change tuples values

#mutiple tuples can be stored in a single tuple
box1 = ("a", "b")
box2 = ("c", "d")
cho_bag = (box1, box2)

print(cho_bag)

#accessing a item of tuple in a tuple
print(cho_bag[1][1]) #it will print d
print(cho_bag[0][0]) #it will print a

for box in cho_bag:    #it will access the box one by one
    for choc in box:    #it will access the element of box one by one
        print(choc)      

# Creating a tuple named tuple1 with repeated elements
tuple1 = ("jittu", "jittu", 1, 2, 3, 3, 3, 4, "jittu")

# Counting occurrences of the number 3 in the tuple
print(tuple1.count(3))  # Output: 3 (since 3 appears three times)

# Counting occurrences of the string "jittu" in the tuple
print(tuple1.count("jittu"))  # Output: 3 (since "jittu" appears three times)

# Finding the index of the first occurrence of the number 3
print(tuple1.index(3))  # Output: 4 (zero-based index, so the first 3 appears at position 4)

# Finding the index of the first occurrence of the string "jittu"
print(tuple1.index("jittu"))  # Output: 0 (the first occurrence is at index 0)

# Slicing the tuple from index 3 to 6 (excluding 6)
print(tuple1[3:6])  # Output: (2, 3, 3) (extracts elements at indices 3, 4, and 5)

# Reversing the tuple using slicing
print(tuple1[::-1])  # Output: ('jittu', 4, 3, 3, 3, 2, 1, 'jittu', 'jittu') (full tuple reversed)

# 1️⃣ Finding the Maximum and Minimum in a Tuple
numbers = (10, 50, 30, 80, 20, 90, 70)  # Tuple containing numbers

# Finding the maximum value in the tuple
max_value = max(numbers)  
# Finding the minimum value in the tuple
min_value = min(numbers)

# Printing the maximum value and its index
print("Maximum value is:", max_value, "at index", numbers.index(max_value))  
# Printing the minimum value and its index
print("Minimum value is:", min_value, "at index", numbers.index(min_value))  
print("-" * 50)  # Separator for better readability

# 2️⃣ Tuple Nesting (Tuple inside a Tuple)
tuple1 = (1, 2, 3)  # First tuple
tuple2 = ("a", "b", "c")  # Second tuple

# Creating a nested tuple that contains tuple1 and tuple2
nested_tuple = (tuple1, tuple2)

# Printing the nested tuple
print("Nested Tuple:", nested_tuple)  
# Accessing and printing the first tuple inside nested_tuple
print("First tuple:", nested_tuple[0])  
# Accessing and printing the second tuple inside nested_tuple
print("Second tuple:", nested_tuple[1])  
print("-" * 50)

# 3️⃣ Tuple Deletion
sample_tuple = (10, 20, 30, 40)  # Creating a sample tuple

# Deleting the tuple
del sample_tuple  
# print(sample_tuple)  # Uncommenting this will cause an error because the tuple is deleted
print("Tuple deleted successfully!")  
print("-" * 50)

# 4️⃣ Checking Membership (`in` and `not in`)
my_tuple = ("apple", "banana", "cherry", "date")  # Tuple containing fruit names

# Checking if "apple" exists in my_tuple
print("Is 'apple' in tuple?", "apple" in my_tuple)  # Output: True

# Checking if "mango" exists in my_tuple
print("Is 'mango' in tuple?", "mango" in my_tuple)  # Output: False

# Checking if "mango" is NOT in my_tuple
print("Is 'mango' not in tuple?", "mango" not in my_tuple)  # Output: True
print("-" * 50)

# 5️⃣ Concatenation of Tuples
tuple1 = (1, 2, 3)  # First tuple
tuple2 = ("a", "b", "c")  # Second tuple

# Concatenating tuple1 and tuple2
combined_tuple = tuple1 + tuple2  
print("Concatenated Tuple:", combined_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')
print("-" * 50)
