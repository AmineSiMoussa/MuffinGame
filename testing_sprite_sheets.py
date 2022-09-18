import pygame,sys
from Game_1.Animator import Spliting_Sprite_Sheets
import time

pygame.init()

(width, height) = (890, 590)
pygame.display.set_caption("sprite sheet")
DISPLAY = pygame.display.set_mode((width, height))

BG = (50,50,50)
#--------+
frame = 8
#--------+
slashing = False
dir = False
#-----------------------------------------------------------------------------+
sprite_sheet_image = pygame.image.load('sprites/slash_spriteSheet.png')

sprite_sheet = Spliting_Sprite_Sheets(sprite_sheet_image)
#-----------------------------------------------------------------------------+

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    DISPLAY.fill(BG)

    keys = pygame.key.get_pressed()
    
#----------------------------------------------------------+
    left_slash = sprite_sheet.split(frame, 73, 74)
    right_slash = pygame.transform.flip(left_slash, True, False)
    right_slash.set_colorkey((0,0,0))

    if keys[pygame.K_a]:
        dir = True

    if keys[pygame.K_d]:
        dir = False

    if keys[pygame.K_SPACE]:
        slashing = True
    
    if slashing == True and frame < 9:
        frame = frame + 1
        time.sleep(0.05)

    if frame > 8:
        frame = -1
        slashing = False
#-----------------------------------------------------------+

    if dir == False:
        DISPLAY.blit(right_slash, (width/2,height/2))
    if dir == True:
        DISPLAY.blit(left_slash, (width/2,height/2))

    pygame.display.update()