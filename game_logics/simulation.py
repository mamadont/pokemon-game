from models.cpu_user import CPU_User


def simulate(cpu_1: CPU_User, cpu_2: CPU_User):
    while (len(cpu_1._team) > 0) and (len(cpu_2._team) > 0):

        # Select random pokemon
        cpu_attacker = cpu_1.select_pokemon()

        # Choose an attack
        cpu_damage = cpu_attacker.select_attack()

        # Choose a one of player 2's pokemon to attack
        cpu_2_victim = cpu_attacker.select_victim(cpu_2)

        cpu_2_victim._health_points = cpu_2_victim._health_points - cpu_damage

        print(
            f"cpu_1's {cpu_2_victim._name} lost {cpu_damage} health points. Current HP: {cpu_2_victim._health_points}")

        # If the hp is less than or equal to 0 delete that pokemon from the team
        if cpu_2_victim.is_dead():
            cpu_2.remove_from_team(cpu_2_victim)
            print(f"cpu_1's {cpu_2_victim.name} has fainted")

        # Check to see if there is a winner
        if len(cpu_2._team) == 0:
            print(f"{cpu_1._name} has won!")
            return

        # Select random pokemon
        cpu_attacker = cpu_2.select_pokemon()

        # Choose an attack
        cpu_damage = cpu_attacker.select_attack()

        # Choose a one of player 1's pokemon to attack
        cpu_1_victim = cpu_attacker.select_victim(cpu_1)

        cpu_1_victim._health_points = cpu_1_victim._health_points - cpu_damage

        print(
            f"cpu_1's {cpu_1_victim._name} lost {cpu_damage} health points. Current HP: {cpu_1_victim._health_points}")

        # If the hp is less than or equal to 0 delete that pokemon from the team
        if cpu_1_victim.is_dead():
            cpu_1.remove_from_team(cpu_1_victim)
            print(f"cpu_1's {cpu_1_victim.name} has fainted")

        # Check to see if there is a winner
        if len(cpu_1._team) == 0:
            print(f"{cpu_2._name} has won!")
            return
