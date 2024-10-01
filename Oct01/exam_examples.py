'''
    Example code for exam 00
'''

odd_numbers = 0 # count the nums
for i in range(4): #Thanks, Covy, Ellie, and Chris!
	num = int(input(">")) # Thanks, Ellie, Kevin
	if (num > 0) and (num % 2 != 0): # Thanks Madison and Ellie!
		odd_numbers += 1

print(odd_numbers)

