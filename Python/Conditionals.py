# the conditions are used to run the code for particular scenario

if 3>4:                    #if block is used for checking the condition , 3>4 is a condition
    print("it is false")    #this code will run if the condition is true, otherwise it will not run this part

if (3 == 3):    #condition should be in parantheses for better understanding and readablity
    print("it is true")

number1 = input("Enter the number")  #it does not give integer, it will give number in string form

number1 = int(number1)

if( number1 < 40):
    print("it is less than 40")
else:        #else run when if condition is false
    print("it is greater than 40")  




if( number1 % 2 == 0):    #it will check if the given number is divided by 2 and have 0 as remainder
    print("The number will be divide by 2")
else:             #if the number is not divide by 2 and does not have remainder 0
    print("The number will not be divide by 2, and will have 1 as remainder")

#ELIF is used for checking multiple condition in a particular code

if(number1 % 2 == 0):
    print("The number is divided by 2")
elif(number1 % 3 == 0):                    # elif will check another condition , if the first if block condition is not true
    print("The number is divided by 3")
elif(number1 % 5 == 0):                    # it will third codition if the first two is false
    print("The number is divided by 5")
else:                                     #if the above conditions is not true then it will run this code
    print("The number is not divided 2, 3, and 5")


#claculate student grade
marks = input("Enter the marks of student :   ")

marks = int(marks)

if( marks > 90):
    print("Grade A")
elif( 80 <= marks < 90):
    print("Grade B")
elif( 70 <= marks < 80):
    print("Grade C")
elif( 60 <= marks < 60):
    print("Grade D")
else:
    print("Fail")

#check if student is pass or not
Grade = input("Enter the Grade of Student:  ")
if( marks > 80) & (Grade == "A"):
    print("Passed with 1st Division")
elif( 60 <= marks < 80 ) & (Grade == "B"):
    print("Passed with 2nd Division")
else:
    print("Third Division")