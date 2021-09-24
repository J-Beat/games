import pictures as pc
from cell import Cell
from bezier import *
from random import choice, randint, uniform
from river import River


class MapCreator:
    def __init__(self, size):
        self.size = size
        self.map = [['_' for c in range(self.size+1)] for r in range(self.size+1)]
        river = River()
        self.map = river.river_creator(self.size, self.map)
        # print(self.map)
        pc.map_paint(self.map)



MapCreator(10)

