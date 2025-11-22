#list can store anything or it can store all the data types in it. 
#list is mutable, it can be updated or changed anytime
#list start with 0 and end with n-1
#from reverse item can be accessed with negative values start from -1 to number to elements

num = [1 ,2 , 3, 4, 5]
print("type: ", type(num))  #type == list

print(num)  #it will print all the data stored in num list

print(num[2])  #it will print 3
print(num[-1]) #it will print 5
print(num[-5])  #it will print 1

all_list = [2, 3.3, "jittu", False, (3+2j)] #it has all the data types in the list

print(type(all_list[-1]))  #it will print complex

#adding element to list
all_list.append("kittu") #it will add element kittu in the end of the list
print(all_list)

all_list.append("kittu")
print(all_list)
print(all_list[6]) #it has value = kittu

#index 5 and 6 has value = kittu

all_list.remove("kittu")  #it will remove first occurence of element , it will remove kittu of 5th index
print(all_list)


#storing list in list
new_list = [2, 3, "jittu", [3, 5, 7]]
print(new_list[3][1]) #it will print 5 from second list in it

a_list = [[2, 3, 4], [1 , 2, 3], [7, 8, 9]]
print(a_list[2]) #it will print all 3 list

all_list[3] = True #it will change the value of 3 index in all_list from false to true
print(all_list)

all_list[4] = 5+6j #it will change the value of inndex 4 from 3+2j to 5+6j
print(all_list)

for item in all_list:
    print(item, end=" ")

print()
lis = ["apple", "mango", "orange", "banana"]
lis.insert(1, "pineapple") #this will add pineapple before 1st index
print(lis)

lis1 = ["apple", "banana", "orange"]
lis2 = ["pineapple", "watermelon", "kivi"]
lis1.extend(lis2)  #this will add elements of lis2 in the lis1
print(lis1)

#repeatation
lis3 = ["jittu"]
lis3 = lis3 * 3 #it will add jittu 3 times in lis3
print(lis3)

lis4 = [12]
lis4 = lis4 * 5
print(lis4)

lis5 = list(range(10)) #it will make a list of containing element from 0 to 9
print(lis5)

lis6 = list(range(0, 11, 2)) #it will make a list of even numbers
print(lis6)

#checking if the element is present or not in the list
ans = "potato" in lis1  #it will check if the potato is in the lis1
print(ans)

ans = "orange" in lis1
print(ans)  #true

ans = "mango" not in lis1  #it will check if the element is not present in the list
print(ans)

ans = "banana" not in lis1
print(ans)

#shallow copy
name = ["jittu", "kittu", "mittu"]
new_lis = name   #it will copy all the elements of name list into new_lis
print(new_lis)

name.insert(2, "chittu")  #if we change in name list then it will also affect new lis
print(name)
print(new_lis) #new lis also have the updated element at the same index

new_lis.insert(2, "littu") #new lis changes will also shown in name list
print(new_lis)
print(name)

#deep copy

b = name.copy()  #it will copy the element of name into b
print(b)

name.remove("littu")  #it will not affect the other list
print(name)   #it one value is deleted
print(b)  #it will remain same

#sorting of list
print(sorted(name))  #it will short the element by alphabetic
print(sorted(lis1))

#index function
value = name.index("chittu")  #it will store the first index of element
print(value)

value = lis1.index(lis1[3])
print(value)

#lenght of list
print(len(lis1)) #it will print total number of element present in lis1
print(len(name))

#count the occurance of element
book_lis = ["keep", "door", "knok knok", "door", "keep", "keep"]
value = book_lis.count("keep")  #keep is apeared 3 time
print(value)

value = book_lis.count(book_lis[1])
print(value)

#deleting a list
del lis1   #it will delete the lis1 list
# print(lis1)

#clear the list or empty the list
book_lis.clear()  #it will remove all the element of list
print(book_lis)

book_lis = ["keep", "door", "knok knok", "door", "keep", "keep"]
book_lis.pop()  #by default it will remove last element
print(book_lis)

book_lis.pop()  #by default it will remove last element
print(book_lis)

book_lis.pop(2) #it will remove the element of 2 index
print(book_lis)

