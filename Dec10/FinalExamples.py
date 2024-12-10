'''
    Examples for final exam
'''

def show_stride_example():
    mystr = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    print(mystr)
    print(mystr[0:5])
    print(mystr[10:13])
    print(" --> now lets see strides")
    print(mystr[0:12])
    print(mystr[0:12:1])
    print(mystr[0:12:2])
    print(mystr[0:12:3])
    print(mystr[::1])
    print(mystr[::-1])
    print(mystr[::-2])

def show_dictionary_example():
    person1 = {
        "name" : "Chris",
        "major" : "Cybersecurity",
        "pokemon" : "Pikachu"
        }
    person2 = {
        "name" : "Jo",
        "major" : "Math",
        "pokemon" : "Gengar"
        }
    person3 = {
        "name" : "Saorise",
        "major" : "English",
        "pokemon" : "Vanillish"
        }
    myPersons = [person1, person2, person3]
    print(person1)
    print(person1["pokemon"])
    #print(myPersons)

    for k in person1:
        print(k, ":", person1[k])
    print()
    
    for v in person1.values():
        print(v)
    print()

    for k,v in person1.items():
        print(k, ":", v)
    print()
    
    for i in range(len(myPersons)):
        print(i, ":", myPersons[i]["name"])
    print()

    for i in range(len(myPersons)):
        for j in range(len(myPersons)-1):
            print(myPersons[i]['name'], end=',')
        print()

def show_multiplication_table():
    for i in range(1,10):
        for j in range(1,10):
            print(f'{i*j:5}', end='')
        print()

def show_trycatch():
    print("Enter positive numbers only!")
    a = int(input("a>"))
    b = int(input("b>"))

    if a < 0 or b < 0:
        raise ValueError("That sucks sorry, can't do it")

    try:
        print(a / b)
    except TypeError:
        print("No can div by string!")
    except ZeroDivisionError as x:
        print("Sorry, that would be illegal.  Go to jail.")
        print(x)

def main():
    #show_stride_example()
    #show_dictionary_example()
    #show_multiplication_table()
    show_trycatch()

main()
