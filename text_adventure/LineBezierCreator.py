import pictures as pc
from cell import Cell
from bezier import *
from random import choice, randint, uniform
import json
from define_neighbours import *


class LineCreator:
    def check_wholeness(self, map):
        neighbours_1 = ((-1, 0), (0, 1), (1, 0), (0, -1))
        neighbours_2 = ((-1, -1), (-1, 1), (1, 1), (1, -1))
        for rn, r in enumerate(map):
            for cn, c in enumerate(r):
                if c!='_':
                    num_neighbours_1 = define_neighbours((rn, cn), neighbours_1, map, '_')
                    num_neighbours_2 = define_neighbours((rn, cn), neighbours_2, map, '_')
                    for n in range(4):
                        if n in num_neighbours_1 and n+1 in num_neighbours_1:
                            if n+1 not in num_neighbours_2:
                                map[rn][cn] = Cell(location=[rn, cn], place_type=self.cell_type['type'], description=self.cell_type['description'], picture= self.cell_type['picture'], opened=False)
                    if len(num_neighbours_1) ==1:
                        dict_def_cell = {0:2, 2:0, 1:3, 3:1}
                        neighbour = neighbours_1[dict_def_cell[num_neighbours_1[0]]]
                        rn += neighbour[0]
                        cn += neighbour[1]
                        if rn<=len(map)-1 and cn<=len(map)-1:
                            map[rn][cn] = Cell(location=[rn, cn], place_type=self.cell_type['type'], description=self.cell_type['description'], picture= self.cell_type['picture'], opened=False)
        return map


    def line_creator(self, size, map, object):
        ts = [t/size for t in range(size+1)]
        massive = object.def_type()
        self.cell_type = object.cell_type
        
        
        for n, r in enumerate(massive):
            for nn, c in enumerate(r):
                    massive[n][nn] = (round(size*c[0]), round(size*c[1]))

        for p_list in massive:
            bezier = make_bezier(p_list)
            points = bezier(ts)
            for p in points:
                if object.orientation == 0:
                    y = round(p[0])
                    x = round(p[1])
                else:
                    x = round(p[0])
                    y = round(p[1])
                map[y][x] = Cell(location=[y, x], place_type=self.cell_type['type'], description=self.cell_type['description'], picture= self.cell_type['picture'], opened=False)
        map = self.check_wholeness(map)
        return map