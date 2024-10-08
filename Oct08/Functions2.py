'''
More function examples, yay!

Special thanks: Ashley, Cameron, Madison, Chris
'''

def stars(n):
    # loop that prints the stars
    for i in range(n):
        print('*', end='')
    print()

def chars(ch, n):
    result = ch * n
    print(result)

# draw the lantern, with the pieces
def makeLantern(h):
    makeLanternTop()
    makeLanternMid(h)
    makeLanternBot()

# draw top of lantern
def makeLanternTop():
    print("  =====  ")
    print("=========")

# draw middle of lantern... height is based on parameter
def makeLanternMid(height):
    print("  -----  ")
    for i in range(height):
        print("  |   |  ")
    print("  -----  ")

# draw bottom of lantern
def makeLanternBot():
    print("=========")
    print("  =====  ")

def main():
    #stars(9)
    #stars(4)
    #stars(9)

    #makeLantern(5)

    chars('???', 5)
    chars(9, 9)

main()
