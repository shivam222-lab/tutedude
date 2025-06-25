'''Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.'''

num1 = int(input("enter a num1 "))
num2 = int(input("enter a num2 "))
def add():
    return num1+num2
def sub():
    return num1-num2
def multi():
    return num1*num2
def div():
    return num1/num2


print("num1 + num2 is ",add())
print("num-num2 is ",sub())
print("num*num2 is ",multi())
print("num1/num2 is ",div())
