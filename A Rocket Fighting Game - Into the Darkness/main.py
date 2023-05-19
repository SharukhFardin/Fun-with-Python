import pygame
import random
import math
from pygame import mixer

# initializing Pygame
pygame.init()

# Deciding the screen size
screen = pygame.display.set_mode((800, 600))

# Title, Icon, Background
pygame.display.set_caption(" Into the Darkness")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Background.jpg")

# Add Music
mixer.music.load('background_music.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

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
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 5

for e in range(number_of_enemies):
    img_enemy.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(0.3)
    enemy_y_change.append(50)

'''
def summon_enemy():
    enemy_x = random.randint(0, 736)
    enemy_y = random.randint(50, 200)
    
    return enemy_x, enemy_y
'''


def enemy(x, y, en):
    screen.blit(img_enemy[en], (x, y))


# Bullet Variables
img_bullet = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 2.5
visible_bullet = False

# Score
score = 0
my_font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10


# show score function
def show_score(x,y):
    text = my_font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (x, y))


# Shoot Bullet
def shoot_bullet(x, y):
    global visible_bullet
    visible_bullet = True
    screen.blit(img_bullet, (x + 16, y + 10))


# Detect Collision Function
def there_is_a_collision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x2-x1, 2) +math.pow(y2-y1, 2))
    if distance < 27:
        return True
    else:
        return False


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
                player_x_change = -0.4
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.4
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('shot.mp3')
                bullet_sound.play()
                if not visible_bullet:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)

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
    for enem in range(number_of_enemies):
        enemy_x[enem] += enemy_x_change[enem]

        # Keeping Enemy inside screen
        if enemy_x[enem] <= 0:
            enemy_x_change[enem] = 0.3
            enemy_y[enem] += enemy_y_change[enem]
        elif enemy_x[enem] >= 736:
            enemy_x_change[enem] = -0.3
            enemy_y[enem] += enemy_y_change[enem]

        # Collision
        collision = there_is_a_collision(enemy_x[enem], enemy_y[enem], bullet_x, bullet_y)
        if collision:
            collision_sound = mixer.Sound('punch.mp3')
            collision_sound.play()
            bullet_y = 500
            visible_bullet = False
            score += 1
            enemy_x[enem] = random.randint(0, 736)
            enemy_y[enem] = random.randint(50, 200)

        # Calling Enemy
        enemy(enemy_x[enem], enemy_y[enem], enem)
    '''
    elif enemy_y >= 400:
        enemy_y_change = -0.3
        enemy_y += enemy_y_change
    '''

    # Bullet Movement
    if bullet_y <= -64:
        bullet_y = 500
        visible_bullet = False
    if visible_bullet:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # calling the player
    player(player_x, player_y)

    # Show Score
    show_score(text_x, text_y)

    # updating the game
    pygame.display.update()
