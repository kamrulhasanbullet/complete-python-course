# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dict = {}

name = input("Enter your name: ")
fav_lang = input("Enter your favorite language: ")
dict.update({name: fav_lang})

name = input("Enter your name: ")
fav_lang = input("Enter your favorite language: ")
dict.update({name: fav_lang})

name = input("Enter your name: ")
fav_lang = input("Enter your favorite language: ")
dict.update({name: fav_lang})

name = input("Enter your name: ")
fav_lang = input("Enter your favorite language: ")
dict.update({name: fav_lang})

print(dict)