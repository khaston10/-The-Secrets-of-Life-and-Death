from HumanoidTypes import *
from LocationTypes import *
from ItemTypes import *
from Container import Container
from Location import Location
from Humanoid import Humanoid
from AcceptableAnswers import *
import random
from Materials import *
from HumanoidMoods import *
from HumanoidNames import *
from MapSettings import *


def question(question, answers=acceptable_answers):
    """
    To avoid situations where the user inputs an inappropriate string.
    :param question: string
    :param acceptable_answers: list of acceptable answers. Each element should be a lowercase string.
    :return: String, user's acceptable answer.
    """
    not_acceptable_answer = True
    while not_acceptable_answer:
        temp_answer = input(question).lower()
        for cmd_list in answers:
            if temp_answer in cmd_list:
                not_acceptable_answer = False
    return temp_answer


def create_humanoid(type, name, gender, mood, player):
    """
    This function creates a humanoid of type, and returns it.
    :param type: string, currently it can be "dwarf" or "goblin"
    :param name: string
    :param gender: string, currently it can be "male" or "female"
    :param mood: string, humanoids mood.
    :return: Humanoid object.
    """
    if type == "dwarf" or type == "Dwarf":
        return Dwarf(name=name, gender=gender, mood=mood, player=player)

    elif type == "goblin" or type == "Goblin":
        return Goblin(name=name, gender=gender, mood=mood, player=player)


def player_take_item_from_container(player):
    """
    This method handles a player trying to take an item from container.
    :return: None
    """
    if len(player.room.containers) == 0:
        print("There are no containers in this room.")
    elif len(player.room.containers) == 1:
        if player.room.containers[0].is_open and len(player.room.containers[0].contents) != 0:
            options = ""
            option_number = []
            for i in range(len(player.room.containers[0].contents)):
                options += "[" + str(i) + "] " + player.room.containers[0].contents[i].get_description() + "\n"
                option_number.append(str(i))
            print(options)
            num = question("Which item would you like to take?", option_number)
            if not player.right_hand:  # is right hand empty?
                item = player.room.containers[0].contents[int(num)]
                player.room.containers[0].remove_item(item)
                player.right_hand.append(item)
                print("Your grab the " + item.get_description() + " with your right hand.\n")
            elif len(player.left_hand) < 1:
                item = player.room.containers[0].contents[int(num)]
                player.room.containers[0].remove_item(item)
                player.left_hand.append(item)
                print("Your grab the " + item.get_description() + " with your left hand.\n")
            else:
                print("Your hands are full.")
        elif len(player.room.containers[0].contents) == 0:
            print("There are no items in container.")
        else:
            print("The container is not open.")
    else:
        options = ""
        option_number = []
        for i in range(len(player.room.containers)):
            options += "[" + str(i) + "] " + player.room.containers[i].get_description() + "\n"
            option_number.append(str(i))
        print(options)
        num_container = question("From which container?", option_number)
        if player.room.containers[int(num_container)].is_open and len(player.room.containers[int(num_container)].contents):
            options = ""
            option_number = []
            for i in range(len(player.room.containers[int(num_container)].contents)):
                options += "[" + str(i) + "] " + player.room.containers[int(num_container)].contents[i].get_description() + "\n"
                option_number.append(str(i))
            print(options)
            num = question("Which item would you like to take?", option_number)
            if len(player.right_hand) < 1:
                item = player.room.containers[int(num_container)].contents[int(num)]
                player.room.containers[int(num_container)].remove_item(item)
                player.right_hand.append(item)
                print("Your grab the " + item.get_description() + " with your right hand.\n")
            elif len(player.left_hand) < 1:
                item = player.room.containers[int(num_container)].contents[int(num)]
                player.room.containers[int(num_container)].remove_item(item)
                player.left_hand.append(item)
                print("Your grab the " + item.get_description() + " with your left hand.\n")
            else:
                print("Your hands are full.")
        elif len(player.room.containers[int(num_container)].contents) == 0:
            print("There are no items in container.")
        else:
            print("The container is not open.")


