import pygame
from os.path import join 

pygame.init()

# Information regarding Window Size and Game State
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
running = True

# Creates a Window and Title
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("SpaceWars")

# Icon
icon_path = join("assets","bronze.png")
icon_surface = pygame.image.load(icon_path).convert_alpha()
pygame.display.set_icon(icon_surface)

# Background Image
background_image = pygame.image.load(join("assets","Background.png")).convert_alpha()

# Main
while running: 
    # Event Loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("Maroon")
    display_surface.blit(background_image,(-100,-100))
    pygame.display.update()

pygame.quit()   