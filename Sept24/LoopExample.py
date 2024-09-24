'''
    In class example for LOOPS!

    authors: COSC 240 class
    Sept 24, 2024
'''

# print a sum
my_sum = 0
i = 0

val = int(input("Enter number>"))

while (i <= val):
    my_sum += i #my_sum = my_sum + i
    i += 1 #i = i + 1

avg = my_sum / (i-1)

print(f'Average of 1-{val} is {avg}')

my_list = ['Chris', 'Wesley', 'Emmanuel', 'Madison', 'Isaac']

for name in my_list:
    print(name)

for i in range(5):
    print(i)
