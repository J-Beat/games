def define_neighbours(location, n_list, map, check, type=False):
        cx = location[1]
        cy = location[0]
        neighbours = []
        for i, n in enumerate(n_list):
            if cy+n[0]<len(map) and cx+n[1]<len(map):
                n_cell = map[cy+n[0]][cx+n[1]]
                check = check_cell_contains(n_cell)
                if check!='NaN':
                    if type!=False and check == type:
                        neighbours.append(i)
                    elif type==False:
                        neighbours.append(i)
        return neighbours


def check_cell_contains(n_cell):
    if n_cell == '_':
        result = 'NaN'
    elif type(n_cell) != str:
        result = n_cell.place_type
    return result