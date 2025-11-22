print("hello world")
a = 3
print(a)
b = 3.5
print(type(b))
 # type tell what is the datatype we used
c = a * "hii"  #this will print hii 3 times because a has value 3
print(c) #this will make integer to string without any error
print(type(c))

com = 4+3j
print(type(com))
print(com.real) #real number of complex value
print(com.imag) #imaginary number of complex value

"""
Rule of defining a variable
1. we can start with letter or underscore but we can not use number or anything else
2. It should not be any keywords

example:

3 = a # this will give you error
1name = "ajay" #this will also give error
data-analytics = "anything" #this will also give error

correct ways:
name = "ajay"
value = 5
data_analytics = "anything"


"""

a = "jittu"
print(a)

#a = a + 2 #we can not convert string to int directly
#print(a)

#to find keywords in python
print(help('keywords'))

#c = 3 #assignment statement
#a + b = 6 #expression statement

#a = input("Enter the first number")  #for taking input from the user
#print(a)
#print(type(a))  #input takes every value as string

type = "jittu" #The value is assigned to type keyword
#print(type(type)) #so we can not able use type for knowing data types

print(type)  #this will print value of type assigned to it.
#print(type(a))  #this will give error because type is used here as variable so we can not able to use it for knowing data types.
