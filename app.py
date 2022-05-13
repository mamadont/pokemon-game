from models.pokemon import Pokemon

moves = [
    {
        "name": "Move 1",
        "type": "Fire",
        "minimum_damage": 5,
        "maximum_damage": 10
    },
    {
        "name": "Move 2",
        "type": "Fire",
        "minimum_damage": 3,
        "maximum_damage": 7
    },
    {
        "name": "Move 3",
        "type": "Fire",
        "minimum_damage": 8,
        "maximum_damage": 20
    },

]

pokemon = Pokemon("Pokemon 1", "Fire", 40, moves)


new_move = {
        "name": "Move 4",
        "type": "Fire",
        "minimum_damage": 8,
        "maximum_damage": 20
    }

print(pokemon.attack())

