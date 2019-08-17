class Location:
    """
    This class represents a location.
    """
    def __init__(self, name="no_name", description="This is a room.", light_level=100, room_capacity=20):
        self.name = name
        self.description = description
        self.items = []
        self.containers = []
        self.characters = []
        self.exits = {}  # This is a dictionary of the form {"location of exit": room}
        self.light_level = light_level
        self.room_Capacity = room_capacity
        self.coordinates = [0, 0]

    def get_description(self):
        """
        This function returns a string that describes the humanoid.
        :return: string
        """
        description = self.description + "\n"
        return description

    def get_description_of_characters_in_room(self):
        """
        This function returns a description of characters in room.
        :return: string
        """
        description = ""
        number_of_characters = len(self.characters)
        if number_of_characters == 1:
            description += "There is " + str(number_of_characters) + " humanoid in this room."
        elif number_of_characters != 1:
            description += "There are " + str(number_of_characters) + " humanoids in this room."
        for char in self.characters:
            description += "\n" + char.get_description()

        return description + "\n"

    def get_description_of_containers_in_room(self):
        """
        This function returns a description of containers in room.
        :return: string
        """
        description = ""
        number_of_containers = len(self.containers)
        if number_of_containers == 0:
            description += "There are no containers in this room."
        elif number_of_containers == 1:
            description += "There is " + str(number_of_containers) + " container in this room."
        else:
            description += "There are " + str(number_of_containers) + " containers in this room."
        for container in self.containers:
            description += "\n" + container.get_description()

        return description + "\n"

    def get_description_of_items_in_room(self):
        """
        This function returns a description of items in room.
        :return: string
        """
        description = ""
        for item in self.items:
            description += item

        return description + "\n"

    def get_description_of_exits(self):
        """
        This function returns a description of exits and where they are located.
        :return: string.
        """
        description = ""
        number_of_exits = len(self.exits)
        location_of_exits = []
        for key in self.exits:
            location_of_exits.append(key)
        if number_of_exits == 1:
            description += "There is 1 exit in the room.\n"
            description += "The exit is located " + str(location_of_exits)
        else:
            description += "There are " + str(number_of_exits) + " exits in this room.\n"
            description += "Exits are located " + str(location_of_exits)
        return description + "\n"

    def delete_character(self, character):
        """
        This function deletes a character from the room.
        :param character: A humanoid object.
        :return: True if the character was successfully deleted. False if not.
        """
        if character in self.characters:
            self.characters.remove(character)
            return True
        else:
            return False

    def add_character(self, character):
        """
        This function adds a character to the room.
        :param character: A humanoid object.
        :return: True if the character was successfully deleted. False if not.
        """
        if character not in self.characters:
            self.characters.append(character)
            return True
        else:
            return False