def player_put_item_in_container(player):
    """
    This method handles a player trying to put an item into a container.
    :return: None
    """
    if len(player.room.containers) == 0:
        print("There are no containers in this room.")
    elif len(player.room.containers) == 1:
        if player.room.containers[0].is_open and (player.left_hand or player.right_hand):
            options = ""
            option_number = []
            if player.left_hand and player.right_hand:
                options += "[0]" + player.left_hand[0].get_description() + "\n"
                options += "[1]" + player.right_hand[0].get_description() + "\n"
                option_number = ["0", "1"]
                print(options)
                num = question("Which item would you like to put in the container?", option_number)
                if num == '0':
                    item = player.left_hand[0]
                    player.left_hand.remove(item)
                    player.room.containers[0].add_item(item)
                    print("The " + item.get_description() + " has been added to the container. \n")
                else:
                    item = player.right_hand[0]
                    player.right_hand.remove(item)
                    player.room.containers[0].add_item(item)
                    print("The " + item.get_description() + " has been added to the container. \n")
            elif player.left_hand:
                item = player.left_hand[0]
                player.left_hand.remove(item)
                player.room.containers[0].add_item(item)
                print("The " + item.get_description() + " has been added to the container. \n")
            else:
                item = player.right_hand[0]
                player.right_hand.remove(item)
                player.room.containers[0].add_item(item)
                print("The " + item.get_description() + " has been added to the container. \n")

        elif player.room.containers[0].is_open:
            print("You are not holding anything.")
        else:
            print("The container is not open.")
    else:
        options = ""
        option_number = []
        for i in range(len(player.room.containers)):
            options += "[" + str(i) + "] " + player.room.containers[i].get_description() + "\n"
            option_number.append(str(i))
        print(options)
        num_container = question("In which container?", option_number)
        if player.room.containers[int(num_container)].is_open and (player.left_hand or player.right_hand):
            options = ""
            option_number = []
            if player.left_hand and player.right_hand:
                options += "[0]" + player.left_hand[0].get_description() + "\n"
                options += "[1]" + player.right_hand[0].get_description() + "\n"
                option_number = ["0", "1"]
                print(options)
                num = question("Which item would you like to put in the container?", option_number)
                if num == '0':
                    item = player.left_hand[0]
                    player.left_hand.remove(item)
                    player.room.containers[int(num_container)].add_item(item)
                    print("The " + item.get_description() + " has been added to the container. \n")
                else:
                    item = player.right_hand[0]
                    player.right_hand.remove(item)
                    player.room.containers[int(num_container)].add_item(item)
                    print("The " + item.get_description() + " has been added to the container. \n")
            elif player.left_hand:
                item = player.left_hand[0]
                player.left_hand.remove(item)
                player.room.containers[int(num_container)].add_item(item)
                print("The " + item.get_description() + " has been added to the container. \n")

            else:
                item = player.right_hand[0]
                player.right_hand.remove(item)
                player.room.containers[int(num_container)].add_item(item)
                print("The " + item.get_description() + " has been added to the container. \n")
        elif player.room.containers[int(num_container)].is_open:
            print("You are not holding anything.")
        else:
            print("The container is not open.")


def player_put_item_in_backpack(player):
    """
    Puts item from player's hand into backpack.
    :param player: instance of humanoid.
    :return: None
    """
    if not player.right_hand and not player.left_hand:
        print("There is nothing to put in backpack.")

    elif not player.left_hand:
        item = player.right_hand[0]
        player.right_hand.remove(item)
        player.backpack.append(item)
        print("The " + item.get_description() + " has been added to your backpack.")

    elif not player.right_hand:
        item = player.left_hand[0]
        player.left_hand.remove(item)
        player.backpack.append(item)
        print("The " + item.get_description() + " has been added to your backpack.")

    else:
        item_1 = player.right_hand[0]
        player.right_hand.remove(item_1)
        item_2 = player.left_hand[0]
        player.left_hand.remove(item_2)
        player.backpack.append(item_1)
        player.backpack.append(item_2)
        print("The " + item_1.get_description() + " and " + item_2.get_description()
              + " have been added to your backpack.")


