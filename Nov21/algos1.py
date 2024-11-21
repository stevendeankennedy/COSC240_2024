'''
    Algorithm Analysis & stuff

    authors: COSC 240 Fall 24
'''

import math

# Thanks, Chris!
def constant(n):
    return 1  # +1, there's literally just this 1 step

# Thanks, Ashley!
def linear(n):
    count = 0  # +1

    # this gives us n
    for i in range(n): # +n*(1)
        count += 1 # +1

    return count # +1

# Thanks, Madison
# O(n^2) = O(n * n)
def quadratic(n):
    count = 0 # +1

    # this is n
    for i in range(n):# n *(n*(1))
        # this is also n
        for j in range(n): # n*(1)
            count += 1 # +1

    return count # +1

# O(lg n)
def logarithmic(n):
    count = 0 # +1

    limit = math.ceil(math.log2(n))
    for i in range(limit): # lg n
        count += 1 # +1

    return count # +1

def myprint(n, msg, result):
    print(f'{msg}: With n={n}, we got a count of {result}')

def main():
    n = 100
    myprint(n, "O(n)", linear(n))
    myprint(n, "O(1)", constant(n))
    myprint(n, "O(n^2)", quadratic(n))
    myprint(n, "O(lg n)", logarithmic(n))
    n = 10000
    myprint(n, "O(n)", linear(n))
    myprint(n, "O(1)", constant(n))
    myprint(n, "O(n^2)", quadratic(n))
    myprint(n, "O(lg n)", logarithmic(n))
    
main()
