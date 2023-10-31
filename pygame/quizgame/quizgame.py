import pygame, sys
from pygame.locals import *

#initialize pygame instance
pygame.init()

#create screen
screen = pygame.display.set_mode((680, 400))

#set caption
pygame.display.set_caption('My PyGame')

#create clock 
#clock = pygame.time.Clock()

#set boolean for means to end running loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.rect(screen, 'green', rect=(30, 30, 30, 30))


    #rect isn't shown without
    pygame.display.flip()
