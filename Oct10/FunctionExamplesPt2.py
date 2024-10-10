'''
    Some more function examples in Python.

    Thanks Ellie, Chris, Madison, Covy,
        Dean, Donald, Nathan, Ashley, Isaac!
'''

# Function that gets name and favorite color
def get_name_and_color():
    print("Please enter your name and favorite color.")

    name = input('name>')
    color = input('color>')

    return name, color

def print_name_and_snacks(name, snacks):
    print(name)
    for s in snacks:
        print(s)

    snacks.append('goldfish')
    snacks.append('Snickers')
    name = "some other name"
    print(name,'?')

# remember: Python is 'dynamically typed'
def mess_with_this(value):
    print("hmm....")
    print(value)

    return value + value

def doAThing():
    print("something")
    mess_with_this("?")
    mess_with_this("!")

def showWord(word):
    # base case

    # recursive case
    print(word, end=' ')
    showWord(word)

def countRecursion(count):
    # base case
    if count == 0:
        return

    # recursive case
    print(count)
    countRecursion(count - 1)
    print(count)

def printLetters(word):
    print(word[0])

def printLettersReverse(word):
    i = len(word)-1
    _printLettersReverse(word, i)

def _printLettersReverse(word, i):
    # base case
    if i < 0:
        return
    
    # recursive case
    i = i-1
    _printLettersReverse(word, i)
    print(word[i], end='')


    
# This function tests our other ones
def main():
    # example 1, returning a collection of values
    name, x = get_name_and_color()
    print(name, x)

    # example 2, passing immutable v mutable types
    snacks = ['chips', 'gummies', 'cookies']
    print_name_and_snacks(name, snacks)
    print(snacks)
    print(f'Is it {name}?')

    # example 3, types and functions
    my_list = [1, 2, 3, 4]
    word = "word"
    x = mess_with_this(99)
    print(x)
    x = mess_with_this(my_list)
    print(x)
    x = mess_with_this(word)
    print(x)
    print(word)

    # calling other functions
    doAThing()
    #showWord(word) # don't call this!
    countRecursion(5)

    # reverse name
    #printLetters("abcde")
    printLettersReverse("abcde")

main()