#list comprehension
prices = [10, 20, 30, 40, 50]
double_price = [price *2 for price in prices]  #this is a sort way to copy the element in different list using condition
print(double_price)

double_price = [(price * 2)/ 5 for price in prices] #it will first make each price to double then it will divide it by 5 then ii will store in list
print(double_price)

names = ['jittu', 'kittu', 'mittu', 'chittu']
cap_nam = [name.capitalize() for name in names] #it will make each name in capitalize form
print(cap_nam)

#store the square of each number
number = [1, 2, 3, 4, 5, 6]
square_lis = [num**2 for num in number] #it will make square of each number and store it in square_lis
print(square_lis)

#splitting the list names
file_lis = ['name.docs', 'view.txt', 'uncode.img', 'cartton.mp4']
extension = [str.split(".")[-1] for str in file_lis] #it will split the names with . and then get the second value
print(extension)

#conditional list comprehension
email_lis = ['jittu1@gmail.com', 'jittu2@yahoo.com', 'jittu3@gmail.com', 'jittu4@yahoo.com', 'jittu5@yahoo.com']
only_yahoo = [email for email in email_lis if email.endswith('yahoo.com')] #it will only add email which ends with yahoo.com
print(only_yahoo)

strings = ['heelo', 'eorlds', 'jksuren', 'namememe', 'coooool']
big_str = [stri for stri in strings if(len(stri) > 6)]  #it will only include values whose length is greater than 6
print(big_str)

#nested list comprehension
pairs = [[x, y] for x in [1, 2, 3] for y in [4, 5, 6]]  #it will make the list of pairs of numbers eg. [1,4] [1, 5], [1, 6]
print(pairs)

# Create an empty stack using a list
stack = []  # Initializing an empty list to use as a stack

# Push elements onto the stack
stack.append(1)  # Add the first element (1) to the stack
stack.append(2)  # Add the second element (2) to the stack
stack.append(3)  # Add the third element (3) to the stack
print("Stack after pushing elements:", stack)  # Display the stack after all pushes

# Pop elements from the stack
popped_element = stack.pop()  # Remove the top element from the stack (Last In, First Out)
print("Popped element:", popped_element)  # Display the popped element
print("Stack after popping:", stack)  # Display the stack after the pop operation

# Check if the stack is empty
if not stack:  # If the stack is empty, print a message
    print("Stack is empty")
else:  # If the stack is not empty, print a different message
    print("Stack is not empty")

# Browsing data example - a stack of browsing history
browsing_data = ["home", "menu", "contact", "search"]  # List representing browsing history (stack)

browsing_data.pop()  # Remove the last element added (LIFO behavior: "search" will be removed first)
print(browsing_data)  # Display browsing data after the pop operation

# Queue implementation using deque
from collections import deque  # Importing deque for queue functionality

checkout = deque()  # Initializing an empty deque to use as a queue

# Add customers to the queue
checkout.append('cus1')  # Add the first customer
checkout.append('cus2')  # Add the second customer
checkout.append('cus3')  # Add the third customer
checkout.append('cus4')  # Add the fourth customer
checkout.append('cus5')  # Add the fifth customer

# First In, First Out (FIFO) operation
while checkout:  # Continue as long as the queue is not empty
    customer = checkout.popleft()  # Remove the first customer from the queue
    print("serving", customer)  # Serve the customer and display their name

# Queue implementation using the Queue module
from queue import Queue  # Importing the Queue class from the queue module

print_queue = Queue()  # Initialize an empty queue

# Add print jobs to the queue
print_queue.put("print 1st pdf")  # Add the first print job to the queue
print_queue.put("print 2nd pdf")  # Add the second print job to the queue
print_queue.put("print 3rd pdf")  # Add the third print job to the queue
print_queue.put("print 4th pdf")  # Add the fourth print job to the queue
print_queue.put("print 5th pdf")  # Add the fifth print job to the queue

# Process the print queue
while not print_queue.empty():  # Continue as long as the queue is not empty
    print_job = print_queue.get()  # Get the next print job from the queue (FIFO behavior)
    print('printing', print_job)  # Display the print job being processed


