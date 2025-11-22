#sets are unordered collection of unique elements
#we can also add different types of data
#it is mutable


s = {"jittu", "kittu"}  #declaration of sets
print(type(s)) #it will print set

a = {"orange", "apple", "apple", "orange", "mango"}
print(a) #it will only print one item only one time

#adding an element to set
s.add("mittu") 
print(s)

s.remove("jittu") #this will remove the element from the set
print(s)

#accessing the elements of set
for item in a:
    print(item)

# Creating a list with duplicate values
list1 = [2, 2, 3, 1, 1, "jittu", "jittu", "ajay"]

# Converting list to a set to remove duplicates
s = set(list1)
print("Set after removing duplicates:", s)  # Output will have unique values only

# Using set comprehension to create another set from 's'
set1 = {x for x in s}
print("New set using set comprehension:", set1)

# Uncommenting the below line will cause an error because sets are unordered and do not support indexing
# print(s[1])

# Invalid set example: Uncommenting the below will throw an error because sets can't have mutable elements like another set
# set2 = {2, 4, 5, 3, {1, 6, 7}}  # This will give a TypeError

# Creating a set with a tuple (since tuples are immutable, they can be added to a set)
set3 = {2, 4, 3, 5, (1, 6, 7)}
print("Set containing a tuple:", set3)

# Uncommenting the below line will cause an error because slicing is not supported in sets
# print(set3[:4])

# Adding elements to the set 's'
s.add("kittu")  # Adding a string
s.add(7)       # Adding an integer
print("Set after adding elements:", s)

# Adding multiple elements using update()
s.update([8, 9, "hello", "world"])
print("Set after adding multiple elements:", s)

# Removing an arbitrary element using pop()
s.pop()  # Removes a random element since sets are unordered
print("Set after pop operation:", s)

# Clearing all elements from set1
set1.clear()
print(set1)  # Output: set()

# Discarding an element (does not raise an error if element is absent)
s.discard(2)
print(s)  # Output: Set without the number 2

# Define two sets containing some common and some unique elements
s1 = {"mango", "apple", "banana", "grapes"}
s2 = {"pineapple", "grapes", "apple", "mango"}

# UNION: Combines all unique elements from both sets
s3 = s1 | s2  
print("Union:", s3)  
# Output: {'mango', 'banana', 'grapes', 'pineapple', 'apple'}

# INTERSECTION: Returns only the common elements present in both sets
s3 = s1 & s2  
print("Intersection:", s3)  
# Output: {'grapes', 'mango', 'apple'}

# DIFFERENCE: Returns elements present in s1 but not in s2
s3 = s1 - s2  
print("Difference (s1 - s2):", s3)  
# Output: {'banana'}

# DIFFERENCE (reversed): Returns elements present in s2 but not in s1
s3 = s2 - s1  
print("Difference (s2 - s1):", s3)  
# Output: {'pineapple'}

# SYMMETRIC DIFFERENCE: Returns elements that are unique to each set (not in both)
s3 = s1 ^ s2  
print("Symmetric Difference:", s3)  
# Output: {'banana', 'pineapple'}

# Example with numbers to understand set operations better
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union (set_a | set_b):", set_a | set_b)  # {1, 2, 3, 4, 5, 6}
print("Intersection (set_a & set_b):", set_a & set_b)  # {3, 4}
print("Difference (set_a - set_b):", set_a - set_b)  # {1, 2}
print("Difference (set_b - set_a):", set_b - set_a)  # {5, 6}
print("Symmetric Difference (set_a ^ set_b):", set_a ^ set_b)  # {1, 2, 5, 6}

# FROZENSET: An immutable version of a set, meaning elements cannot be added or removed
my_fs = frozenset([1, 2, 4, 5, 7, 3, 4, 2])  # Duplicates are automatically removed
print("Frozen set:", my_fs)  
# Output: frozenset({1, 2, 3, 4, 5, 7})

# Check the type of the frozen set
print("Type of my_fs:", type(my_fs))  
# Output: <class 'frozenset'>

# The following operations are invalid because frozensets do not support modification:
# my_fs.add("jittu")  # ERROR: AttributeError: 'frozenset' object has no attribute 'add'
# my_fs.remove(2)  # ERROR: AttributeError: 'frozenset' object has no attribute 'remove'
