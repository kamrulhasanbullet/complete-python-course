# Repeat program 4 for a list of such words to be censored.

words = ["bad", "ugly", "nasty", 'downkey', 'stupid']

with open("file.txt", "r") as file:
    content = file.read()

for word in words:
    content = content.replace(word, "*" * len(word))

with open("file.txt", "w") as file:
    file.write(content)
