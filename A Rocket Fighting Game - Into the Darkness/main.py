import pygame
import random

# initializing Pygame
pygame.init()

# Deciding the screen size
screen = pygame.display.set_mode((800, 600))

# Title, Icon, Background
pygame.display.set_caption(" Into the Darkness")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Background.jpg")

# Player variables
img_player = pygame.image.load("rocket.png")
player_x = 368
player_y = 500
player_x_change = 0
#player_y_change = 0


# Player function
def player(x, y):
    screen.blit(img_player, (x, y))


# Enemy variables
img_enemy = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 200)
enemy_x_change = 0.3
enemy_y_change = 50


def enemy(x, y):
    screen.blit(img_enemy, (x, y))


# Bullet Variables
img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 1
visible_bullet = False


# Shoot Bullet
def shoot_bullet(x, y):
    global visible_bullet
    visible_bullet = True
    screen.blit(img_bullet, (x + 16, y + 10))


# Detect Collision Function

# Game loop
is_running = True
while is_running:
    # changing screen color
    # screen.fill((90, 20, 20))

    # Setting up Background Image
    screen.blit(background, (0, 0))

    # Even Iteration Happens here
    for event in pygame.event.get():
        # Pressing X will close the Event
        if event.type == pygame.QUIT:
            is_running = False

        # Pressing key event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_SPACE:
                shoot_bullet(player_x, bullet_y)

        # Releasing arrow key event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player_x_change = 0

    # Modify Player location
    player_x += player_x_change

    # Keeping rocket inside screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Modify Enemy location
    enemy_x += enemy_x_change

    # Keeping Enemy inside screen
    if enemy_x <= 0:
        enemy_x_change = 0.3
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.3
        enemy_y += enemy_y_change
    elif enemy_y >= 400:
        enemy_y_change = -0.3
        enemy_y += enemy_y_change

    # Bullet Movement
    if visible_bullet:
        shoot_bullet(player_x, bullet_y)
        bullet_y -= bullet_y_change

    # calling the player/ Enemy
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    # updating the game
    pygame.display.update()
