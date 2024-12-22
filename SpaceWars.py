import pygame
from sys import exit


pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Creates a Window 
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
running = True

while running: 
    # Event Loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

pygame.quit()