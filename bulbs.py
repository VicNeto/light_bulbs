from room import Room
from copy import deepcopy


def try_new_disposition(room, row_range, column_range):
    current_room = room.get_room()
    number_of_bulbs = 0
    
    for i in row_range:
        for j in column_range:

            if current_room[i][j] == 0:
                room.set_bulb(i,j)
                number_of_bulbs += 1

    return number_of_bulbs

def try_dispostions(room):
    room_copy = deepcopy(room.get_room())
    xrange = range(len(room_copy))
    yrange = range(len(room_copy[0]))
    ranges = ((xrange, list(reversed(xrange))), (yrange, list(reversed(yrange))))
    min_bulbs = len(room_copy) * len(room_copy[0])

    for x_rg in ranges[0]:
        for y_rg in ranges[1]:
            disposition_bulbs = try_new_disposition(room, x_rg, y_rg)

            if disposition_bulbs < min_bulbs:
                min_bulbs = disposition_bulbs
                best_room = room.get_room()[:]

            room.load_room(room_copy)

    return (best_room, min_bulbs)


def check_cross(room):
    r = room.get_room()
    current_bulbs = 0
    cross_items = ((-1,0), (1,0), (0,-1), (0,1))
    x_items = ((-1,-1), (-1,1), (1,1), (1,-1))
    xr_items = ((-1,1), (1,1), (1,-1), (-1,-1))

    for i in range(1, len(r) - 1):
        for j in range(1, len(r[0]) - 1):
            if all([r[i+add[0]][j+add[1]] == 0 for add in cross_items]) and any([ r[i+it[0]][j+it[1]] == 1 and r[i+it2[0]][j+it2[1]] == 1 for it,it2 in zip(x_items, xr_items)]):
                room.set_bulb(i,j)
                current_bulbs += 1
    return current_bulbs


def solve_minimum_bulbs():
    room = Room()

    with open('room.txt', 'r') as reader:
        room.load_room_from_file(reader)
        bulbs = check_cross(room)
        solution, n_solution = try_dispostions(room)

        for i in solution:
            print(i)
        print(n_solution)

        return (solution, n_solution + bulbs)
    
    return None
