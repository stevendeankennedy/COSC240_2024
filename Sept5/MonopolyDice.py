'''
Steve Kennedy & friends
Sept 5
This is a sample program using modules
This comment
lasts
multiple
lines.
'''

# Get 2 dice, roll them and print out how many
#   monopoly spaces I get to move

import random

# make two variables for dice
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

steps = dice1 + dice2

print(f'You can move {steps} steps.')