def player_take_item_from_backpack(player):
    """
    Takes item from back pack and places it in players hand. The right hand fills first and then the left.
    :param player: instance of humanoid.
    :return: None
    """
    if len(player.backpack) == 0:
        print("No items in back pack.")
    elif len(player.backpack) == 1:
        if len(player.right_hand) == 0:
            item = player.backpack[0]
            player.right_hand.append(item)
            player.backpack.remove(item)
            print("Item has been added to your right hand.")
        elif len(player.left_hand) == 0:
            item = player.backpack[0]
            player.left_hand.append(item)
            player.backpack.remove(item)
            print("Item has been added to your left hand.")
        else:
            print("You can not grab item because your hands are full.")
    else:
        options = ""
        option_number = []
        for i in range(len(player.backpack)):
            options += "[" + str(i) + "] " + player.backpack[i].get_description() + "\n"
            option_number.append(str(i))
        print(options)
        num_item = question("Which item?", option_number)
        if len(player.right_hand) == 0:
            item = player.backpack[int(num_item)]
            player.right_hand.append(item)
            player.backpack.remove(item)
            print("Item has been added to your right hand.")
        elif len(player.left_hand) == 0:
            item = player.backpack[int(num_item)]
            player.left_hand.append(item)
            player.backpack.remove(item)
            print("Item has been added to your left hand.")
        else:
            print("You can not grab item because your hands are full.")


def player_close_container(player):
    """
    Handles player closing container.
    :param player: Instance of player.
    :return: None
    """
    if len(player.room.containers) == 1:
        if player.room.containers[0].is_open:
            player.room.containers[0].close_container()
            print("The container has been closed.")
            time = "move forward"
        else:
            print("This container is already closed.")
    elif len(player.room.containers) > 1:
        options = ""
        option_number = []
        for i in range(len(player.room.containers)):
            options += "[" + str(i) + "] " + player.room.containers[i].get_description() + "\n"
            option_number.append(str(i))
        print(options)
        num = question("Which container do you want to close?", option_number)
        if player.room.containers[int(num)].is_open:
            player.room.containers[int(num)].close_container()
            print("The container has been closed.")
            time = "move forward"
        else:
            print("This container is already closed.")
    else:
        print("There are no containers in this room.")


def player_open_container(player):
    """
    Handles player opening container.
    :param player: Instance of player.
    :return: None
    """
    if len(player.room.containers) == 1:
        if not player.room.containers[0].is_open:
            if not player.room.containers[0].is_locked:
                player.room.containers[0].open_container()
                print("The container has been opened.")
            else:
                print("Container is locked.")
        else:
            print("This container is already open.")
    elif len(player.room.containers) > 1:
        options = ""
        option_number = []
        for i in range(len(player.room.containers)):
            options += "[" + str(i) + "] " + player.room.containers[i].get_description() + "\n"
            option_number.append(str(i))
        print(options)
        num = question("Which container do you want to open?", option_number)
        if not player.room.containers[int(num)].is_open:
            if not player.room.containers[int(num)].is_locked:
                player.room.containers[int(num)].open_container()
                print("The container has been opened.")
            else:
                print("Container is locked.")
        else:
            print("This container is already open.")
    else:
        print("There are no containers in this room.")


