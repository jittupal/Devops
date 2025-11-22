a = 4
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # this will give remainder after dividing the number
print(a // b) # this // is a floor oprators, it round of the value to it's nearest integer
print(a ** b) # ** is used for know the power eg. a to power b

# *****COMMPARISION OPERATORS****
print(a > b) #is a greater than b
print(a < b) #is a less than b
print(a == b) #is a equal to b
print(a >= b) #is a greater than or equal to b
print(a <= b) #is a less than or equal to b
print(a != b) #is a not equal to be


#******Logical Operators******
print((a == 4) and (b == 3)) #it will check both , and if both is true then it is true otherwise it is false
print((a == 3) or (b == 4)) #if both are false then it is false otherwise it is true
print(not ( a == 4)) #if it is true then it will print false and vice verca


# ********Membership Oprators*******
name = "jittu"
print("jittu" in name)
print("ajay" in name)
name_list = ["jittu", "kittu", "mittu", "ajay"]
print("ajay" in name_list)

# ******Identity Oprators*******
c = 4
d = 3
print(c is d) #it will compare the location of variables, it checks if both are same or not
#it will give false because both variable referring to different memory location

# ****bitwise oprators*****
print(10 & 10) #& (and) oprators checks with each bit of 10 and then perform calculation
# 10 in bit = 1010

print(bin(10)) #bin will print the bits of integer

print(a | b) #or oprators

print(bin(a | b))

print(bin(3))
print(~3)
print(bin(~3)) #it will print nagation of 3 in bits

print(3 ^ 5) # ^ xor operators, if both values is same then it will be 1 otherwise 0.

print(1 << 2) # << left shift operator will shift the bits of 3 from 2 place to left and fill the 0s in right

print(4 >> 2) # >> right shift operator will shift the bits of 4 from 2 place to right and fill the 0s in left
