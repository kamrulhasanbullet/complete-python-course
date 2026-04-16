# Write a program to create a dictionary of bangla words with value as their English translations. Provide user with an option to look it up!

words = {
    "Aaam": "Mango",
    "Kola": "Banana",
    "Komola": "Orange",
}

word = input("Enter a Bangla word to look up its English translation: ")

translation = words[word]

print(translation)
