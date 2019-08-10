
class Item:
    """
    This class represents all items a humanoid can carry.
    """
    def __init__(self, description="Default Item", assigned=False, item_type="no_type",
                 material="bronze", condition="new"):
        self.description = description
        self.assigned = assigned
        self.item_type = item_type
        self.material = material
        self.condition = condition

    def is_item_assigned(self):
        """
        This function returns True if the item belongs to someone.
        :return: Boolean
        """
        return self.assigned

    def get_description(self):
        """
        This function returns a string that describes the item.
        :return: String.
        """
        description = ""
        description += self.condition + " " + self.material + " " + self.item_type + " "
        return description

