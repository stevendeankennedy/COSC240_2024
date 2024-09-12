'''
Sample program about types.  Let's go Pokemon!
The Class and me
Sept 12, 2024
'''

# Making a pokedex!

# We'll use a Dictionary for Pokemon
pokemon1 = {
    "name" : "Pikachu",
    "type1" : "Electric",
    "category" : "Mouse",
    "HP" : 128,
    "attack" : 60
    }

pokemon2 = {
    "name" : "Bulbasaur",
    "type1" : "Grass",
    "category" : "Seed",
    "HP" : 130,
    "attack" : 40
    }

pokemon3 = {
    "name" : "Psyduck",
    "type1" : "Water",
    "category" : "Duck",
    "HP" : 140,
    "attack" : 55
    }

# The list (Pokedex is a list)
pokedex = [pokemon1, pokemon2, pokemon3]

print("Please add a new Pokemon!")
name = input("Name>")
type1 = input("Type1>")
cat = input("Category>")
hp = int(input("HP>"))
atk = int(input("Attack>"))

# make the new Pokemon
pokemon4 = {
    "name": name,
    "type1": type1,
    "category": cat,
    "HP": hp,
    "Attack": atk}
pokedex.append(pokemon4)

print(f"Oh!  What's happening?  {pokedex[0]['name']} is evolving!")
pokedex[0]["name"] = "Raichu"
pokedex[0]["HP"] = pokedex[0]["HP"] * 2
pokedex[0]["attack"] = pokedex[0]["attack"] + 100


print(pokedex)
