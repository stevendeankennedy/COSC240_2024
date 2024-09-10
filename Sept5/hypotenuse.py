'''
Steve + co
Sept 5, 2024
Get hypotenuse
'''

import math

# get two side lengths
a = int(input("a>"))
b = int(input("b>"))
# square each of them
c = math.pow(a,2) + math.pow(b,2)
#c = (a ** 2) + (b ** 2)  # <- alternate version
# get square root of their sum
c = math.sqrt(c)

print(f'The hyp ohooho tonuuse of a triangle with sides {a} and {b} is {c:.5f}.')
