'''
    This is my chatbot example.
'''

def main():
    pass

    while(True):
        statement = input(">")
        # if they ask about movies, we'll say something
        if 'movie' in statement:
            print("What kinds of movies do you like?")
        else:
            print("That's nice.  Thanks for telling me!")

main()
