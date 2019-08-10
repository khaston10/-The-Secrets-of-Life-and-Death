from HumanoidTypes import *
from LocationTypes import *
from ItemTypes import *
from Location import Location
from Humanoid import Humanoid
from AcceptableAnswers import *
import random


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


def create_humanoid(type, name, gender, player):
    """
    This function creates a humanoid of type, and returns it.
    :param type: string, currently it can be "dwarf" or "goblin"
    :param name: string
    :param gender: string, currently it can be "male" or "female"
    :return: Humanoid object.
    """
    if type == "dwarf" or type == "Dwarf":
        return Dwarf(name=name, gender=gender, player=player)

    elif type == "goblin" or type == "Goblin":
        return Goblin(name=name, gender=gender, player=player)


def create_npcs(number_of_npcs):
    """
    This function returns a list of humanoid objects, they will all have unique names.
    :param number_of_npcs: integer
    :return: list of non player characters
    """
    list_of_npcs = []
    names = {"dwarf": ["Thatmig", "Ostar", "Lokoki", "Graghik"], "goblin": ["Krasb", "Zruq", "Vrois", "Zex"]}

    for i in range(number_of_npcs):
        random_species = random.choice(["dwarf", "goblin"])
        random_name = random.choice(names[random_species])
        names[random_species].remove(random_name)
        random_gender = random.choice(["male", "female"])
        list_of_npcs.append(create_humanoid(type=random_species, name=random_name, gender=random_gender, player=False))

    return list_of_npcs


def assign_npc_item(in_npc, type_of_item):
    """
    Assign items list of npcs.
    :param in_npc: A humanoid
    :param: type_of_item: String, this is a type of item. Acceptable items are "sword", "axe", "shield".
    :return: None
    """
    if type_of_item == "sword":
        in_npc.items.append(Sword(assigned=True, material="bronze", condition="new", item_type="sword"))

    elif type_of_item == "axe":
        in_npc.items.append(Axe(assigned=True, material="bronze", condition="new", item_type="axe"))

    elif type_of_item == "shield":
        in_npc.items.append(Shield(assigned=True, material="bronze", condition="new", item_type="shield"))


def create_weapon(type_of_weapon, material, condition="new"):
    """
    This function creates a weapon.
    :param type_of_weapon: String. Acceptable types at this point are ["sword", "axe"]
    :param material: String. Acceptable types at this point are ["bronze", "copper", "silver" "iron"]
    :param condition: String. Acceptable condition at this point are ["broken", "used", "new"]
    :return: None
    """
    if type_of_weapon == "sword":
        sword = Sword(material=material, condition=condition, item_type="sword")
        return sword
    elif type_of_weapon == "axe":
        axe = Axe(material=material, condition=condition, item_type="axe")
        return axe


def create_location(type):
    """
    This function creates one location based upon the type.
    :param type: String, the available types are ["small_room" "big_room"]
    :return: an istance of Location
    """
    if type == "small_room":
        room = Small_Room()

    elif type == "big_room":
        room = Big_Room()

    return room


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


def print_help_menu():
    """
    This prints some helpful hints to screen.
    :return:
    """
    print("\n---------------------------------------------------------------------------------------------------------")
    print("OBJECTIVE:")
    print("The is a sandbox game, so you get to pick your own objective. Remember, you are in a necromancer's tower.\n")
    print("\nCOMMANDS:")
    print("go to room on right")
    print("go to room on left")
    print("go to room ahead")
    print("go to room behind")
    print("look")
    print("look at 'character's name'")
    print("---------------------------------------------------------------------------------------------------------\n")


def print_game_intro():
    """
    This function prints the game intro information.
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
    print("\n---------------------------------------------------------------------------------------------------------")
    print("At last, your search is over! You found the infamous tower! Rumor has it, a necromancer resides here. \n"
          "Be on guard. You know what you are here to do, the time for action is nigh.")
    print("---------------------------------------------------------------------------------------------------------\n")
