
class Humanoid:
    """
    This class represents a humanoid.
    """
    def __init__(self, name="no_name", gender="male", health=100, items=[], visibility=100, player=False):
        self.name = name
        self.gender = gender
        self.health = health
        self.items = items
        self.visibility = visibility
        self.description = self.name + " is a humanoid."

    def get_description(self):
        """
        This function returns a string that describes the humanoid.
        :return: string
        """
        return self.description

    def go(self, location, mode="walk"):
        """
        This function moves the humanoid to a different location if possible.
        :param location: An instance of the location class.
        :param mode: A string that describes how the humanoid wants to travel. Acceptable modes: [walk, sneak, tbd...]
        :return: true if the humanoid was successfully moved, and False if the move was not accomplished.
        """
        pass

    def get_list_of_items(self):
        """
        This function returns the list of items the humanoid has in their inventory.
        :return: List of items
        """
        return self.items

