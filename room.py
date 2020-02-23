from copy import deepcopy

class Room(object):

    def __init__(self):
        self.room = []
        self.rows = 0
        self.columns = 0

    def load_room(self, new_room):
        self.room = deepcopy(new_room)
        self.rows = len(new_room)
        self.columns = len(new_room[0])

    def load_room_from_file(self, reader):
        line = reader.readline()
        self.room = []
        self.rows = 0

        while line != '':
            self.room.append([int(i) for i in line if i != '\n'])
            self.rows += 1
            line = reader.readline()
        self.columns = len(self.room[0])

    def set_bulb(self, posx, posy):
        self.room[posx][posy] = 'b'

        # iluminate above
        i,j = posx - 1, posy
        while i >= 0 and self.room[i][j] != 1:
            self.room[i][j] = 'i'
            i -= 1

        # iluminate to right
        i,j = posx, posy + 1
        while j < self.columns and self.room[i][j] != 1:
            self.room[i][j] = 'i'
            j += 1

        # iluminate below
        i,j = posx + 1, posy
        while i < self.rows and self.room[i][j] != 1:
            self.room[i][j] = 'i'
            i += 1

        # iluminate to left
        i,j = posx, posy - 1
        while j >= 0 and self.room[i][j] != 1:
            self.room[i][j] = 'i'
            j -= 1

    def get_room(self):
        return self.room
    
    def print_room(self):
        for row in self.room:
            print(row)
