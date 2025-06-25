'''ASSIGNMENT 4:
Module 5: Files, Exceptions, and Errors in Python
 
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''
try:
    with open("output.txt", "r") as file:
        for line in file:
            print(line.strip()) 
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")