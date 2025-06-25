'''ASSIGNMENT 2:
Module 3: Control Structures in Python
 
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.'''


num = int(input("enter a number: "))

if num %2==0:
    print ("number is even",num)
else:
    print("numer is odd",num)
