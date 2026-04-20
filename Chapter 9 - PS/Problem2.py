# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random


def game():
    print("Welcome to the game! Try to beat the Hi-score!")
    score = random.randint(0, 100)

    with open("hi-score.txt") as f:
        hi_score = f.read()
        if hi_score != "":
            hi_score = int(hi_score)
        else:
            hi_score = 0

        print(f"Your score: {score}")
        if score > hi_score:
            print("Congratulations! You've set a new Hi-score!")
            with open("hi-score.txt", "w") as f:
                f.write(str(score))
        return score


game()
