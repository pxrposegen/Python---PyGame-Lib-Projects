import pygame
from os.path import join
from random import randint

pygame.init()

# Information regarding Window Size and Game State
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
running = True

# Creates a Window and Title
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("SpaceWars")

# Icon
icon_path = join("assets", "bronze.png")
icon_surface = pygame.image.load(icon_path).convert_alpha()
pygame.display.set_icon(icon_surface)

# Background Image
background_image = pygame.image.load(join("assets", "Background.png")).convert_alpha()
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Coins
coin_image = pygame.image.load(join("assets", "coin.png")).convert_alpha()
coin_image = pygame.transform.scale(coin_image, (50, 50))
coin_positions = [(randint(0,WINDOW_WIDTH-100), randint(0,WINDOW_HEIGHT-200)) for i in range(7)]

# Main
while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game Elements
    display_surface.fill("Maroon") 
    display_surface.blit(background_image, (0, 0))
    for pos in coin_positions:
        display_surface.blit(coin_image, pos)
    pygame.display.update()

pygame.quit()
