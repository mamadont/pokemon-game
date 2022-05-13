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