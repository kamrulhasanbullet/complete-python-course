# Guess the number

import random

number = random.randint(1, 100)
a = -1
guesses = 1

while a != number:
    a = int(input("Guess the number please: "))
    if a > number:
        print("Lower nubmer please")
        guesses += 1
    elif a < number:
        print("Higher nubmer please")
        guesses += 1
print(f"You have guessed the number {number} correctly in {guesses} attempts")
