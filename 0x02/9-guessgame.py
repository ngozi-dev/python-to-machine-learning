#!/usr/bin/python3
# a module that impliment a guess game

import random

trial = 3
while trial > 0:
    num = random.randint(1, 5)
    guess = int(input("Guess a number between 1 and 5: "))
    if guess == num:
        print("Congratulations! you guessed it right")
        break
    else:
        print("Wrong guess, try again")
    trial -= 1
    
