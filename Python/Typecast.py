#typecasting means changing one variable to different variable
#implicit typecasting means we don't have to define , it's integer or string or float
#explicit typecasting means we can convert by using inbuilt function

a = "3"
b = 3
# print(a + b) this will give error

print(type(a)) # type of a is string
print(type(int(a))) # now type of a is integer
a = int(a) #string a now converted to int a , who stores the value 3 in integer
print(a + b)

c = 2.3
c = int(c) #this will change float to int

d = 3
e = 3
d = str(d)
e = str(e)
print(d + e) #it will adds the string after it covert from int to string

f = "3"
print(bool(f)) #any value greater than 0 will be true

g = 3
g = float(g) #it will convert int to float 
print(g)