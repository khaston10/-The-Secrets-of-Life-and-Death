from Humanoid import *


class Dwarf(Humanoid):
    """
    This class represents a type of humanoid, a dwarf. It is a child class of Humanoid.
    """
    def __init__(self, name="no_name", gender="male", health=100, items=[], visibility=100, player=False, player_id=0):
        super().__init__(name, gender, health, items, visibility, player, player_id)

        self.description = self.name + " is a dwarf."


class Goblin(Humanoid):
    """
    This class represents a type of humanoid, a goblin. It is a child class of Humanoid.
    """
    def __init__(self, name="no_name", gender="male", health=100, items=[], visibility=100, player=False, player_id=0):
        super().__init__(name, gender, health, items, visibility, player, player_id)

        self.description = self.name + " is a goblin."