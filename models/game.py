from models.user import User

class Game:
    def __init__(self, player1: User, player2: User):
        self._player1 = player1
        self._player2 = player2
        self._winner = ""
        self._loser = ""
        self._round = 0

    @property
    def player1(self):
        return self._player1

    @player1.setter
    def player1(self, player):
        self._player1 = player

    @property
    def player2(self):
        return self._player2
        
    @player2.setter
    def player2(self, player):
        self._player2 = player
