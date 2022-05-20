from models.user import User
from models.cpu_user import CPU_User

def play_game(user: User, cpu: CPU_User):
    while (len(user._team) > 0) and (len(cpu._team) > 0):

        # Ask player 1 to choose a pokemon to attack with
        user_attacker = user.select_pokemon()

        # Choose an attack
        move = user_attacker.attack()

        # Choose a one of player 2's pokemon to attack #fix this
        cpu_victim = user.select_cpu_victim(cpu)

        # Deduct health points
        cpu_victim._health_points = cpu_victim._health_points - move

        print(
            f"CPU's {cpu_victim._name} lost {move} health points. Current HP: {cpu_victim._health_points} ")

        # If the hp is less than or equal to 0 delete that pokemon from the team
        if cpu_victim.is_dead():
            cpu.remove_from_team(cpu_victim)
            print(f"CPU's {cpu_victim.name} has fainted")

        if len(cpu._team) == 0:
            print(f"{user._name} has won!")
            return

        # Select random pokemon
        cpu_attacker = cpu.select_pokemon()

        # Choose an attack
        cpu_damage = cpu_attacker.select_attack()

        # Choose a one of player 1's pokemon to attack
        user_victim = cpu_attacker.select_victim(user)

        user_victim._health_points = user_victim._health_points - cpu_damage

        print(
            f"User's {user_victim._name} lost {cpu_damage} health points. Current HP: {user_victim._health_points}")

        # If the hp is less than or equal to 0 delete that pokemon from the team
        if user_victim.is_dead():
            user.remove_from_team(user_victim)
            print(f"User's {user_victim.name} has fainted")

        # Check to see if there is a winner
        if len(user._team) == 0:
            print(f"{cpu._name} has won!")
            return
