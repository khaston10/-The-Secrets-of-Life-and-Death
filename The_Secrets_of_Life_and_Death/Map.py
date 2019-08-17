from LocationTypes import *
import random

m_directions = ['north', 'south', 'east', 'west']

def map_init(in_seed, in_max_num_rooms):
    random.seed(in_seed)
    list_of_rooms = []

    for i in range(random.randint(1, in_max_num_rooms)):

        # randomly add a big or small room. TODO: support other room types/sizes?
        if random.random() < 0.5:
            list_of_rooms.append(Big_Room())
        else:
            list_of_rooms.append(Small_Room())

    # Assign random coordinates to the locations. Only one location per set of coordinates.
    max_x = len(list_of_rooms)
    max_y = max_x
    # Denotes whether or not a set or coordinates are occupied. Initialize all to False.
    taken = [[False]*max_x for j in range(max_y)]

    # Place first room at a random location.
    room1 = list_of_rooms[0]
    x = random.randint(0, max_x - 1)
    y = random.randint(0, max_y - 1)
    taken[x][y] = True
    room1.coordinates = [x, y]

    # Place the rest of the rooms.
    for i in range(1, len(list_of_rooms)):  # Already placed first room, so skip it.
        # We want to make sure all rooms are connected.
        # So build off the previous room in an unoccupied direction
        [x, y] = list_of_rooms[i-1].coordinates

        while(True):  # Iterate until we've placed this room.
            dir = random.choice(m_directions)  # choose a random direction
            try:
                if dir == 'north' and y < max_y-1 and not taken[x][y+1]:
                    taken[x][y+1] = True
                    list_of_rooms[i].coordinates = [x, y+1]
                    break
                elif dir == 'south' and y > 0 and not taken[x][y-1]:
                    taken[x][y-1] = True
                    list_of_rooms[i].coordinates = [x, y-1]
                    break
                elif dir == 'east' and x < max_x-1 and not taken[x+1][y]:
                    taken[x+1][y] = True
                    list_of_rooms[i].coordinates = [x+1, y]
                    break
                elif dir == 'west' and x > 0 and not taken[x-1][y]:
                    taken[x-1][y] = True
                    list_of_rooms[i].coordinates = [x-1, y]
                    break
            except:
                print('gotcha, you wily bastard.')  # TODO: Fix whatever lands here.

    # Connect the locations.
    for room1 in list_of_rooms:  # for each room
        x1 = room1.coordinates[0]
        y1 = room1.coordinates[1]
        for room2 in list_of_rooms:  # check every other room to see if it is an exit to the former
            x2 = room2.coordinates[0]
            y2 = room2.coordinates[1]
            if y1 == y2 and x1 == (x2 - 1):  # configure East exit for room1
                room1.exits['east'] = room2
            if y1 == y2 and x1 == (x2 + 1):  # configure West exit for room1
                room1.exits['west'] = room2
            if x1 == x2 and y1 == (y2 - 1):  # configure North exit for room1
                room1.exits['north'] = room2
            if x1 == x2 and y1 == (y2 + 1):  # configure South exit for room1
                room1.exits['south'] = room2

    # Let unconnected rooms bark about it.
    for room in list_of_rooms:
        if len(room.exits) == 0:
            print('Room ' + str(room) + ' is lonely :(')

    # Print a rudimentary map.
    for y in range(max_y-1, -1, -1):
        for x in range(0, max_x-1):
            if taken[x][y]:
                print('O', end='')
            else:
                print('.', end='')
        print('\n')

    return list_of_rooms


def map_scatter_chars(in_player, in_npcs, in_list_of_rooms):
    in_player.room = in_list_of_rooms[random.randint(0, len(in_list_of_rooms)-1)]
    in_player.room.add_character(in_player)
    for npc in in_npcs:
        npc.room = in_list_of_rooms[random.randint(0, len(in_list_of_rooms)-1)]
        npc.room.add_character(npc)

def map_scatter_containers(in_containers, in_list_of_rooms):
    for container in in_containers:
        in_list_of_rooms[random.randint(0, len(in_list_of_rooms)-1)].containers.append(container)

