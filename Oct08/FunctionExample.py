'''
Example program that experiments with functions.

Authors: COSC 240
Special Thanks: Shawn, Madison, Chris
'''

# Adds two numbers and returns the result
def add(a, b):
    return a + b

# sub
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# a to the power of b (a^b)
def exp(a, b):
    return a ** b
    
def main():
    print("This is our function example!")

    a = int(input("Enter first num>"))
    op = input("Enter operator>")
    b = int(input("Enter second num>"))

    result = 0

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '/':
        result = divide(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '**' or op == '^':
        result = exp(a, b)
    else:
        print(f"I don't understand {op} operator.")
    print(f"{a} {op} {b} = {result}")

main()
