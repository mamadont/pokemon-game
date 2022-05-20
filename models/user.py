class User:
    def __init__(self, name, team):
        self._name = name
        self._team = team

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, team):
        self._team = team

    def list_team(self):
        count = 1
        for member in self._team:
            print(f"{count}) {member.name}")
            count = count + 1
    
    def add_to_team(self, pokemon):
        if len(self._team) >= 3:
            print("Team is already at max capacity!") 
        self._team.append(pokemon)
    
    def remove_from_team(self, cpu_pokemon):
        count = 0
        for pokemon in self._team:
            if pokemon.name == cpu_pokemon.name:
                del self._team[count]
            count = count + 1
    
    def select_attack(self):
        self.list_team()
        index = int(input("Please select a pokemon to attack with: "))
        pokemon = self._team[index]        
        damage = pokemon.attack()
        return damage
    
    def select_pokemon(self):
        self.list_team()
        index = int(input("Pick a pokemon to attack with: "))
        return self._team[index - 1]
    
    def select_cpu_victim(self, cpu):
        cpu.list_team()
        index = int(input("Select a pokemon to attack"))
        return cpu._team[index - 1]
