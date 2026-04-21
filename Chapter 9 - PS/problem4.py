# A file contains a word “Donkey” multiple times. You need to write a program which replaces this word with ###### by updating the same file.

with open("file.txt", "r") as file:
    data = file.read()

contentNew = data.replace("Donkey", "######")

with open("file.txt", "w") as file:
    file.write(contentNew)
