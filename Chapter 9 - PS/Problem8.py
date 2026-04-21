# Write a program to make a copy of a text file ‘this.txt’.

with open("this.txt", "r") as source_file:
    content = source_file.read()

with open("copy_of_this.txt", "w") as destination_file:
    destination_file.write(content)
    
print("File copied successfully.")
