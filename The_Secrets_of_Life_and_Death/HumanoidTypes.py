from Humanoid import *


class Dwarf(Humanoid):
    """
    This class represents a type of humanoid, a dwarf. It is a child class of Humanoid.
    """
    def __init__(self, name="no_name", gender="male", mood="content", health=100, visibility=100, player=False):
        super().__init__(name, gender, mood, health, visibility, player)

        self.description = self.name + " is a dwarf."


class Goblin(Humanoid):
    """
    This class represents a type of humanoid, a goblin. It is a child class of Humanoid.
    """
    def __init__(self, name="no_name", gender="male", mood="content", health=100, visibility=100, player=False):
        super().__init__(name, gender, mood, health, visibility, player)

        self.description = self.name + " is a goblin."
