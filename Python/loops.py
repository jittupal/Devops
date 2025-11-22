#loops is used to perform a task repeatedly
#if the condition of loops true then it will repeatedely execute thec code and if condition is false then it will stop the execution

#print 10 number from 1 to 10

i = 1
while (i < 11):
    print("The Value Of I Is:  ", i)
    i = i + 1

#print even numbers from 1 to 50

i = 1
while( i <= 50):
    if(i % 2 == 0):
        print(i, end=" ")
    i = i + 1
print(" ")


#check if number is prime or not
number1 = int(input("Enter the number:  "))
prime = True
i = number1 - 1
while(i > 1):
    if(number1 % i == 0):
        print("This is a prime number")
        break
    i = i -1
else:
    print("This is not a prime number")

# if prime:
#     print(number1, "is prime")
# else:
#     print(number1, "is not prime")

#sum of firt 10 numbers from 1 to 10
i = 1
sum = 0
while(i <= 10):
    sum = sum + i
    i = i + 1

print("The Sum of 10 Numbers are:  ", sum)


# ********** FOR LOOP ************* #
j = 1
for i in "jittu":
    print("The ", j, "word is : ", i)
    j = j + 1


list_item = ["jittu", "kittu", "mittu", "chittu"]

person = input("Enter the name you want to search:  ")

for i in list_item:  #for loop checks each item in the list one by one
    if (i == person):
        print("Yes, ", i, " is present in the list")
        break       #if condition is true then it will break the loop
else:
    print(person, "is not present in the list")


for i in range(1, 9):  #range is from 1 to 8 excluding 9
    print(i, end=" ")

print(" ")
 
# printing all odd number from 1 to 50
for i in range(1, 51, 2):  #range is from 1 to 50 having a difference of 2
    print(i, end=" ")

print()
print()

#print the pattern

row = 1
while( row <= 4):   
    col = 1          #everytime the loop re-run then this will be 1 for everytime
    while(col <= row):      #it will check from 1 to until current row value
        print("*", end=" ")
        col = col + 1
    print()
    row = row + 1

print()
print()


#using for loop

for i in range(4):   #it will start from 0 to 3
    for j in range(i+1):  #i + 1 specify how many time it will run
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1

#square pattern

print()
print()

row = 1
while(row <= 3):
    col = 1
    while(col <= 3):
        print("*", end=" ")
        col = col + 1
    print()
    row = row + 1


print()
print()

#using for loop
for i in range(3):
    for j in range(3):
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1
