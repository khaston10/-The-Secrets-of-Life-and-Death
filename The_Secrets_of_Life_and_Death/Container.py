class Container:
    """
    This class represents a container. The object that can contain items.
    """
    def __init__(self, description="container", material="oak", condition="Weak", capacity=5, is_open=False,
                 is_locked=False):
        self.description = description
        self.material = material
        self.condition = condition
        self.capacity = capacity
        self.is_open = is_open  # A container must be open for a player to look or take.
        self.is_locked = is_locked  # A container must be unlocked for it to be opened.
        self.contents = []

    def get_description(self):
        """
        This function returns a string that describes the item.
        :return: String.
        """
        if self.is_open:
            description = ""
            description += self.condition + " " + self.material + " " + self.description + ". "
            description += " It contains: "
            count = 0
            for item in self.contents:
                count += 1
                if count < len(self.contents):
                    description += "a " + item.get_description() + ", "
                else:
                    description += "a " +item.get_description() + "."
            return description
        else:
            description = ""
            description += self.condition + " " + self.material + " " + self.description + ". It is closed."
            return description

    def open_container(self):
        """
        Opens the container if it is not locked.
        :return: None
        """
        if not self.is_locked:
            self.is_open = True

    def close_container(self):
        """
        Closes container.
        :return: None
        """
        self.is_open = False

    def add_item(self, item):
        """
        This function adds an item into the container, provided the container is not full, and it is open.
        :param item: Instance of item class.
        :return: True if item was added successfully. False otherwise.
        """
        if len(self.contents) < self.capacity and self.is_open:
            self.contents.append(item)
            return True
        else:
            return False

    def remove_item(self, item):
        """
        Removes an item from the container, provided the item exits in the container and container is open.
        :param item: Instance of item class.
        :return: True if the item is successfully removed. False otherwise.
        """
        if item in self.contents and self.is_open:
            self.contents.remove(item)
            return True
        else:
            return False

