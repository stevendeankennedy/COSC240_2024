'''
    New string example.

    October 15, 2024
'''

def main():
    print("hello")
    #showSlices()
    #doFormatExample()
    #doFormatEx2()
    #doSplit()
    doSplit2()

def showSlices():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    nums = '0123456789'
    words = "Clark Kent is Superman"

    my_slice = alpha[1:-1:5] # slice, with a stride

    clark = words[0:5] # Thanks, Ashley!
    superman = words[14:] # Thanks, Isaac!
    secret = words[:-12]
    print(my_slice)
    print(clark)
    print(superman)
    print(secret)

def doFormatExample():
    name1 = "Clark"
    name2 = "Barry"
    name3 = "Diana"
    name4 = "Harley"

    print(f'{name1:-^10} {name2:!>10} {name3:?<10} {name4:<10}')

def doFormatEx2():
    team1 = "Ravens"
    team2 = "Steelers"
    team3 = "Titans"

    scores = [5, 20, 11]

    # Thanks Isaac for the print!  Shawn for the debug!
    fstr = f'{team1:-<10}{scores[0]:<3}\n{team2:-<10}{scores[1]:<3}'
    fstr = fstr + f'\n{team3:-<10}{scores[2]:<3}'
    print(fstr)

def doSplit():
    sentence = "Barry Allen is the Flash"
    words = sentence.split()
    sentence2 = '_'.join(words)

    print(sentence)
    print(words)
    print(sentence2)

def doSplit2():
    sentence = "a b c d e f g h i j k l m n o p"
    words = sentence.split()
    words = words[::2]
    sentence = ' '.join(words)
    print(sentence)

    print(sentence[-3:])

main()
