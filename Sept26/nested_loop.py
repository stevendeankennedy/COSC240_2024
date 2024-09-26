'''
    More loop examples!

    Special thanks to Isaac, Chris, Madison, and Ashley!
    
    Sept 26
'''

num = int(input('>'))

# draw a box
for i in range(num):
    for j in range(num):
        print('x', end='')
    print()

# multiplication table
for i in range(num):
    for j in range(num):
        x = i*j
        print(f'{x:3}', end='')

    print() 

# selection sort

my_list = [6,1,5,4,3]
print('before:', my_list)
for j in range(len(my_list)):
    # find largest
    largest = 0
    mark = len(my_list) - j
    print(f'mark :{mark}', end=' ')
    
    for i in range(mark):
        if (my_list[i] > my_list[largest]):
            largest = i
    # swap to end
    mark = mark - 1 # adjust value
    tmp = my_list[mark]
    my_list[mark] = my_list[largest]
    my_list[largest] = tmp

    print(my_list, f'largest:{my_list[largest]}')

print('after: ', my_list)
