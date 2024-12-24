import pygame
from os.path import join
from random import randint, uniform


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("assets", "plane.png"))
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
        self.direction = pygame.math.Vector2()
        self.speed = 350

        # Laser
        self.can_shoot = True
        self.cooldown_duration = 500
        self.laser_shoot_time = 0

        # Mask 
        self.mask = pygame.mask.from_surface(self.image)

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = (
            self.direction.normalize() if self.direction else self.direction
        )
        self.rect.center += self.direction * self.speed * delta_time

        if keys[pygame.K_LSHIFT]:
            self.speed = 600
        else:
            self.speed = 350

        if pygame.mouse.get_just_pressed()[0] and self.can_shoot:
            Laser(laser_image, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        self.laser_timer()


class Laser(pygame.sprite.Sprite):
    def __init__(self, surface, position, groups):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(midbottom=position)

    def update(self, delta):
        self.rect.centery -= 700 * delta
        if self.rect.bottom < 0:
            self.kill()


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, surface, position, speed, groups):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(center=position)
        self.direction = pygame.math.Vector2(
            uniform(-0.5, 0.5), 1
        )  # Directional Asteroids
        self.speed = speed

    def update(self, delta):
        self.rect.center += (
            self.direction * self.speed * delta
        )  # Sets Asteroid Movement Speed
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()


# Function responsible for Collisions
def collision():
    global running
    global score

    # Collision between Asteroid and Player Ship
    destoryed_ship = pygame.sprite.spritecollide(player, asteroid_sprite, True, pygame.sprite.collide_mask)
    if destoryed_ship:
        running = False

    # Collision between Laser and Asteroid
    for laser in laser_sprites:
        destroyed_asteroid = pygame.sprite.spritecollide(laser, asteroid_sprite, True, pygame.sprite.collide_mask)
        if destroyed_asteroid:
            score += 1
            laser.kill()

# Function for Display Score
def display_score():
    score_text = game_font.render(str(score), False, (240, 240, 240))
    score_rect = score_text.get_frect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50))
    display_surface.blit(score_text, score_rect)
    pygame.draw.rect(display_surface, (240, 240, 240), score_rect.inflate(20, 20), 5, 5)


pygame.init()

# Window Constants, DO NOT CHANGE
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

running = True
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Window Icon and Title
icon_image = pygame.image.load(join("assets", "bronze.png")).convert_alpha()
pygame.display.set_icon(icon_image)
pygame.display.set_caption("SpaceWars.py")

# Background Image
background_image = pygame.image.load(join("assets", "Background.jpg")).convert_alpha()
background_image = pygame.transform.scale(
    background_image, (WINDOW_WIDTH, WINDOW_HEIGHT)
)
background_image_rect = background_image.get_frect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
)

# Laser
laser_image = pygame.image.load(join("assets", "Laser.png")).convert_alpha()
laser_image = pygame.transform.scale(laser_image, (15, 75))

# Asteroids
asteroid_image_1 = pygame.image.load(join("assets", "asteroid1.png")).convert_alpha()
asteroid_image_1 = pygame.transform.scale(asteroid_image_1, (100, 100))
asteroid_image_2 = pygame.image.load(join("assets", "asteroid2.png")).convert_alpha()
asteroid_image_2 = pygame.transform.scale(asteroid_image_2, (80, 80))

# Font
score = 0
game_font = pygame.font.Font(join("font", "04B_30__.TTF"), 25)


# Spawns Asteroids at Custom Intervals
asteroid_event = pygame.event.custom_type()
pygame.time.set_timer(asteroid_event, 1200)

# Sprite Groups
all_sprites = pygame.sprite.Group()
asteroid_sprite = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()

# Player Creation
player = Player(all_sprites)

while running:
    delta = clock.tick(240) / 1000  # Return Value by default is ms, converted to s

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Asteroid Spawn
        if event.type == asteroid_event:
            if randint(0, 1):
                Asteroid(
                    asteroid_image_1,
                    (randint(0, WINDOW_WIDTH), 0),
                    600,
                    (all_sprites, asteroid_sprite),
                )
            else:
                Asteroid(
                    asteroid_image_2,
                    (randint(0, WINDOW_WIDTH), 0),
                    350,
                    (all_sprites, asteroid_sprite),
                )

    # Update
    all_sprites.update(delta)

    # Collision
    collision()

    # Display loop
    display_surface.fill((20, 40, 48))
    display_surface.blit(background_image, background_image_rect)

    # Score
    display_score()
    # Drawing Elements to Screen
    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()
