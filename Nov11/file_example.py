'''
    File I/O Practice and Super Fun Exciting Time!!!!!!
    authors: COSC 240
    date: 11/12/24
'''

import csv

def main():
    #readFile("numbers.txt")
    #readFile("pokemon.csv")

    #readFileByLine("numbers.txt")
    #writeFile("steve.txt", "hello world")

    #readWriteNums("numbers.txt", "new_nums.txt")

    #readWriteNumsVer2("numbers.txt", "new_nums2.txt")

    readCSV("pokemon.csv")

# Thanks Ashley, Isaac, and Chris!
def readCSV(fname):
    with open(fname, 'r') as theFile:
        poke_reader = csv.reader(theFile, delimiter=',')

        for row in poke_reader:
            dex_num = row[0]
            name = row[1]
            type1 = row[2]
            type2 = row[3]
            print(f'{dex_num}:{name} is {type1} and {type2} type!')

def writeFile(fname, msg):
    theFile = open(fname, "w")
    theFile.write(msg)
    theFile.close()

# fname1 is the read file
# fname2 is the write file
''' Thanks Isaac and Chris! '''
def readWriteNums(fname1, fname2):
    theFile = open(fname1)
    contents = theFile.readlines()
    theFile.close()

    theFile2 = open(fname2, 'w')
    for line in contents:
        num = int(line)
        num += 1
        theFile2.write(str(num) + '\n')
    theFile2.close()

''' Thanks Isaac and Chris! '''
def readWriteNumsVer2(fname1, fname2):

    print(f'Reading {fname1} and writing {fname2}')
    with open(fname1, 'r') as theFile:
        with open(fname2, 'w') as theFile2:
            for line in theFile:            
                num = int(line) + 2
                theFile2.write(str(num) + '\n')
            
def readFile(fname):
    # open
    theFile = open(fname)
    
    # read
    contents = theFile.read()
    print(contents) # <- should do this after close
    
    # close
    theFile.close()

'''
    Read by line.
    Special thanks to Madison, Ellie, Ashley
'''
def readFileByLine(fname):
    theFile = open(fname)
    # read all the lines
    contents = theFile.readlines()
    theFile.close()

    #print(contents)

    total = 0
    for line in contents:
        num = int(line)
        total += num
    print(f'The sum of the file is {total}')
    

main()
