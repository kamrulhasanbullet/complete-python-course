# We all have played Snake, Water, Gun game in our childhood. If you haven’t, google the rules of this game and write a Python program capable of playing this game with the user.

"""
1 for snake
-1 for water
0 for gun
"""

import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter Your Choice: ")
yourDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = yourDict[youstr]

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if computer == you:
    print("Its a Draw")
elif (computer - you) == -1 or (computer - you) == 2:
    print("You Lose!")
else:
    print("You Win!")
