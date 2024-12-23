import pygame
from os.path import join
from random import randint
from ImageObject import ImageObject

pygame.init()

# Information regarding Window Size and Game State
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
running = True
clock = pygame.time.Clock()

# Creates a Window and Title
display_surface = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE
)
pygame.display.set_caption("SpaceWars")

# Icon
icon_path = join("assets", "bronze.png")
icon_surface = pygame.image.load(icon_path).convert_alpha()
pygame.display.set_icon(icon_surface)

# Background Image
background = ImageObject("assets/Background.png")
background.scale(WINDOW_WIDTH, WINDOW_HEIGHT)
background.frectposition("center", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

# Player
player = ImageObject("assets/plane.png")
player.scale(90, 50)
player.frectposition("midleft", 10, WINDOW_HEIGHT / 2)
player_direction = pygame.math.Vector2(2,-1)
player_speed = 100

# Coins
coin = ImageObject("assets/coin.png")
coin.scale(35, 35)
coin_positions = {
    (randint(0, WINDOW_WIDTH - 100), randint(0, WINDOW_HEIGHT - 300)) for i in range(7)
}

# Main
while running:
    # Frame Rendering readjusted with Delta Time 
    delta = clock.tick(240) / 1000 # Return value converted from ms to s
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game Elements
    display_surface.fill("Maroon")
    display_surface.blit(background.image, background.frect)
    for pos in coin_positions:
        display_surface.blit(coin.image, pos)

    # Player Movements
    player.frect.center += player_direction * player_speed * delta
    display_surface.blit(player.image, player.frect)

    pygame.display.update()

pygame.quit()
