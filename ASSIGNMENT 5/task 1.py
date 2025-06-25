'''Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.'''

dict1 = {"python":40,"c++":20,"php":10 ,"html&css":50}
print(dict1)
sub = input("enetr sub : ")
marks =int (input("enetr marks : "))
dict1.update({sub:marks})

print("Updated Dictionary:",dict1)
