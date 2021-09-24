import pictures as pc
from cell import Cell
from bezier import *
from random import choice, randint, uniform
import json

class River:
    def __init__(self):
        with open("cell_type.json", "rb") as read_file:
            data = json.load(read_file)
        self.type = data['river']['type']
        self.description = data['river']['description']
        self.picture = data['river']['picture']


    def create_U_type(self):
        base = 0.5
        coeff = choice([-1, 1])
        print(coeff)
        rndBx = uniform(0.0, 0.4)
        rndBy = uniform(0.0, 0.3)
        rndAx = uniform(-0.4, rndBx-0.1)
        rndCx = uniform(-0.4, rndBx-0.1)
        B = [base+rndBx*coeff, base+rndBy*coeff]
        A = [base+rndAx*coeff, 0]
        C = [base+rndCx*coeff, 1]
        rndABx = (A[0] + B[0])/2+uniform(-0.05, 0.05)
        rndABy = (0 + B[1])/2+uniform(-0.05, 0.05)
        AB = [rndABx, rndABy]
        rndBCx = (C[0] + B[0])/2+uniform(-0.05, 0.05)
        rndBCy = (1 + B[1])/2+uniform(-0.05, 0.05)
        BC = [rndBCx, rndBCy]
        A1 = [A[0], AB[1]]
        B1 = [B[0], AB[1]]
        B2 = [B[0], BC[1]]
        C1 = [C[0], BC[1]]
        result = [[A, A1, AB], [AB, B1, B], [B, B2, BC], [BC, C1, C]]
        return result


    def create_S_type(self):
        base = 0.5
        A = [base+uniform(-0.4, 0.4), 0]
        C = [base+uniform(-0.4, 0.4), 1]
        rndABx = (A[0] + C[0])/2
        rndABy = base+uniform(-0.1, 0.1)
        B = [rndABx, rndABy]
        print(A, B, C)
        A1 = [A[0], B[1]]
        C1 = [C[0], B[1]]
        result = [[A, A1, B], [B, C1, C]]
        print(result)
        return result
    
    def define_count_neighbours(self, location, n_list, map):
        cx = location[1]
        cy = location[0]
        neighbours = []
        for i, n in enumerate(n_list):
            try:
                n_cell = map[cy+n[0]][cx+n[1]]
                if n_cell!='_':#n_cell.place_type==self.type
                    neighbours.append(i)
            except IndexError:
                continue
        return neighbours

    def search(self, n_list, location, map):
        cx = location[1]
        cy = location[0]
        for n in n_list:
            try:
                n_cell = map[cy+n[0]][cx+n[1]]
                if n_cell != '_':
                    return cy, cx+n[1]
            except IndexError:
                continue

    def check_wholeness_river(self, map):
        neighbours_1 = ((-1, 0), (0, 1), (1, 0), (0, -1))
        neighbours_2 = ((-1, -1), (-1, 1), (1, 1), (1, -1))
        for rn, r in enumerate(map):
            for cn, c in enumerate(r):
                if c!='_':
                    num_neighbours_1 = self.define_count_neighbours((rn, cn), neighbours_1, map)
                    num_neighbours_2 = self.define_count_neighbours((rn, cn), neighbours_2, map)
                    for n in range(4):
                        if n in num_neighbours_1 and n+1 in num_neighbours_1:
                            if n+1 not in num_neighbours_2:
                                map[rn][cn] = Cell(location=[rn, cn], place_type=self.type, description=self.description, picture= self.picture, opened=False)
                    if len(num_neighbours_1) ==1:
                        dict_def_cell = {0:2, 2:0, 1:3, 3:1}
                        neighbour = neighbours_1[dict_def_cell[num_neighbours_1[0]]]
                        rn += neighbour[0]
                        cn += neighbour[1]
                        if rn<=len(map)-1 and cn<=len(map)-1:
                            map[rn][cn] = Cell(location=[rn, cn], place_type=self.type, description=self.description, picture= self.picture, opened=False)
        return map


    def river_creator(self, size, map):
        ts = [t/size for t in range(size+1)]
        r_type =[self.create_U_type, self.create_S_type]
        riv = choice(r_type)()
        
        
        for n, r in enumerate(riv):
            for nn, c in enumerate(r):
                    riv[n][nn] = (round(size*c[0]), round(size*c[1]))
        coeff = choice([0, 1])
        for p_list in riv:
            bezier = make_bezier(p_list)
            points = bezier(ts)
            for p in points:
                if coeff == 0:
                    y = round(p[0])
                    x = round(p[1])
                else:
                    x = round(p[0])
                    y = round(p[1])
                map[y][x] = Cell(location=[y, x], place_type=self.type, description=self.description, picture= self.picture, opened=False)
        map = self.check_wholeness_river(map)
        return map