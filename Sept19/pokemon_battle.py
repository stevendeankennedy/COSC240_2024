'''
    Example program - Pokemon Battle!
'''

# Pseudo code... -------
# pick 2 pokemon (and 1 enemy pokemon)

pokemon1 = {
    "name" : "Pikachu",
    "type1" : "Electric",
    "category" : "Mouse",
    "HP" : 128,
    "attack" : 60,
    "defense" : 25,
    "speed" : 50
    }

pokemon2 = {
    "name" : "Bulbasaur",
    "type1" : "Grass",
    "category" : "Seed",
    "HP" : 130,
    "attack" : 40,
    "defense" : 20,
    "speed" : 10
    }

wild_pokemon = {
    "name" : "Psyduck",
    "type1" : "Water",
    "category" : "Duck",
    "HP" : 140,
    "attack" : 55,
    "defense" : 10,
    "speed" : 51
    }

my_pokemon = [pokemon1, pokemon2]
active_poke = 0

print(f'A wild {wild_pokemon["name"]} appears!')

# while loops will continue until the condition becomes false...
while(wild_pokemon["HP"] > 0):  # <-- Note: Isaac had a cool idea to use a variable to keep game active/inactive...
    # choose between fight(f), other pokemon(o), or run(r)
    choice = input("Command? [f]ight, switch [o]ut, or [r]un>")

    # Thanks Ashley!
    if (choice == 'r'):
        #running away!
        print ("You got away safely!")
    elif (choice == 'o'):
        #switch betweeen 0 and 1 (for our active pokemon)
        if (active_poke == 0):
            active_poke = 1
        else:
            active_poke = 0
        print(f"Active pokemon: {my_pokemon[active_poke]}")
    else: # default choice... # Thanks, Isaac!
        # attack stuff
        # select move (between attack, and special)
        atk_cmd = input("Select [a]ttack or [s]pecial>")

        # faster pokemon attacks first
        if (my_pokemon[active_poke]["speed"] < wild_pokemon["speed"]):  # Thanks Ashley!
            # wild pokemon attacks first!  # Thanks Nathan!
            wild_damage = wild_pokemon["attack"] - my_pokemon[active_poke]["defense"]
            my_pokemon[active_poke]["HP"] = my_pokemon[active_poke]["HP"] - wild_damage
            print(f'{wild_pokemon["name"]} attacks {my_pokemon[active_poke]["name"]}!')
            print(f'{my_pokemon[active_poke]["name"]} takes {wild_damage} damage!  {my_pokemon[active_poke]["HP"]} remaining.')
        if (atk_cmd == 'a'): #Thanks Madison!
            # my attack - their defense = damage
            # opponent health = hp - damage
            damage = my_pokemon[active_poke]["attack"] - wild_pokemon["defense"]
            wild_pokemon["HP"] = wild_pokemon["HP"] - damage
            print()
            print(f'{my_pokemon[active_poke]["name"]} attacks {wild_pokemon["name"]}!')
            print(f'{wild_pokemon["name"]} has {wild_pokemon["HP"]} health remaining.')

            if (wild_pokemon["HP"] <= 0):
                print(f'{wild_pokemon["name"]} has feinted!')

# print some results

