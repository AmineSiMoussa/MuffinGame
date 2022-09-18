import pygame

class Spliting_Sprite_Sheets():
    def __init__(self, image):
        self.sheet = image

    def split(self, frame, width, height):
        image = pygame.Surface((width ,height))
        image.blit(self.sheet, (0, 0), ((frame*width), 0, width, height))
        image.set_colorkey((0,0,0))

        return image