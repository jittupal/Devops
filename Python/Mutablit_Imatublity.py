list_con = [1, 2, 4.3, 3+3j, True, "jittu"]
print(list_con[5])

"""
mutable

if we are able to change or modify the value in a container after it's creation then it is mutable
list, dictionary and set are mutable
"""

list_con[5] = "kittu"  #value of jittu is changed to kittu
list_con[3] = 200  #value of 3+3j is changed to 200

print(list_con) 
#output => [1, 2, 4.3, 200, True, 'kittu']

"""
immutable

if we are not able to change or modify the value in a container after it's creation then it is immutable
tuple, string are immutable
"""

name = "jittu"
# name[0] = 'k' #trying to change 'J' to 'k'
# print(name)  #will give error
