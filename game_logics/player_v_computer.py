from models.user import User
import random 

def play_game(player1: User, player2: User):
    while (len(player1._team) > 0) and (len(player2._team) > 0):

        # Ask player 1 to choose a pokemon to attack with
        player1.list_team()
        attacker_index = int(input("Pick a pokemon to attack with: "))
        attacker = player1._team[attacker_index]

        # Choose an attack
        move = attacker.attack()

        # Choose a one of player 2's pokemon to attack
        player2.list_team()
        victim_index = int(input("Choose pokemon to attack: "))
        victim = player2._team[victim_index]

        victim._health_points = victim._health_points - move

        print(f"{victim._name} lost {move} health points. Health Points: {victim._health_points}")

        # If the hp is less than or equal to 0 delete that pokemon from the team
        if victim._health_points <= 0:
            del player2._team[victim_index]
            print(f"{victim.name} has fainted")

        # Select random pokemon
        attacker_index = random.randint(0,len(player2._team)-1)
        attacker = player2._team[attacker_index]

        # Choose an attack
        move_index = random.randint(0,2)
        cpu_damage = random.randint(attacker._moves[move_index]["minimum_damage"], attacker._moves[move_index]["maximum_damage"]) 
        
        # Choose a one of player 2's pokemon to attack
        victim_index = random.randint(0,2)
        victim = player2._team[victim_index]

        victim._health_points = victim._health_points - cpu_damage

        print(f"{victim._name} lost {cpu_damage} health points. Health Points: {victim._health_points}")

        # If the hp is less than or equal to 0 delete that pokemon from the team
        if victim._health_points <= 0:
            del player1._team[victim_index]
            print(f"{victim.name} has fainted")

        # Check to see if there is a winner
        if len(player1._team) == 0:
            print(f"{player2._name} has won!")

        if len(player2._team) == 0:
            print(f"{player1._name} has won!")
