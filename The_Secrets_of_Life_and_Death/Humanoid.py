from Location import Location
from LocationTypes import *

class Humanoid:
    """
    This class represents a humanoid.
    """
    def __init__(self, name="no_name", gender="male", health=100, items=[], visibility=100, player=False, player_id=0):
        self.name = name
        self.gender = gender
        self.health = health
        self.items = items
        self.visibility = visibility
        self.description = self.name + " is a humanoid."
        self.player = player
        # This attribute is only initialized after rooms have been created. It is an instance of a location.
        self.room = ""
        self.player_id=player_id

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
        # Update self.room
        self.room = location

    def look(self):
        """
        This function returns a description of what the humanoid can see.
        :return: string
        """
        description = ""
        description += "\n"
        description += self.room.get_description()
        description += self.room.get_description_of_characters_in_room()
        description += self.room.get_description_of_exits()
        return description

    def look_at_character(self, name):
        """
        This function returns a desrciption of the character if he/she is in the same room.
        :param name: name of humanoid object
        :return: string
        """
        description = ""
        list_of_characters = self.room.characters
        list_of_character_names = []
        for char in list_of_characters:
            list_of_character_names.append(char.name.lower())
        if name in list_of_character_names:
            index = list_of_character_names.index(name)
            description += list_of_characters[index].get_description() + "\n"
            description += list_of_characters[index].get_description_of_items() + "\n"
            return description
        else:
            description += name + " not found."
            return description



    def get_description_of_items(self):
        """
        This function returns a description of items the humanoid has.
        :return: List of items
        """
        description = ""
        if len(self.items) == 0:
            description = self.name + " has no items."
            return description
        elif len(self.items) == 1:
            pass
        else:
            pass

