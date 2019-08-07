from Humanoid import Humanoid
from HumanoidTypes import *
from Location import Location
from LocationTypes import *
from Functions import *


def main():

    # Initialize game settings__________________________________________________

    # Initialize player settings.
    humanoid_type = question("Do you want to be a dwarf or goblin?", ["dwarf", "goblin"])
    name = input("What is your name?")
    gender = question("What is your gender?", ["male", "female"])
    player = create_humanoid(humanoid_type, name, gender, player=True, player_id=-1)

    # Initialize npc settings.
    probability_that_npc_will_move = 50  # This is given in percentage.
    npcs = create_nps(4)

    # Initialize locations.
    list_of_rooms = []
    room_1 = Big_Room(name="room_1", characters=[player], player_ids=[player.player_id])
    list_of_rooms.append(room_1)
    room_2 = Small_Room(name="room_2", characters=[npcs[0], npcs[1]], player_ids=[npcs[0].player_id, npcs[1].player_id])
    list_of_rooms.append(room_2)
    room_3 = Big_Room(name="room_3", characters=[npcs[2], npcs[3]], player_ids=[npcs[2].player_id, npcs[3].player_id])
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
    room_1.exits = {"right": room_2, "left": room_3, "ahead": room_5}
    room_2.exits = {"left": room_1}
    room_3.exits = {"right": room_1}
    room_4.exits = {"left": room_5}
    room_5.exits = {"right": room_4, "left": room_6, "behind": room_1}
    room_6.exits = {"right": room_5, "ahead": room_8}
    room_7.exits = {"behind": room_5}
    room_8.exits = {"behind": room_6}

    # Update player's and npc's location.
    player.room = room_1
    npcs[0].room = room_2
    npcs[1].room = room_2
    npcs[2].room = room_3
    npcs[3].room = room_3

    # Initialize acceptable answers.
    acceptable_answers = ["go to room on right", "go to room on left",
                          "go to room ahead", "go to room behind", "look", "help"]
    list_of_acceptable_look_at_player_commands = []
    for npc in npcs:
        acceptable_answers.append("look at " + npc.name.lower())
        list_of_acceptable_look_at_player_commands.append("look at " + npc.name.lower())



    # Main game loop____________________________________________________________
    print_game_intro()
    game = True

    while game:

    # This line is put here for game testing purposes. It will print to screen all game objects and their locations.
        # print_game_information(list_of_rooms)

        time = "stay"
        while time != "move forward":
    # Get user input____________________________________________________________
            action = question("What do you do?", acceptable_answers)

    # Update game state_________________________________________________________
        # Update player.

            if action == "go to room on right":
                if "right" in player.room.exits:
                    player.room.delete_character(player)
                    player.go(player.room.exits["right"])
                    player.room.add_character(player)
                    time = "move forward"
            elif action == "go to room on left":
                if "left" in player.room.exits:
                    player.room.delete_character(player)
                    player.go(player.room.exits["left"])
                    player.room.add_character(player)
                    time = "move forward"
            elif action == "go to room ahead":
                if "ahead" in player.room.exits:
                    player.room.delete_character(player)
                    player.go(player.room.exits["ahead"])
                    player.room.add_character(player)
                    time = "move forward"
            elif action == "go to room behind":
                if "behind" in player.room.exits:
                    player.room.delete_character(player)
                    player.go(player.room.exits["behind"])
                    player.room.add_character(player)
                    time = "move forward"
            elif action == "help":
                print_help_menu()
            elif action == "look":
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