'''
    Searching and Sorting Examples

    Special thanks to Dean and Maliyah
'''
import random

# Thanks, Ellie, et al
# It is not a good idea to actually call this function.......
def bogoSort(mylist):
    # randomly shuffle
    # check to see if it is order, if not, try again
    isSorted = False
    count = 0
    while(isSorted == False):
        random.shuffle(mylist)
        # check
        for i in range(len(mylist)-1):
            if mylist[i] < mylist[i+1]:
                continue
            else:
                break
            isSorted = True
        count += 1
        print(count)

    print(f"Sorted after {count} tries!")
                
        
# Thanks, Ashley, Chris, Ellie, et al
def selectionSort(mylist):
    largest = 0
    mark = len(mylist)

    for j in range(len(mylist)):
        # Get the largest
        largest = 0
        for i in range(mark): #TODO: maybe bug here
            if mylist[largest] < mylist[i]:
                largest = i
        print(f'L:{largest}({mylist[largest]}), {mylist[:mark]} {mylist[mark:]}')
        mark = mark - 1
        swap(largest, mark, mylist)
        #print(mylist)


# Special thanks to Chris, Ashley, et al
def bubbleSort(mylist):
    print(mylist)

    # Get all the bubbles
    for j in range(len(mylist)):
        # take a bubble to the end of the list
        for i in range(len(mylist)-1):
            if mylist[i] > mylist[i+1]:
                swap(i, i+1, mylist)
            print(mylist)

# quick function to swamp positions in list
# Thanks, Madison!
def swap(a, b, mylist):
    tmp = mylist[a]
    mylist[a] = mylist[b]
    mylist[b] = tmp


# A simple implementation of a sequential (linear) search
def linearSearch(target, mylist):
    for num in mylist:
        if num == target:
            print(f"Found {target}!")
            return
        else:
            print(num, end=' ')

def main():
    test = [6, 4, 7, 2, 5, 1, 8, 3]
    #linearSearch(1, test)
    #bubbleSort(test)
    #selectionSort(test)
    #bogoSort(test)

main()
