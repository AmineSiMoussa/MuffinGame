#importing stuff------------------+
import pygame, sys, time
from pygame.locals import*

import weapons

#importing classes---------------+
from player import Player
from background import Background

#main game-------------------------------------------------------------------+
def main():
    pygame.init()

#---window-------------------------------------------+
    (width, height) = (890, 590)
    pygame.display.set_caption("Game")
    DISPLAY = pygame.display.set_mode((width, height))

#---framerate-----------------+
    FPS = 60
    cloke = pygame.time.Clock()

#---delta time stuff------+
    lastTime = time.time()

#---player class variable-+
    player = Player()

#---weapons-------+
    sword = weapons.Weapon1
    frames = 8
#---state of combat-+
    attacking = weapons.attacking
    recovery = True

    #background class variable-+
    background = Background()

    #direction of the player and weapons-+
    direction = False

#---game running--------------------------------------------------------------+
    while True:

#-------quiting the game---------------+
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

#-------delta time doing stuff----+
        dt = time.time() - lastTime
        dt *= 60
        lastTime = time.time()

#-------background---------------------------+
        DISPLAY.blit(background.image_2, (0,0))

#-------player movement controls-----+
        keys = pygame.key.get_pressed()

#-------up and down controls--------------------------------+
        if keys[pygame.K_s]:
            player.posY = player.posY + player.moveSpeed * dt
        if keys[pygame.K_w]:
            player.posY = player.posY - player.moveSpeed * dt

#-------left and right controls----------------------------+
        if keys[pygame.K_d]:
            player.posX = player.posX + player.moveSpeed * dt
            direction = False
        if keys[pygame.K_a]:
            player.posX = player.posX - player.moveSpeed * dt
            direction = True

#-------when the player turns left----------------------------------+
        if direction == True:
            DISPLAY.blit(player.leftSprite, (player.posX,player.posY))

#-------when the player turn right-----------------------------------+
        if direction == False:
            DISPLAY.blit(player.rightSprite, (player.posX,player.posY))
        
#-------weapons----------------------------------------------------------------------------------------------+

#-------sword--------------------------------------------------------------------------------------------+
        if direction == False:
            DISPLAY.blit(sword.rightSprite, (player.posX + sword.offsetX, player.posY + sword.offsetY))
        if direction == True:
            DISPLAY.blit(sword.leftSprite, (player.posX + sword.offsetX * -1,player.posY + sword.offsetY))

#-------attacking with the sword---------------------------------------------------+

#-------attacking control------+
        if keys[pygame.K_SPACE] and recovery == True:
            attacking = True

#-------attacking animation------------------------------------------------------+

        if direction == False and attacking == True:
            sword.rightSprite = pygame.transform.rotate(sword.rightSprite_2, -90)
            sword.offsetY = 30
        if direction == False and attacking == False:
            sword.rightSprite = pygame.transform.rotate(sword.rightSprite_2, 0)
            sword.offsetY = 0

        if direction == True and attacking == True:
            sword.leftSprite = pygame.transform.rotate(sword.leftSprite_2, 90)
            sword.offsetY = 30
        if direction == True and attacking == False:
            sword.leftSprite = pygame.transform.rotate(sword.leftSprite_2, 0)
            sword.offsetY = 0

#-------animation--------------------------------------------------------------------------------------------+
        left_slash = sword.sprite_sheet.split(frames, 73, 74)
        left_slash = pygame.transform.scale(left_slash,(100, 100))
        right_slash = pygame.transform.flip(left_slash, True, False)
        right_slash.set_colorkey((0,0,0))

        if attacking == True and frames < 9:
            frames = frames + 1
            time.sleep(0.05)

        if frames > 8:
            frames = -1
            sword.rightSprite = pygame.transform.rotate(sword.rightSprite_2, 0)
            sword.leftSprite = pygame.transform.rotate(sword.leftSprite_2, 0)
            attacking = False

        if direction == False:
            DISPLAY.blit(right_slash, (player.posX + (sword.offsetX * 2), player.posY))
        if direction == True:
            DISPLAY.blit(left_slash, (player.posX + ((sword.offsetX + 14) * 2 * -1), player.posY))

#-------offscreen teleport on the x-axis----------+
        if player.posX > 980:
            player.posX = player.posX - (980 + 105)
        if player.posX < -130:
            player.posX = player.posX + 980 + 75

#-------offscreen teleport on the y-axis--+
        if player.posY > 580:
            player.posY = player.posY - 654
        if player.posY < -74:
            player.posY = player.posY + 654

#-------refreshing the game--+
        pygame.display.update()
#-------frames per second-+
        cloke.tick(FPS)
        
main()