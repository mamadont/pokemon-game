import random
from models.pokemon import Pokemon

class CPU_Pokemon(Pokemon):
    def __init__(self, id, name, type, health_points, moves):
        super().__init__(id, name, type, health_points, moves)

    def select_attack(self):
        index = random.randint(0, 2)
        return random.randint(self._moves[index]["minimum_damage"], self._moves[index]["maximum_damage"])

    def select_victim(self, user):
        index = random.randint(0, len(user._team)-1)
        return user._team[index]