def player_pick_lock(player):
    """
    Handles player picking lock on container. Player needs to have picks in a hand to pick a lock.
    :param player: Instance of player.
    :return: True if a lock has be picked successfully.
    """
    if len(player.room.containers) == 1:
        if player.room.containers[0].is_locked:
            if len(player.right_hand) == 1:
                if player.right_hand[0].item_type == "picks":
                    if player.right_hand[0].condition != "broken":
                        player.room.containers[0].pick_lock()
                        check_to_see_if_item_should_age(player.right_hand[0], probability_that_item_will_age,
                                                        item_condition)
                        print("The lock has been picked.")
                        return True
                    else:
                        print("These lock picks are broken.")
                        return False
                if player.left_hand[0].item_type == "picks":
                    if player.left_hand[0].condition != "broken":
                        player.room.containers[0].pick_lock()
                        check_to_see_if_item_should_age(player.left_hand[0], probability_that_item_will_age,
                                                        item_condition)
                        print("The lock has been picked.")
                        return True
                    else:
                        print("These lock picks are broken.")
                        return False
                else:
                    print("You have no lock picks equipped.")
                    return False
            else:
                print("You have no lock picks equipped.")
                return False
        else:
            print("The container is not locked.")
            return False
    elif len(player.room.containers) > 1:
        options = ""
        option_number = []
        for i in range(len(player.room.containers)):
            options += "[" + str(i) + "] " + player.room.containers[i].get_description() + "\n"
            option_number.append(str(i))
        print(options)
        num = question("Which lock do you want to pick?", option_number)
        if player.room.containers[int(num)].is_locked:
            if len(player.right_hand) == 1:
                if player.right_hand[0].item_type == "picks":
                    if player.right_hand[0].condition != "broken":
                        player.room.containers[int(num)].pick_lock()
                        check_to_see_if_item_should_age(player.right_hand[0], probability_that_item_will_age,
                                                        item_condition)
                        print("The lock has been picked.")
                        return True
                    else:
                        print("These lock picks are broken.")
                        return False
            if len(player.left_hand) == 1:
                if player.left_hand[0].item_type == "picks":
                    if player.left_hand[0].condition != "broken":
                        player.room.containers[int(num)].pick_lock()
                        check_to_see_if_item_should_age(player.left_hand[0], probability_that_item_will_age,
                                                        item_condition)
                        print("The lock has been picked.")
                        return True
                    else:
                        print("These lock picks are broken.")
                        return False
            else:
                print("You have no lock picks equipped.")
                return False
        else:
            print("The container is not locked.")
            return False
    else:
        print("There are no locks to pick.")
        return False


def check_to_see_if_item_should_age(item, p_that_item_will_age, item_condition_list):
    """
    This function checks to see if an item should age when used based off the variable in map settings.
    :param item: An instance of the item class.
    :param p_that_item_will_age: An integer from the MapSetting script.
    :param item_condition_list: An list from the Materials script.
    :return: True if item should age. False if it should not.
    """
    condition = item.condition

    rand_num = random.randint(0, 100)
    if rand_num < p_that_item_will_age:
        if item_condition_list.index(condition) != len(item_condition_list) - 1:
            condition = item_condition_list[item_condition_list.index(condition) + 1]
            item.condition = condition
            return True
        else:
            return False
    else:
        return False


def get_humanoid_object_from_look_command(action, list_of_humanoids):
    """
    This function was created to keep the main game loop clean. It returns the humanoid object when player enters the
    command: look at 'humanoid's name'. The return for this function is typically passed into look_at_humanoid.
    :param action: String of the form, look at 'humanoid's name'
    :param list_of_humanoids: List of humanoids in game.
    :return: instance of the humanoid class.
    """
    humanoid_name = action[8:len(action)]
    list_of_humanoid_names = []

    for humanoid in list_of_humanoids:
        list_of_humanoid_names.append(humanoid.name.lower())

    if humanoid_name in list_of_humanoid_names:
        index = list_of_humanoid_names.index(humanoid_name)
        return list_of_humanoids[index]


def look_at_humanoid(humanoid):
    """
    Returns a detailed description of humaniod.
    :param humanoid: Instance of humanoid
    :return: String
    """
    return humanoid.look_at_character(humanoid.name)


def create_npcs(number_of_npcs, names, moods):
    """
    This function returns a list of humanoid objects, they will all have unique names.
    :param number_of_npcs: integer
    :return: list of non player characters
    """
    list_of_npcs = []

    for i in range(number_of_npcs):
        random_species = random.choice(["dwarf", "goblin"])
        random_name = random.choice(names[random_species])
        names[random_species].remove(random_name)
        random_mood = random.choice(moods)
        random_gender = random.choice(["male", "female"])
        list_of_npcs.append(create_humanoid(type=random_species, name=random_name, gender=random_gender,
                                            mood=random_mood, player=False))

    return list_of_npcs


def assign_npc_item(in_npc, type_of_item):
    """
    Assign items list of npcs.
    :param in_npc: A humanoid
    :param: type_of_item: String, this is a type of item. Acceptable items are "sword", "axe", "shield", "helmet".
    :return: None
    """
    condition = random.choice(item_condition)
    if type_of_item == "sword":
        material = select_random_material("metal")
        in_npc.backpack.append(Sword(assigned=True, material=material, condition=condition, item_type="sword"))

    elif type_of_item == "axe":
        material = select_random_material("metal")
        in_npc.backpack.append(Axe(assigned=True, material=material, condition=condition, item_type="axe"))

    elif type_of_item == "shield":
        material = select_random_material(random.choice(["wood", "metal"]))
        in_npc.backpack.append(Shield(assigned=True, material=material, condition=condition, item_type="shield"))

    elif type_of_item == "helmet":
        material = select_random_material("metal")
        in_npc.backpack.append(Helmet(assigned=True, material=material, condition=condition, item_type="helmet"))


