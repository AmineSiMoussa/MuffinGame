import pygame

#the class----------------------------------------------------+
class Background:

#---images------------------------------------------------------+

#---blue background-------------------------------------------+
    image_1 = pygame.image.load('sprites/background_blue.png')

#---the size of the blue background---------------------+
    image_1 = pygame.transform.scale(image_1,(890, 590))

#---red background-------------------------------------------+
    image_2 = pygame.image.load('sprites/background_red.png')

#---the size of the red background----------------------+
    image_2 = pygame.transform.scale(image_2,(890, 590))