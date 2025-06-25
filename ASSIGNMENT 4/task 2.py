
with open("output.txt", "w") as file:
    data = input("Enter initial data to write to the file: ")
    file.write(data + "\n")

with open("output.txt", "a") as file:
    more_data = input("Enter additional data to append: ")
    file.write(more_data + "\n")


print("\nFinal contents of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())