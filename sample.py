import pygame
import sys
from pygame import FULLSCREEN, mixer
import random
import math
from player import *
from enemy import *


pygame.init()

is_fullscreen = False
screen = pygame.display.set_mode((800, 650))

#screen.fill((100,0,100))
pygame.display.set_caption('inveaders game')

#score
score_value = 0

#bullet
bulletimg = pygame.image.load('bullet.png')
bulletX,bulletY = 370,500
bulletX_change,bulletY_change = 0,2
bullet_state = 'ready'
bullet_delay = 0
bullet_delay_max = 15

enemy_bullet_img = pygame.image.load('enemy_bullet.png')
enemy_bulletX = 0
enemy_bulletY = 0
enemy_bulletX_change = 0
enemy_bulletY_change = 0.8
enemy_bullet_state = 'ready'

#life
player_life_value = 500

#flag
# hit  : 1
# not hit : 0
collision_flag = 0

invincible_time = 60

invincible_timer = 0

#game_over
game_over = False

#mixer.Sound('laser.wav').play()

def fire_bullet(x,y):
    global bullet_state
    bullet_state ='fire'
    screen.blit (bulletimg,(x + 16,y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance =   math.sqrt(math.pow(enemyX - bulletX,2) + math.pow(enemyY - bulletY,2))  
    if distance < 27:
        return True
    else:
        return False
    
def isPlayerCollision(playerX, playerY, enemyX, enemyY):
    global collision_flag
    distance = math.sqrt(math.pow(playerX - enemyX, 2) + math.pow(playerY - enemyY, 2))
    if distance < 35:
        if collision_flag == 0:
            collision_flag = 1
            return True
        
        if collision_flag == 1:
            return False

    else:
        if collision_flag == 1:
            collision_flag = 0
            return False
    
def fire_enemy_bullet(x, y):
    global enemy_bullet_state
    enemy_bullet_state = 'fire'
    screen.blit(enemy_bullet_img, (x, y))

   



running = True
while running:
    screen.fill((0,0,150))
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if bullet_delay > 0:
    #     bullet_delay -= 1

    # for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change =0.45
            if event.key == pygame.K_RIGHT:
                playerX_change = -0.45
            if event.key == pygame.K_UP:
               playerY_change = -0.3
            if event.key == pygame.K_DOWN:
              playerY_change = 0.3    

            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready' and bullet_delay == 0:
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX,bulletY)
                    bullet_state = 'fire'
                    bullet_delay = bullet_delay_max

        

            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RSHIFT:
                    is_fullscreen =not is_fullscreen
                    if is_fullscreen:
                        screen = pygame.display.set_mode((800, 650), pygame.FULLSCREEN)
                    else:
                         screen = pygame.display.set_mode((800, 650))       

           
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0    
   
    playerX -= playerX_change
    if playerX <=0:
      playerX =0
    elif playerX >=735:
       playerX = 735
    playerY += playerY_change
    if playerY<=0:
        playerY =0
    elif playerY >=560:
        playerY = 560    

    # Enemy
    if enemyY > 440:
        enemyY_change
    enemyX += enemyX_change
    if enemyX <= 0: 
        enemyX_change = 0.7
        enemyY += enemyY_change
    elif enemyX >=735: 
        enemyX_change = -0.7
        enemyY += enemyY_change    

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score_value += 10
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)
    enemy(enemyX, enemyY)

    if enemy_bullet_state == 'ready':
       if random.randint(0, 100) < 1:  
        enemy_bulletX = enemyX 
        enemy_bulletY = enemyY  
        fire_enemy_bullet(enemy_bulletX, enemy_bulletY)

    if enemy_bullet_state == 'fire':
        enemy_bulletY += enemy_bulletY_change
    screen.blit(enemy_bullet_img, (enemy_bulletX, enemy_bulletY))

    collision_with_player = isPlayerCollision(playerX, playerY, enemy_bulletX, enemy_bulletY)
    if collision_with_player:
        player_life_value -= 1
        sys.stdout.write(f"\n life: {player_life_value}")
        
        
        if player_life_value < 0:
            game_over = True
        

    if enemy_bulletY >= 650: 
        enemy_bullet_state = 'ready'

    if invincible_timer > 0:
        invincible_timer -= 1

    
    
    
    

    

# Bullet Movement

    if bulletY <=0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_delay > 0:
        bullet_delay -= 1    

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change  

    #score
    font = pygame.font.SysFont(None, 50)
    score =font.render(f'score : {str(score_value)}',True,(250,50,100))
    screen.blit(score,(10,15))

    #player_life
    player_life =font.render(f'life : {str(player_life_value)} flag : {str(collision_flag)}',True,(250,50,100))
    screen.blit(player_life,(10,80))

    #game_over
    collision_with_player = isPlayerCollision(playerX, playerY, enemyX, enemyY)
    if collision_with_player:
      #game_over = True

    #   if collision_with_player:  
        player_life -= 1
        
        if player_life == 0:
            game_over = True


    #collision_with_player = isPlayerCollision(playerX, playerY, enemy_bulletX, enemy_bulletY)
    # if collision_with_player and invincible_timer == 0:
    #   player_life -= 1
    # if player_life == 0:
    #     game_over = True
    # else:
    #     invincible_timer = invincible_time

    # if invincible_timer == 0:
    #     if collision_with_player:  
    #           player_life -= 1
    #     if player_life == 0:
    #         game_over = True
    #     else:
    #         invincible_timer = invincible_time
    
    

    if game_over:
        font = pygame.font.SysFont(None, 100)
        game_over_text = font.render("Game Over ", True, (255, 0, 0))
        screen.blit(game_over_text, (250, 250))
        pygame.display.update()
        pygame.time.delay(3000) 
        running = False 


    player(playerX,playerY)
    enemy(enemyX,enemyY)
    
    pygame.display.update()

