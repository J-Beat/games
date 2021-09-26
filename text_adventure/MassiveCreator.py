from random import randint, choice, shuffle
import json
from cell import Cell

class MassiveCreator:
    def __init__(self):
        self.neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        
        # print('block_size = ', self.blocks_size)

    def define_type(self, type):
        with open("D:/Python/games/text_adventure/cell_type.json", "rb") as read_file:
            data = json.load(read_file)
        cell_type = data[type]
        return cell_type

    def define_size_blocks(self, size):
        blocks = []
        coeff = [0.001, 0.02]
        while size >0:
            block = randint(10, 30)#
            if block>10:
                size -= block
                coeff[0] += 0.1
                coeff[1] += 0.1
                blocks.append(block)
            else:
                blocks.append(size)
                size = 0
        return blocks

    def get_massives(self, map, size, type):
        self.cell_type = self.define_type(type)
        blocks_size = self.define_size_blocks(size)
        for b in blocks_size:
            if self.get_count_free_cell(map)>3:
                try:
                    map, y, x = self.define_first_cell(map)
                    # print('first cell')
                    map = self.create_massive(y, x, map, b, self.neighbours)
                    # print('create massive')
                except TypeError:
                    print('TypeError')
                    continue
            else:
                continue
        return map

    def get_count_free_cell(self, map):
        count = 0
        for r in range(len(map)):
            for c in range(len(map)):
                n = self.define_neighbours(map, r, c, '_')
                if map[r][c] == '_' and len(n)>0:
                    count+=1
        return count


    def define_rand_cell(self, map, eq):
        rows = [_ for _ in range(len(map))]
        cols = [_ for _ in range(len(map))]
        shuffle(rows)
        shuffle(cols)
        result = []
        for r in rows:
            for c in cols:
                n = self.define_neighbours(map, r, c, '_')
                if eq == '_':
                    if len(n)>0 and map[r][c] == eq:
                        result.append([r, c])
                    else: continue
                else:
                    if map[r][c] =='_':
                        if len(self.define_neighbours(map, r, c, eq))>0:
                            if len(n)>0:
                                result.append([r, c])
                    else: continue
        # print('find cell')
        return result

    def define_first_cell(self, map):
        cell = self.define_rand_cell(map, '_')
        if len(cell)>0:
            y, x = cell[0]
            # print(f'first cell {self.cell_type}', map[y][x])
            map[y][x] = Cell(location=[y, x], place_type=self.cell_type['type'], description=self.cell_type['description'], picture= self.cell_type['picture'], opened=False)
            n = self.define_neighbours(map, y, x, '_')
            if len(n) >0:
                nc = choice(n)
                # print(f'second cell {self.cell_type}',map[nc[0]][nc[1]])
                map[nc[0]][nc[1]] = Cell(location=[nc[0], nc[1]], place_type=self.cell_type['type'], description=self.cell_type['description'], picture= self.cell_type['picture'], opened=False)
            
            return map, nc[0], nc[1]

    def define_neighbours(self, map, y, x, contain):
        ncl = []
        for n in self.neighbours:
            if 0<=y+n[0]<len(map) and 0<=x+n[1]<len(map):
                if contain == '_':
                    if map[y+n[0]][x+n[1]] == '_':
                        ncl.append([y+n[0], x+n[1]])
                else:
                    if map[y+n[0]][x+n[1]] != '_':
                        if map[y+n[0]][x+n[1]].place_type == contain:
                            ncl.append([y+n[0], x+n[1]])
        return ncl


    def create_massive(self, y, x, map, size, neighbours):
        size = size-2
        m_size = 0
        # neighbours = list([(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)])
        while m_size<size:
            # print('start while')
            shuffle(neighbours)
            if self.get_count_free_cell(map) == 0:
                break
            for n in neighbours:
                if self.get_count_free_cell(map) == 0:
                    break
                # print('start_for  ', y+n[0], x+n[1], 'count free cell ', self.get_count_free_cell(map))
                if 0<=y+n[0]<len(map) and 0<=x+n[1]<len(map):
                    # print('count free neighbours  ', len(self.define_neighbours(map, y+n[0], x+n[1], True)))
                    cell = self.define_rand_cell(map, self.cell_type['type'])
                    # print('free cell w neighb  ', len(cell), 'free cells  ', self.get_count_free_cell(map))
                    if len(cell) >0:
                        if len(self.define_neighbours(map, y+n[0], x+n[1], '_')) > 0:
                            # print(map[y+n[0]][x+n[1]])
                            if map[y+n[0]][x+n[1]] == '_':
                                # print(map[y+n[0]][x+n[1]])
                                map[y+n[0]][x+n[1]] = Cell(location=[y+n[0], x+n[1]], place_type=self.cell_type['type'], description=self.cell_type['description'], picture= self.cell_type['picture'], opened=False)
                                y = y+n[0]
                                x = x+n[1]
                                m_size +=1
                        else:
                            if self.get_count_free_cell(map) > 2:
                                # print('free cells = ', self.get_count_free_cell(map))
                                y, x = choice(self.define_rand_cell(map, self.cell_type['type']))
                                # print(map[y][x])
                                map[y][x] = Cell(location=[y, x], place_type=self.cell_type['type'], description=self.cell_type['description'], picture= self.cell_type['picture'], opened=False)                     
                            else: m_size = size
                    else: m_size = size   

        return map

    def fill_free_cells(self, map):
        for r in range(len(map)):
            for c in range(len(map)):
                neighbours = {}
                if map[r][c] == '_':
                    # print(self.get_count_free_cell(map))
                    for type in ['forest', 'field', 'mountains', 'hills', 'swamp']:
                        neighbours[type] = len(self.define_neighbours(map, r, c, type))
                    sorted_values = sorted(neighbours.values()) # Sort the values
                    sorted_dict = {}
                    for i in sorted_values:
                        for k in neighbours.keys():
                            if neighbours[k] == i:
                                sorted_dict[k] = neighbours[k]
                                # break
                    res_type = list(sorted_dict.keys())[-1]
                    cell_type = self.define_type(res_type)
                    map[r][c] = Cell(location=[r, c], place_type=cell_type['type'], description=cell_type['description'], picture= cell_type['picture'], opened=False)
        return map

# map = [['_' for _ in range(30)] for _ in range(30)]

# pc.map_paint(map)