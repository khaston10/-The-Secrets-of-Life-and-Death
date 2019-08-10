from Humanoid import Humanoid
from HumanoidTypes import *
from Location import Location
from LocationTypes import *
from Map import *
from Functions import *
from AcceptableAnswers import *
from random import randint


def main():

    # Initialize game settings__________________________________________________

    # Initialize player settings.
    humanoid_type = question("Do you want to be a dwarf or goblin?", [["dwarf", "goblin"]])
    name = input("What is your name?")
    gender = question("What is your gender?", [["male", "female"]])
    player = create_humanoid(humanoid_type, name, gender, player=True)

    # Initialize locations.
    seed = 666
    max_rooms = 32
    list_of_rooms = map_init(seed, randint(1, max_rooms))

    # Initialize npc settings.
    probability_that_npc_will_move = 50  # This is given in percentage.
    npcs = create_npcs(4)
    assign_npcs_items(npcs)
    for npc in npcs:
        print(npc.name)
        print(npc.items)

    # Update player's and npc's location.
    map_scatter_chars(player, npcs, list_of_rooms)

    list_of_acceptable_look_at_player_commands = []
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
