from PIL import Image, ImageDraw
 
# Создаем белый квадрат
# img = Image.new('RGBA', (160, 160), 'grey')    
# idraw = ImageDraw.Draw(img)
 
# idraw.rectangle((0, 0, 40, 40), fill='yellow')
# idraw.rectangle((40, 0, 80, 40), fill='green')
# idraw.rectangle((80, 0, 120, 40), fill='red')
# idraw.rectangle((120, 0, 160, 40), fill='blue')
 
# img.save('rectangle.png')

def map_paint(map):
    img = Image.new('RGBA', (len(map)*40, len(map)*40), 'grey')
    for row in map:
        for col in row:
            if col!='_':
                x1 = col.location[1]*40
                y1 = col.location[0]*40
                if col.opened:
                    img.paste(col.picture, (x1, y1))
    # return img
    img.save('D:/Python/games/map.png')
        