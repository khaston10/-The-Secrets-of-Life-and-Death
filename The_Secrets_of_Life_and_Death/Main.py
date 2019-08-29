from Humanoid import Humanoid
from HumanoidTypes import *
from Location import Location
from LocationTypes import *
from Map import *
from Functions import *
from AcceptableAnswers import *
from random import randint
from ItemTypes import *
from Map import print_maps
from HumanoidNames import humanoid_names
from HumanoidMoods import humanoid_moods
from MapSettings import *


def main():

    # Initialize game settings__________________________________________________
    print_game_logo()

    # Initialize player settings.
    player = initialize_player_settings()
    list_of_acceptable_look_at_player_commands = ["look at " + player.name.lower()]

    # Initialize locations.
    seed = 666
    list_of_rooms = map_init(seed, randint(1, max_rooms))

    # Initialize npc settings.
    npcs = create_npcs(number_of_npcs, humanoid_names, humanoid_moods)
    for npc in npcs:
        weapon = random.choice(["sword", "axe"])
        assign_npc_item(npc, weapon)
        assign_npc_item(npc, "shield")
        assign_npc_item(npc, "helmet")

    # Update player's and npc's location.
    map_scatter_chars(player, npcs, list_of_rooms)

    for npc in npcs:
        list_of_acceptable_look_at_player_commands.append("look at " + npc.name.lower())
    acceptable_answers.append(list_of_acceptable_look_at_player_commands)
    list_of_humanoids = npcs.copy()
    list_of_humanoids.append(player)

    list_of_containers = create_containers_with_random_items(number_of_containers)
    map_scatter_containers(list_of_containers, list_of_rooms)

    # Main game loop____________________________________________________________
    game = True
    print_game_intro()
    while game:
        # This line is put here for game testing purposes. It will print to screen all game objects and their locations.
        # print_game_information(list_of_rooms)

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
            elif action in open_container:
                player_open_container(player)
                time = "move forward"
            elif action in close_container:
                player_close_container(player)
                time = "move forward"
            elif action in pick_lock:
                success = player_pick_lock(player)
                if success:
                    time = "move forward"
            elif action in take_item_from_container:
                player_take_item_from_container(player)
                time = "move forward"
            elif action in put_item_in_container:
                player_put_item_in_container(player)
                time = "move forward"
            elif action in put_item_in_backpack:
                player_put_item_in_backpack(player)
                time = "move forward"
            elif action in take_item_from_backpack:
                player_take_item_from_backpack(player)
                time = "move forward"
            elif action in show_map:
                print_maps(list_of_rooms)
            elif action in cmd_help:
                print_help_menu()
            elif action in look:
                print(player.look())
            elif action in list_of_acceptable_look_at_player_commands:
                hum = get_humanoid_object_from_look_command(action, list_of_humanoids)
                print(look_at_humanoid(hum))

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
