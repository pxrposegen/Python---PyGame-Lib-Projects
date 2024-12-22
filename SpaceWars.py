import pygame
from sys import exit


pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Creates a Window 
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("SpaceWars")
running = True

while running: 
    # Event Loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0, 41, 51))
    pygame.display.update()

pygame.quit()   