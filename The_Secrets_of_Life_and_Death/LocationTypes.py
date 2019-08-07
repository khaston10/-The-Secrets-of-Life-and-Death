from Location import Location

class Small_Room(Location):
    """
    This class represents a type of humanoid, a dwarf. It is a child class of Humanoid.
    """
    def __init__(self, name="no_name", description="This is a small room.", items=[], characters=[], player_ids=[],
                 exits=[], light_level=100, room_capacity=10):
        super().__init__(name, description, items, characters, player_ids, exits, light_level, room_capacity)


class Big_Room(Location):
    """
    This class represents a type of humanoid, a dwarf. It is a child class of Humanoid.
    """
    def __init__(self, name="no_name", description="This is a big room.", items=[],characters=[],  player_ids=[],
                 exits=[], light_level=100, room_capacity=10):
        super().__init__(name, description, items, characters, player_ids, exits, light_level, room_capacity)