def create_weapon(type_of_weapon, material, condition="new"):
    """
    This function creates a weapon.
    :param type_of_weapon: String. Acceptable types at this point are ["sword", "axe"]
    :param material: String. Acceptable types at this point are ["bronze", "copper", "silver" ,"iron"]
    :param condition: String. Acceptable condition at this point are ["broken", "used", "new"]
    :return: None
    """
    if type_of_weapon == "sword":
        sword = Sword(material=material, condition=condition, item_type="sword")
        return sword
    elif type_of_weapon == "axe":
        axe = Axe(material=material, condition=condition, item_type="axe")
        return axe


def create_armour(type_of_armour, material, condition="new"):
    """
    This function creates an item of armour.
    :param type_of_armour: String. Acceptable types at this point are ["shield", "helmet"]
    :param material: String. Acceptable types at this point are ["bronze", "copper", "silver" ,"iron"]
    :param condition: String. Acceptable condition at this point are ["broken", "used", "new"]
    :return: None
    """
    if type_of_armour == "shield":
        shield = Shield(material=material, condition=condition, item_type="shield")
        return shield
    elif type_of_armour == "helmet":
        helmet = Helmet(material=material, condition=condition, item_type="helmet")
        return helmet


def create_container(weapon_amt=0, armour_amt=0):
    """
    Creates a container and adds items. If no items are entered it will create an empty container.
    Can carry 5 items by default.
    :param weapon_amt: Integer, the amount of weapons to put in container.
    :param armour_amt: Integer, the amount of weapons to put in container.
    :return: container object
    """
    container = Container(material=random.choice(materials["wood"]), condition=random.choice(item_strength), capacity=5,
                          is_open=False, is_locked=False)

    list_of_items = []

    # Create random weapons.
    for i in range(weapon_amt):
        list_of_items.append(create_weapon(type_of_weapon=random.choice(["sword", "axe"]), material=random.choice(
            ["bronze", "copper", "silver", "iron"]), condition=random.choice(["broken", "used", "new"])))

    # Create random armour.
    for i in range(armour_amt):
        list_of_items.append(create_armour(type_of_armour=random.choice(["shield", "helmet"]), material=random.choice(
            ["bronze", "copper", "silver", "iron"]), condition=random.choice(["broken", "used", "new"])))

    # Add items to the container.
    container.is_open = True
    for item in list_of_items:
        container.add_item(item)
    container.is_open = False

    # Randomly assign some containers as locked.
    rand_num = random.randint(0, 100)
    if rand_num < probability_that_containers_will_be_locked:
        container.is_locked = True

    return container


def create_containers_with_random_items(number_of_containers):
    """
    Creates a list of containers filled with random items.
    :param number_of_containers: Integer, the amount o f containers to create.
    :return: list of containers.
    """
    list_of_containers = []
    for i in range(number_of_containers):
        list_of_containers.append(create_container(weapon_amt=3, armour_amt=0))

    return list_of_containers


def create_location(room_type):
    """
    This function creates one location based upon the type.
    :param type: String, the available types are ["small_room" "big_room"]
    :return: an istance of Location
    """
    if room_type == "small_room":
        room = Small_Room()

    elif room_type == "big_room":
        room = Big_Room()

    return room


def select_random_material(type_of_material):
    """

    :param type_of_material: String acceptable values are "metal", "wood", "fabric"
    :return: String of the type of fabric.
    """
    if type_of_material == "metal":
        material = random.choice(materials["metal"])
        return material
    elif type_of_material == "wood":
        material = random.choice(materials["wood"])
        return material


def print_list_of_items_in_rooms(list_of_rooms):
    """
    This function prints a list of items in each room.
    :param list_of_rooms: list of location objects
    :return: None
    """
    for room in list_of_rooms:
        print("The items in " + str(room) + ":")
        print(room.items)


