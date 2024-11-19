'''
    File I/O Practice with Pokimans!!!!!!
    authors: COSC 240
    date: 11/14/24
'''

import csv
import random

def main():
    # Goal:
    #   Get 5 random pokemon for my party
    #   Get  5 random cute names, name my pokemon
    #   Have a Pokimans Pizza/ Dance/ Snowboarding Party!
    list1 = readCSV("pokemon.csv")
    list2 = readCSV("cute_pet_names.csv")
    pokemonParty(list1, list2)

# Thanks Isaac, Ashley, and Kennedy(for showing up right after the theme song played)
def pokemonParty(pokedexlist, nameslist):
    #print(pokedexlist)
    #print(nameslist)

    pokedex = []

    # Do this 5 times:
    for i in range(5):
        numpoke = random.randint(1, len(pokedexlist))
        numpet  = random.randint(1, len(nameslist))

        pokemon = pokedexlist[numpoke][1]
        name    = nameslist[numpet][0] # get out of list
        #print(f'{pokemon}->{name}')

        newpokemon = {
            "dexnum"    : pokedexlist[numpoke][0],
            "pokename" : pokemon,
            "nickname"  : name,
            "type1"     : pokedexlist[numpoke][2],
            "type2"     : pokedexlist[numpoke][3]
            }
        pokedex.append(newpokemon)

    # Party time!
    for i in range(5):
        print(f'{pokedex[i]["pokename"]}, aka "{pokedex[i]["nickname"]}" parties!')


# Thanks Ashley, Isaac, and Chris!
def readCSV(fname):
    with open(fname, 'r') as theFile:
        the_reader = csv.reader(theFile, delimiter=',')

        contents = []
        for row in the_reader:
            contents.append(row)

        return contents
    
main()
