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
background_image_rect = background_image.get_frect(center = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2))

#Player 
player_image = pygame.image.load(join("assets","plane.png")).convert_alpha()
player_image = pygame.transform.scale(player_image,(90,50))
player_rect = player_image.get_frect(midleft = (10,WINDOW_HEIGHT / 2))

# Coins
coin_image = pygame.image.load(join("assets", "coin.png")).convert_alpha()
coin_image = pygame.transform.scale(coin_image, (35, 35))
coin_positions = [(randint(0,WINDOW_WIDTH-100), randint(0,WINDOW_HEIGHT-200)) for i in range(7)]

# Main
while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game Elements
    display_surface.fill("Maroon") 
    display_surface.blit(background_image, background_image_rect)
    player_rect.left += 0.1
    display_surface.blit(player_image, player_rect)
    for pos in coin_positions:
        display_surface.blit(coin_image, pos)
    pygame.display.update()

pygame.quit()
