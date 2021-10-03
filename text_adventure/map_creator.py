import pictures as pc
from cell import Cell
from bezier import *
from random import choice, randint, uniform
from river import River
from LineBezierCreator import LineCreator
from MassiveCreator import MassiveCreator
from datetime import datetime as dt 


class MapCreator:
    def creator(self, size):
        self.size = size
        self.map = [['_' for _ in range(self.size+1)] for _ in range(self.size+1)]
        river = River()
        massive = MassiveCreator()
        massive_size =  massive.get_count_free_cell(self.map)
        print(massive_size)
        self.map = LineCreator().line_creator(self.size, self.map, river)
        self.map = massive.get_massives(self.map, massive_size*0.3, 'field')
        self.map = massive.get_massives(self.map, massive_size*0.3, 'forest')
        self.map = massive.get_massives(self.map, massive_size*0.2, 'hills')
        self.map = massive.get_massives(self.map, massive_size*0.1, 'mountains')
        self.map = massive.get_massives(self.map, massive_size*0.1, 'swamp')
        self.map = massive.fill_free_cells(self.map)
        pc.map_paint(self.map)
        return self.map

if __name__ == '__main__':
    t = dt.now()
    MapCreator().creator(10)
    print(dt.now()-t)
