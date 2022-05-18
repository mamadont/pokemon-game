from models.user import User
import random


def play_game(user: User, cpu: User):
    while (len(user._team) > 0) and (len(cpu._team) > 0):

        # Ask player 1 to choose a pokemon to attack with
        user.list_team()
        attacker_index = int(input("Pick a pokemon to attack with: "))
        user_attacker = user._team[attacker_index - 1]

        # Choose an attack
        move = user_attacker.attack()

        # Choose a one of player 2's pokemon to attack
        cpu.list_team()
        victim_index = int(input("Choose pokemon to attack: "))
        cpu_victim = cpu._team[victim_index - 1]

        cpu_victim._health_points = cpu_victim._health_points - move

        print(
            f"CPU's {cpu_victim._name} lost {move} health points. Health Points: {cpu_victim._health_points}")

        

        # If the hp is less than or equal to 0 delete that pokemon from the team
        if cpu_victim._health_points <= 0:
            cpu.remove_from_team(victim_index - 1)
            print(f"CPU's {cpu_victim.name} has fainted")

        if len(cpu._team) == 0:
            print(f"{user._name} has won!")
            return


        # Select random pokemon
        attacker_index = random.randint(0, len(cpu._team))
        cpu_attacker = cpu._team[attacker_index - 1]

        # Choose an attack
        move_index = random.randint(0, 2)
        cpu_damage = random.randint(
            cpu_attacker._moves[move_index]["minimum_damage"], cpu_attacker._moves[move_index]["maximum_damage"])

        # Choose a one of player 1's pokemon to attack
        victim_index = random.randint(0, len(user._team)-1)
        user_victim = user._team[victim_index]

        user_victim._health_points = user_victim._health_points - cpu_damage

        print(
            f"User's {user_victim._name} lost {cpu_damage} health points. Health Points: {user_victim._health_points}")

        # If the hp is less than or equal to 0 delete that pokemon from the team
        if user_victim._health_points <= 0:
            user.remove_from_team(victim_index)
            print(f"User's {user_victim.name} has fainted")

        # Check to see if there is a winner
        if len(user._team) == 0:
            print(f"{cpu._name} has won!")
            return
