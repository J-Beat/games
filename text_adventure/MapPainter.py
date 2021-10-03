from pictures import map_paint
from PIL import Image


def player_paint(map, player_type, current, move_list):
    map_pic = map_paint(map)
    y = current[0]
    x = current[1]
    for my, mx in move_list:
        



def gifs(name, map, frames, pos, count):
    for frame_number in range(1, count+1):
        # Открываем изображение каждого кадра.
        frame = Image.open(f'D:/Python/games/text_adventure/GIFS/{name}_{frame_number}.png').convert('RGBA')
        i_map = map.copy()
        i_map.paste(frame, (pos[0], pos[1]), frame)
        # Добавляем кадр в список с кадрами.
        frames.append(i_map)#
    return frames

frames = gifs('viking_west_attack', map, frames, (200, 80), 2)
# frames = gifs('viking_south', map, frames, (200, 400))
# frames = gifs('viking_north', map, frames, (200, 400))
# frames = gifs('viking_north', map, frames, (200, 360))


frames[0].save(
    'south.gif', 'GIF',
    save_all=True,
    # transparency = 0,
    append_images=frames[1:],  # Срез который игнорирует первый кадр.
    optimize=True,
    duration=300,
    loop=3
)