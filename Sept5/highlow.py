'''
Steve
Sept 5
High/Low Final Fantasy minigame
'''

'''
Rules:
    Game will pick a number between 1 and 20.
    The user will guess a number.
    The game will tell them if they are high or low.
    They have 3 chances to guess the number.
'''

import random
import math

target = random.randint(1,20) # the random number
user_num = int(input("Enter a guess:"))

if user_num == target:
    print("You guessed it!")
elif user_num > target:
    print("Too high!")
elif user_num < target:
    print("Too low!")
else:
    print(f"Nope!")

print(f'The target number was {target}')
