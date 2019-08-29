from Item import Item


class Weapon(Item):
    def __int__(self, description="This is a weapon.", assigned=False, item_type="weapon",
                material="bronze", condition="new"):
        super().__init__(description, assigned, item_type, material, condition)

        self.description = description
        self.assigned = assigned
        self.attack_min = 1
        self.attack_max = 5
        self.health = 100


class Armour(Item):
    def __int__(self, description="This is a Shield.", assigned=False, item_type="shield",
                material="bronze", condition="new"):
        super().__init__(description, assigned, item_type, material, condition)

        self.description = description
        self.assigned = assigned
        self.item_type = item_type
        self.block_min = 5
        self.block_max = 50
        self.health = 100


class Sword(Weapon):
    def __int__(self, description="This is a sword.", assigned=False, item_type="sword",
                material="bronze", condition="new"):
        super().__init__(description, assigned, item_type, material, condition)

        self.description = description
        self.assigned = assigned
        self.item_type = item_type
        self.attack_min = 10
        self.attack_max = 50
        self.health = 100


class Axe(Weapon):
    def __int__(self, description="This is a Axe.", assigned=False, item_type="axe",
                material="bronze", condition="new"):
        super().__init__(description, assigned, item_type, material, condition)

        self.description = description
        self.assigned = assigned
        self.item_type = item_type
        self.attack_min = 5
        self.attack_max = 50
        self.health = 100


class Shield(Armour):
    def __int__(self, description="This is a Shield.", assigned=False, item_type="shield",
                material="bronze", condition="new"):
        super().__init__(description, assigned, item_type, material, condition)

        self.description = description
        self.assigned = assigned
        self.item_type = item_type
        self.block_min = 5
        self.block_max = 50
        self.health = 100


class Helmet(Armour):
    def __int__(self, description="This is a Helmet.", assigned=False, item_type="helmet",
                material="bronze", condition="new"):
        super().__init__(description, assigned, item_type, material, condition)

        self.description = description
        self.assigned = assigned
        self.item_type = item_type
        self.block_min = 5
        self.block_max = 50
        self.health = 100


class Picks(Item):
    def __int__(self, description="This is a set of lock picks.", assigned=False, item_type="picks",
                material="steel", condition="new"):
        super().__init__(description, assigned, item_type, material, condition)

        self.description = description
        self.assigned = assigned
        self.item_type = item_type


