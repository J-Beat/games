from random import randint
from map_creator import MapCreator
import pictures as pc
from player import Player
from river import River


# map = MapCreator(size = [8, 8]).creator()

# rows = []
# for r in map:
#     columns = []
#     for c in r:
#         columns.append(c.place_type)
#     rows.append(columns)
# print(rows)
# pc.map_paint(map)

def main():
    mapsize = [10, 10]
    map = MapCreator(size = mapsize).creator()
    pc.map_paint(map)
    # player = Player([randint(0, mapsize[0]-1), randint(0, mapsize[1]-1)], mapsize)
    # while True:
    #     location = map[player.y][player.x]
    #     location.opened = True
    #     print(location.description)
    #     pc.map_paint(map)
    #     side = input()
    #     player.move(side)
        

if __name__ == '__main__':
    main()



