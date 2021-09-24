class Player:
    def __init__(self, start_location, map_size):
        self.map_size = map_size
        self.y = start_location[0]
        self.x = start_location[1]

    def move(self, side):
        if side == 'north' and self.y >0:
            self.y -= 1
        elif side == 'south' and self.y < self.map_size[0]-1:
            self.y += 1
        elif side == 'west' and self.x >0:
            self.x -= 1
        elif side == 'east' and self.x < self.map_size[1]-1:
            self.x += 1
        else:
            print('Вы не можете идти в ту сторону, там стена')

    