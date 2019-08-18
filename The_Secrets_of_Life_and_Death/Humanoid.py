from Location import Location
from LocationTypes import *

class Humanoid:
    """
    This class represents a humanoid.
    """
    def __init__(self, name="no_name", gender="male", mood="content", health=100, visibility=100, player=False):
        self.name = name
        self.gender = gender
        self.mood = mood
        self.health = health
        self.backpack = []
        self.left_hand = []
        self.right_hand = []
        self.visibility = visibility
        self.description = self.name + " is a humanoid."
        self.player = player
        self.carrying_capacity = 5
        # This attribute is only initialized after rooms have been created. It is an instance of a location.
        self.room = ""

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
        description += self.room.get_description_of_containers_in_room()
        description += self.room.get_description_of_exits()
        return description

    def look_at_character(self, name):
        """
        This function returns a description of the character if he/she is in the same room.
        :param name: name of humanoid object
        :return: string
        """
        description = ""

        description += self.get_description() + "\n"
        description += self.name + "'s right hand: " + self.get_description_of_item_in_right_hand() + "\n"
        description += self.name + "'s Left hand: " + self.get_description_of_item_in_left_hand() + "\n"
        description += self.name + "'s backpack: " + self.get_description_of_items_in_backpack()
        return description


    def get_description_of_items_in_backpack(self):
        """
        This function returns a description of items the humanoid has.
        :return: List of items
        """
        description = ""
        weapons = ""
        if len(self.backpack) == 0:
            description = self.name + " has no items."
            return description
        elif len(self.backpack) >= 1:
            count = 0
            for item in self.backpack:
                if count < len(self.backpack):
                    description += "a " + str(item.get_description()) + ", "
                else:
                    description += "a " + str(item.get_description()) + "."
            return description

    def get_description_of_item_in_right_hand(self):
        """
        Returns a string of item held by humanoid in right hand.
        :return: String
        """
        description = "empty"

        if len(self.right_hand) != 0:
            description = self.right_hand[0].get_description()
            return description
        else:
            return description

    def get_description_of_item_in_left_hand(self):
        """
        Returns a string of item held by humanoid in left hand.
        :return: String
        """
        description = "empty"

        if len(self.left_hand) != 0:
            description = self.left_hand[0].get_description()
            return description
        else:
            return description

