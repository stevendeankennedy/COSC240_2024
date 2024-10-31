

def myfunct(m, a):
    m[0] = 99
    a = 99

def stringversion(my_str):
    my_str = "bye"

mylist = [1,2,3]
a = 1

myfunct(mylist, a)

print(mylist)
print(a)

greeting = "hello"

stringversion(greeting)
print(greeting)
