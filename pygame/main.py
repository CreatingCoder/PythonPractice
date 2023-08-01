import pygame
import sys

pygame.init()
scr = pygame.display.set_mode((350, 600))
clock = pygame.time.Clock()

run = True

def draw():
    scr.fill('lightblue')


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame,quit()
            sys.exit

    

    draw()

    clock.tick(60)
    pygame.display.update()
