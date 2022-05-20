import random
from models.user import User

class CPU_User(User):

    def select_pokemon(self):
        index = random.randint(0, len(self._team)-1)
        return self._team[index - 1]