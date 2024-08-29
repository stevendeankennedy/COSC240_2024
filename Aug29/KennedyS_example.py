# Steve
# 8/29/24
# This is our I/O example program.

# some variables to help us out ---------
x = "Hello"
y = 1+1 # addition
z = x + "\n" + "World!" # concatenation

firstname = "Steve"
lastname = "Kennedy"

anotherstring = f"{x}{y}"
nameis = f"My name is {firstname} {lastname}"
nameis2 = "My name is {firstname} {lastname}"


# print statements using the variables ------
print(x) # Thanks Ellie and Covy!
print(y)
print(z)

print(anotherstring)

print(nameis)
print(nameis2)


# input examples -----------------------------
print("This is the input section...")

first = input("Type something> ")
print(first)


# Thanks Ellie and Isaac!
# 1 Get first and last name from user
print("Please enter first name")
first = input("First name")
print("Please enter last name")
last = input("Last name")
# 2 print a hello message
#   using fstrings
hello = f"Hello {first} {last}!"
print(hello)


# Next example, using addition
# Thanks Madison, Covy, and Shawn!
firstv = input("Please enter first value>")
secondv = input("Please enter second value>")
v1 = int(firstv) # convert to int
v2 = int(secondv) # convert to int

difference = v1 + v2
outputstring = f"{v1} + {v2} = {difference}"
print(outputstring)





















