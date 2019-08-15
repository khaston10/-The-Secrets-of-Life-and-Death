from LocationTypes import *
import random


def map_init(in_seed, in_max_num_rooms):
    random.seed(in_seed)
    list_of_rooms = []

    for i in range(random.randint(1, in_max_num_rooms)):

        # randomly add a big or small room. TODO: support other room types/sizes?
        if random.random() < 0.5:
            list_of_rooms.append(Big_Room())
        else:
            list_of_rooms.append(Small_Room())

    # Connect locations.
    for i in range(len(list_of_rooms)-1):  # TODO: make this dummy connection method more interesting
        # connect this room's eastern exit to the next room's western exit
        list_of_rooms[i].exits["east"] = list_of_rooms[i+1]

        # and visa versa
        list_of_rooms[i+1].exits["west"] = list_of_rooms[i]

    return list_of_rooms


def map_scatter_chars(in_player, in_npcs, in_list_of_rooms):
    in_player.room = in_list_of_rooms[random.randint(1, len(in_list_of_rooms))]
    in_player.room.add_character(in_player)
    for npc in in_npcs:
        npc.room = in_list_of_rooms[random.randint(0, len(in_list_of_rooms)-1)]
        npc.room.add_character(npc)

def map_scatter_containers(in_containers, in_list_of_rooms):
    for container in in_containers:
        in_list_of_rooms[random.randint(0, len(in_list_of_rooms)-1)].containers.append(container)

