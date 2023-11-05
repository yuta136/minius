import pygame
from pygame import FULLSCREEN, mixer
import random
import math

pygame.init()

is_fullscreen = False
screen = pygame.display.set_mode((800, 650))

#screen.fill((100,0,100))
pygame.display.set_caption('inveaders game')

#score
score_value = 0

#player
playerimg = pygame.image.load('player.png')
playerX,playerY= 370,500
playerX_change = 0
playerY_change = 0

# Enemy
enemyimg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change, enemyY_change = 3, 10

#bullet
bulletimg = pygame.image.load('bullet.png')
bulletX,bulletY = 370,500
bulletX_change,bulletY_change = 0,3
bullet_state = 'ready'
bullet_delay = 0
bullet_delay_max = 15

#game_over
game_over = False

#mixer.Sound('laser.wav').play()

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y):
    screen.blit(enemyimg,(x,y))

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
    distance = math.sqrt(math.pow(playerX - enemyX, 2) + math.pow(playerY - enemyY, 2))
    if distance < 35:
        return True
    else:
        return False
   



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
                playerX_change =0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = -0.5
            if event.key == pygame.K_UP:
               playerY_change = -0.3
            if event.key == pygame.K_DOWN:
              playerY_change = 0.3    

            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready' and bullet_delay == 0:
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
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >=735: 
        enemyX_change = -1
        enemyY += enemyY_change    

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)
    enemy(enemyX, enemyY)
    

# Bullet Movement

    if bulletY <=0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_delay > 0:
        bullet_delay -= 1    

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change  

    #score
    font = pygame.font.SysFont(None, 50)
    score =font.render(f'score : {str(score_value)}',True,(250,50,100))
    screen.blit(score,(10,15))

    #game_over
    collision_with_player = isPlayerCollision(playerX, playerY, enemyX, enemyY)
    if collision_with_player:
      game_over = True

    if game_over:
        font = pygame.font.SysFont(None, 100)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (250, 250))
        pygame.display.update()
        pygame.time.delay(3000) 
        running = False 


    player(playerX,playerY)
    enemy(enemyX,enemyY)
    
    pygame.display.update()

