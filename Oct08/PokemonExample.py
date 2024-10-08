'''
Pokemon example!

Special Thanks: Madison, Isaac
'''

def fight(poke1, poke2):
    print(f"{poke1['name']} fights {poke2['name']}!")

    winner = None
    if poke1["attack"] > poke2["defense"]:
        winner = poke1["name"]
    elif poke2["attack"] > poke1["defense"]:
        winner = poke2["name"]
    else:
        winner = "Nobody :("

    return winner

def main():
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

    winner = fight(pokemon1, pokemon2)
    print(f"They fought and the winner was {winner}")
    
main()
