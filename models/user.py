# TODO:
# Select an attack 

class User:
    def __init__(self, name, team):
        self._name = name
        self._team = team
        self._wins = 0 
        self._losses = 0

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
    
    def remove_from_team(self):
        self.list_team()
        index = int(input("Pick a member to remove: "))
        del self._team[index - 1]
    
    def select_attack(self):
        self.list_team()
        index = int(input("Please select a pokemon to attack with: "))
        pokemon = self._team[index]        
        damage = pokemon.attack()
        return damage
            
    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, count):
        self._wins = self._wins + count
        
    @property
    def losses(self):
         return self._losses
        
    @losses.setter
    def losses(self, count):
        self.losses = self.losses + count