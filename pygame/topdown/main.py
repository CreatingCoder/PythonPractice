import pygame, sys
from pygame.locals import *

#initialize pygame instance
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#set caption
pygame.display.set_caption('My PyGame')

player = pygame.Rect((30,30,30,30))

#set boolean for means to end running loop
running = True

while running:

    screen.fill('black')

    pygame.draw.rect(screen, 'green', player)

    #player input
    key = pygame.key.get_pressed()
    
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)

    elif key[pygame.K_d] == True:
        player.move_ip(1,0)

    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)


    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    #pygame.draw.rect(screen, 'green', rect=(30, 30, 30, 30))

pygame.quit()
    
    



#rect isn't shown without       pygame.draw.rect(screen, 'green', rect=(30, 30, 30, 30))

    

