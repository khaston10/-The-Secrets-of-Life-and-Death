from Humanoid import Humanoid
from HumanoidTypes import *
from Location import Location
from LocationTypes import *
from Functions import *
from AcceptableAnswers import *
from ItemTypes import *

def main():

    # Initialize game settings__________________________________________________

    # Initialize player settings.
    humanoid_type = question("Do you want to be a dwarf or goblin?", [["dwarf", "goblin"]])
    name = input("What is your name?")
    gender = question("What is your gender?", [["male", "female"]])
    weapon = question("What type of weapon do you want? (sword, axe)?", [["sword", "axe"]])
    player = create_humanoid(humanoid_type, name, gender, player=True)
    if weapon == "sword":
        player.items.append(Sword(assigned=True, item_type="sword", material="bronze", condition="new"))
    elif weapon == "axe":
        player.items.append(Axe(assigned=True, item_type="axe", material="bronze", condition="new"))

    list_of_acceptable_look_at_player_commands = ["look at " + player.name.lower()]


    # Initialize npc settings.
    probability_that_npc_will_move = 50  # This is given in percentage.
    npcs = create_npcs(4)
    for npc in npcs:
        weapon = random.choice(["sword", "axe"])
        assign_npc_item(npc, weapon)
        print(npc.name)
        print(npc.items)

    # Initialize locations.
    list_of_rooms = []
    room_1 = Big_Room(name="room_1", characters=[player])
    list_of_rooms.append(room_1)
    room_2 = Small_Room(name="room_2", characters=[npcs[0], npcs[1]])
    list_of_rooms.append(room_2)
    room_3 = Big_Room(name="room_3", characters=[npcs[2], npcs[3]])
    list_of_rooms.append(room_3)
    room_4 = Small_Room(name="room_4")
    list_of_rooms.append(room_4)
    room_5 = Big_Room(name="room_5")
    list_of_rooms.append(room_5)
    room_6 = Small_Room(name="room_6")
    list_of_rooms.append(room_6)
    room_7 = Big_Room(name="room_7")
    list_of_rooms.append(room_7)
    room_8 = Small_Room(name="room_8")
    list_of_rooms.append(room_8)

    # Connect locations.
    room_1.exits = {"east": room_2, "west": room_3, "north": room_5}
    room_2.exits = {"west": room_1}
    room_3.exits = {"east": room_1}
    room_4.exits = {"west": room_5}
    room_5.exits = {"east": room_4, "west": room_6, "south": room_1, "north": room_7}
    room_6.exits = {"east": room_5, "north": room_8}
    room_7.exits = {"south": room_5}
    room_8.exits = {"south": room_6}

    # Update player's and npc's location.
    player.room = room_1
    npcs[0].room = room_2
    npcs[1].room = room_2
    npcs[2].room = room_3
    npcs[3].room = room_3

    for npc in npcs:
        list_of_acceptable_look_at_player_commands.append("look at " + npc.name.lower())
    acceptable_answers.append(list_of_acceptable_look_at_player_commands)



    # Main game loop____________________________________________________________
    print_game_intro()
    game = True

    while game:

    # This line is put here for game testing purposes. It will print to screen all game objects and their locations.
        print_game_information(list_of_rooms)

        time = "stay"
        while time != "move forward":
    # Get user input____________________________________________________________
            action = question("What do you do?", acceptable_answers)

    # Update game state_________________________________________________________
        # Update player.

            if action in go_east:
                if "east" in player.room.exits:
                    player.room.delete_character(player)
                    player.go(player.room.exits["east"])
                    player.room.add_character(player)
                    time = "move forward"
            elif action in go_west:
                if "west" in player.room.exits:
                    player.room.delete_character(player)
                    player.go(player.room.exits["west"])
                    player.room.add_character(player)
                    time = "move forward"
            elif action in go_north:
                if "north" in player.room.exits:
                    player.room.delete_character(player)
                    player.go(player.room.exits["north"])
                    player.room.add_character(player)
                    time = "move forward"
            elif action in go_south:
                if "south" in player.room.exits:
                    player.room.delete_character(player)
                    player.go(player.room.exits["south"])
                    player.room.add_character(player)
                    time = "move forward"
            elif action in cmd_help:
                print_help_menu()
            elif action in look:
                print(player.look())
            elif action in list_of_acceptable_look_at_player_commands:
                print(player.look_at_character(action[8:len(action)]))

        # Update NPCs.
        # Pick the NPCs to move.
        npcs_to_move = []
        for npc in npcs:
            random_number = random.randint(1, 100)
            if 0 < random_number <= probability_that_npc_will_move:
                npcs_to_move.append(npc)
        # Move the NPCs.
        for npc in npcs_to_move:
            direction = random.choice(list(npc.room.exits.keys()))
            npc.room.delete_character(npc)
            npc.go(npc.room.exits[direction])
            npc.room.add_character(npc)



    # Print to screen___________________________________________________________
        print(player.room.get_description())
main()