from models.pokemon import Pokemon
from models.user import User
from game_logics.player_v_computer import play_game

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

pokemon1 = Pokemon("Pokemon 1", "Fire", 40, moves)
pokemon2 = Pokemon("Pokemon 2", "Water", 40, moves)
pokemon3 = Pokemon("Pokemon 3", "Grass", 40, moves)

team = [pokemon1, pokemon2, pokemon3]
team2 = [pokemon1, pokemon2, pokemon3]
user1 = User("Mamadou", team)
user2 = User("CPU", team2)

play_game(user1, user2)