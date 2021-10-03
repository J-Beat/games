class Player:
    def __init__(self, map, type):
        self.player_type = type
        self.map = map
        self.map_size = len(map)
        self.river_find()

    def river_find(self):
        self.river = []
        for r in range(len(self.map)):
            for c in range(len(self.map)):
                if self.map[r][c].place_type in ['river', 'brige', 'brody']:
                    self.river.append((r, c))

    def check_move(self, step):
        if type(step) == tuple:
            print(step, self.river)
            if step in self.river:
                print('river')
                res = []
                i = self.river.index(step)
                for n in range(i, len(self.river)):
                    c = self.river[n]
                    if self.map[c[0]][c[1]].place_type == 'river':
                        res.append(c)
                    else:
                        break
            else:
                res = [step]
        else:
            res = step
        return res





    def move(self, side, y, x):
        if side == 'north' and y >0:
            y -= 1
            result = (y, x)
        elif side == 'south' and y < self.map_size-1:
            y += 1
            result = (y, x)
        elif side == 'west' and x >0:
            x -= 1
            result = (y, x)
        elif side == 'east' and x < self.map_size-1:
            x += 1
            result = (y, x)
        else:
            result = 'Вы не можете идти в эту сторону'
        result = self.check_move(result)
        print(result)
        return result
        

    