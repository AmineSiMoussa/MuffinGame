import pygame
from Animator import Spliting_Sprite_Sheets

attacking = False

class Weapon1:

    offsetX = 30
    offsetY = 0

    rightSprite = pygame.image.load('sprites/Sword.png')
    leftSprite = pygame.transform.flip(rightSprite, True, False)

    rightSprite_2 = pygame.image.load('sprites/Sword.png')
    leftSprite_2 = pygame.transform.flip(rightSprite, True, False)

    sprite_sheet_image = pygame.image.load('sprites/slash_spriteSheet.png')
    sprite_sheet = Spliting_Sprite_Sheets(sprite_sheet_image)