def print_list_of_characters_in_rooms(list_of_rooms):
    """
    This function prints a list of characters in each room.
    :param list_of_rooms: list of location objects
    :return: None
    """
    for room in list_of_rooms:
        print("The characters in " + room.name + ":")
        for character in room.characters:
            print(character.name)


def print_game_information(list_of_rooms):
    """
    This function prints all game objects to screen.
    :param list_of_rooms: A list of location objects.
    :return:
    """
    for room in list_of_rooms:
        character_list = []
        for char in room.characters:
            character_list.append(char.name)
        print(room.name + "\n" + "Player names: " + str(character_list))
        for container in room.containers:
            print(container.get_description())


def print_help_menu():
    """
    This prints some helpful hints to screen.
    :return:
    """
    print("\n---------------------------------------------------------------------------------------------------------")
    print("OBJECTIVE:")
    print("The is a sandbox game, so you get to pick your own objective. Remember, you are in a necromancer's tower.\n")
    print("\nCOMMANDS:")
    print("go North")
    print("go East")
    print("go South")
    print("go West")
    print("look")
    print("look at 'character's name'")
    print("open container")
    print("close container")
    print("pick lock")
    print("take from container")
    print("put in container")
    print("take item from backpack")
    print("put item in backpack")
    print("help")
    print("---------------------------------------------------------------------------------------------------------\n")


def print_game_logo():
    """
    This function prints the game logo.
    :return: None
    """

    print("\n")
    print("----------------------------------------")
    print("| .---.                 .              |")
    print("| \___  ,-. ,-. ,-. ,-. |- ,-.         |")
    print("|     \ |-' |   |   |-' |  `-.         |")
    print("| `---' `-' `-' '   `-' `' `-'         |")
    print("|                                      |")
    print("|                                      |")
    print("|     ,_   .      ,_                   |")
    print("| ,-. |_   |    . |_ ,-.               |")
    print("| | | |    |    | |  |-'               |")
    print("| `-' |    `--' ' |  `-'               |")
    print("|     '           '                    |")
    print("|                                      |")
    print("|           .   .-,--.          .  .   |")
    print("| ,-. ,-. ,-|   ' |   \ ,-. ,-. |- |-. |")
    print("| ,-| | | | |   , |   / |-' ,-| |  | | |")
    print("| `-^ ' ' `-'   `-^--'  `-' `-^ `' ' ' |")
    print("----------------------------------------")
    print("\n")


def print_game_intro():
    """
    This function prints the game intro information.
    :return: None
    """

    print("\n---------------------------------------------------------------------------------------------------------")
    print("At last, your search is over! You found the infamous tower! Rumor has it, a necromancer resides here. \n"
          "Be on guard. You know what you are here to do, the time for action is nigh.")
    print("---------------------------------------------------------------------------------------------------------\n")


def initialize_player_settings():
    start_type = question("Quick Start: Q\nCustom Start: C \n", [["q", "c"]])
    if start_type == "c":
        humanoid_type = question("Do you want to be a dwarf or goblin?", [["dwarf", "goblin"]])
        name = input("What is your name?")
        gender = question("What is your gender?", [["male", "female"]])
        weapon = question("What type of weapon do you want? (sword, axe)?", [["sword", "axe"]])
        player = create_humanoid(humanoid_type, name, gender, mood=humanoid_moods[0], player=True)
        if weapon == "sword":
            player.backpack.append(Sword(assigned=True, item_type="sword", material="bronze", condition="new"))
        elif weapon == "axe":
            player.backpack.append(Axe(assigned=True, item_type="axe", material="bronze", condition="new"))
        player.backpack.append(Picks(assigned=True, item_type="lock-picks", material="steel", condition="new"))

    else:
        gender = random.choice(["male", "female"])
        humanoid_type = random.choice(["dwarf", "goblin"])
        name = random.choice(humanoid_names[humanoid_type])

        player = create_humanoid(humanoid_type, name + " Player", gender, mood=humanoid_moods[0], player=True)
        player.backpack.append(Picks(assigned=True, item_type="picks", material="steel", condition="new"))

    return player
