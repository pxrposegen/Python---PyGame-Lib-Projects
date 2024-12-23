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
player_direction = pygame.math.Vector2()
player_speed = 300

# Coins
coin = ImageObject("assets/coin.png")
coin.scale(35, 35)
coin_positions = {
    (randint(0, WINDOW_WIDTH - 100), randint(0, WINDOW_HEIGHT - 300)) for i in range(7)
}

# Main
while running:
    # Frame Rendering readjusted with Delta Time
    delta = clock.tick(240) / 1000  # Return value converted from ms to s

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Movement Input
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
    player_direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

    # Diagonal player speed would increase, Consistent speed can be achieved with Normalizing
    # if player_direction returns false if vector is [0,0] and true if it's any other value
    player_direction = (
        player_direction.normalize() if player_direction else player_direction
    )
    player.frect.center += player_direction * player_speed * delta

    # Game Elements
    display_surface.fill("Maroon")
    display_surface.blit(background.image, background.frect)
    for pos in coin_positions:
        display_surface.blit(coin.image, pos)
    display_surface.blit(player.image, player.frect)
    pygame.display.update()

pygame.quit()
