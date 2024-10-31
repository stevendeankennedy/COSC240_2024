'''
Spooky example for exceptions. ( ^v^ )
10/29/24

authors: COSC 240 Fall 24 class, yay!
Special thanks to: Chris
'''

def main():
    print("Example!")
    exceptionexample1()
    #exceptionexample2()

# adds two POSITIVE numbers, a and b
def exceptionexample1():
    try:
        a = getInt("num1>")
        b = getInt("num2>")
        r = a + b
        print(f'{a} + {b} = {r}')
    except ValueError as v:
        print(v)
    except:
        print("Please enter numbers only!")

def getInt(msg):
    a = int(input(msg))
    if a < 0:
        raise ValueError("Let's stay positive!")

def exceptionexample2():
    try:
        a = int(input("num1>"))
        b = int(input("num2>"))
        r = a / b
        print(f'{a} / {b} = {r}')
    except ZeroDivisionError:
        print("Can't divide by zero, sorry!")
    except ValueError:
        print("Oops that value won't work...")
    except:
        print("Something else happened... this shouldn't occur")
        
main()
