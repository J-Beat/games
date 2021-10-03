from PIL import Image, ImageDraw
import os

class Cell:
    def __init__(self, location, place_type, description, picture, opened):
        self.location = location
        self.place_type = place_type
        path = os.getcwd().replace('\\', '/')
        # print(path)
        self.picture = Image.open(path+f'/games/text_adventure/icons/{picture}')
        self.description = description
        self.opened = opened