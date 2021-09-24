from PIL import Image, ImageDraw

class Cell:
    def __init__(self, location, place_type, description, picture, opened):
        self.location = location
        self.place_type = place_type
        self.picture = Image.open(picture)
        self.description = description
        self.opened = opened