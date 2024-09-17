'''
    Conditional example program

    Gets a number grade from the user, and tells the user
        what letter grade they got
'''

# Authors: COSC people
# COSC240
# September 17

# get input from the user
num_grade = input("Enter grade>")
num_grade = float(num_grade)
let_grade = 'X'
# make comparisons with that number
# if it is >= whatever value, assign the proper letter
#   A is 89.5 - 100
#   B is 79.5 - 89.5
#   C is 69.5 - 79.5
#   D is 59.5 - 69.5
#   F is 0 - 59.5
if num_grade < 59.5:
    let_grade = 'F'
elif num_grade < 69.5: # num_grade is >= 59.5 
    let_grade = 'D'
elif num_grade < 79.5:
    let_grade = 'C'
elif num_grade < 89.5:
    let_grade = 'B'
else: # that means it is NOT F, D, C, or B... so its A
    let_grade = 'A'

# print it out
if num_grade < 0:
    print("How do you have a negative grade???")
elif num_grade > 105:
    print ("That's a really high grade...")
else:
    print(f'{num_grade} is {let_grade}')

