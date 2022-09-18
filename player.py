import pygame

#the class------------------------------------------------------+
class Player:

#---player size-+
    size = 74

#---player positions-----+
    posX = 890/2 - size/2
    posY = 590/2 - size/2

#---player movement speed-+
    moveSpeed = 2.5

#---the sprites for turning left and right---------------------+

#---right sprite----------------------------------------------+
    rightSprite = pygame.image.load('sprites/Muffin_player.png')

#---left sprite-----------------------------------------------+
    leftSprite = pygame.transform.flip(rightSprite, True, False)