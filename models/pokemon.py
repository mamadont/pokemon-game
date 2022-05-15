import random

class Pokemon:
    def __init__(self, name, type, health_points, moves):
        self._name = name 
        self._type = type
        self._health_points = health_points
        self._moves = moves

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return self._type
    
    @property
    def health_points(self):
        return self._health_points
    
    @health_points.setter
    def health_points(self, health_points):
        self._health_points = health_points

    @property
    def moves(self):
        return self._moves

    def add_move(self, move):
        if (len(self._moves) >= 5):
            print("Cannot add anymore moves")

        self._moves.append(move)
                
    def delete_move(self):
        self.list_moves()
        index =  int(input("Select a move number to delete:")) - 1
        del self._moves[index]

    def list_moves(self):
        count = 1
        for move in self._moves:
            print(str(count) + ") " + move["name"])
            count = count + 1

    def attack(self):
        self.list_moves()
        move = int(input("Please select a move number: "))
        move = self._moves[move - 1] 
        return random.randint(move["minimum_damage"], move["maximum_damage"])
        