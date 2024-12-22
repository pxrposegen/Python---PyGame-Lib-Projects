import pygame
from sys import exit

pygame.init()

# Information regarding Window Size and Game State
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
running = True

# Creates a Window and Title
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("SpaceWars")

# Icon
icon_surface = pygame.image.load('assets/bronze.png')
pygame.display.set_icon(icon_surface)
# Surface


# Main
while running: 
    # Event Loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0, 41, 51))
    pygame.display.update()

pygame.quit()   