
import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

FONT = pygame.font.SysFont('Verdana', 20)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_ENEMY = (255, 0, 0)
COLOR_BONUS = (125, 125, 0)

main_display = pygame.display.set_mode(( WIDTH, HEIGHT))

bg = pygame.transform.scale( pygame.image.load('background.png'), (WIDTH, HEIGHT) )
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

# FOR PLAYER
player_size = (20, 20)
player = pygame.image.load('player.png').convert_alpha()
# player.fill(COLOR_BLACK)
player_rect = player.get_rect()
player_move_down = [0, 3]
player_move_up = [0, -3]
player_move_right = [3, 0]
player_move_left = [-3, 0]
# FOR ENEMIES
def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.image.load('enemy.png').convert_alpha()
    # enemy.fill(COLOR_ENEMY)
    enemy_rect = pygame.Rect(WIDTH, random.randint(200, HEIGHT-200) , *enemy_size)
    enemy_move = [random.randint(-6, -4), 0]
    return [enemy, enemy_rect, enemy_move]
# FOR BONUSES
def create_bonus():
    bonus_size = (30, 30)
    bonus = pygame.image.load('bonus.png').convert_alpha()
    # bonus.fill(COLOR_BONUS)
    bonus_rect = pygame.Rect(random.randint(200, HEIGHT-200), 0, *bonus_size)
    bonus_move = [ 0, random.randint(4, 6)]
    return [bonus, bonus_rect, bonus_move]

CREATE_ENEMY = pygame.USEREVENT +1
CREATE_BONUS = CREATE_ENEMY +1

pygame.time.set_timer(CREATE_ENEMY, 1000)
enemies = []

pygame.time.set_timer(CREATE_BONUS, 1000)
bonuses = []

score = 0
playing = True

while playing:
    FPS.tick(250)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False 
        if event.type == CREATE_ENEMY:
           enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
           bonuses.append(create_bonus())
    
    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()
    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()
    
    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)
   
    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)
   
    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right) 

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left) 

    for enemy in enemies:

        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
        if player_rect.colliderect(enemy[1]):
            playing = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))
  
    main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH-50, 20))            
    main_display.blit(player, player_rect)  

   
    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
  
    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
     # if player_rect.bottom >= HEIGHT:
    #     player_speed = random.choice(([1, -1], [-1,-1]))
    # if player_rect.right >= WIDTH:
    #     player_speed = random.choice(([1, -1], [-1,-1]))
    # if player_rect.top < 0:
    #     player_speed = random.choice(([-1, -1], [-1,1]))
    # if player_rect.left < 0:
    #     player_speed = random.choice(([1, 1], [1,-1]))
    # player_rect = player_rect.move(player_speed)

    

