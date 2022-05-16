import imp
from models.game import Game

class PVC(Game):

    def play_game(self):
        while (len(self._player1._team) > 0) or (len(self._player2._team) > 0):
            # Ask player 1 to choose a pokemon to attack with 
            self._player1.list_team()
            idx1 = int(input("Pick a pokemon to attack with: "))
            attacker = self._player1._team[idx1]

            # Choose an attack
            move = attacker.attack()

            # Choose a one of player 2's pokemon to attack
            self._player2.list_team()
            idx2 = int(input("Choose pokemon to attack: "))
            victim = self._player2.team[idx2]

            victim._health_points = victim._health_points - move

            if victim.victim._health_points <= 0:
                print(f"{victim.name} has fainted")

            # If the hp is less than or equal to 0 delete that pokemon from the team
            pass