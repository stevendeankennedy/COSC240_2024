'''
    Example loop problem.

    Get a bunch of grades from user.
    put all of them into a list.
    print out the list, and their letter grades
    print out the average grade

    authors: COSC 240 class
    special thanks to: Ashley, Isaac, Madison, Chris
        Ellie, Emmanuel, Dean
    Sept 24, 2024
'''

# we'll accept any number of grades
# stop taking input if they type in -1

dostuff = True
grades = []
while(dostuff):
    grade = int(input("Enter Grade>"))
    if (grade == -1):
        dostuff = False
    else:
        grades.append(grade)

print(grades)

mysum = 0
# go through all the grades and do stuff
for grade in grades:
    letter_grade = '?'
    if (grade >= 90):
        letter_grade = 'A'
    elif (grade >= 80):
        letter_grade = 'B'
    elif (grade >= 70):
        letter_grade = 'C'
    elif (grade >= 60):
        letter_grade = 'D'
    else:
        letter_grade = 'F'


    print(f'{grade}:{letter_grade}')
    mysum += grade
avg = mysum / len(avg)

print('The average is', avg)
