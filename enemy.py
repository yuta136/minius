# enemy.py
import pygame
import random
screen = pygame.display.set_mode((800, 650))

enemyimg = pygame.image.load('enemy.png')

def enemy(x,y):
    screen.blit(enemyimg,(x,y))
    
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 10



def randomize_enemy_position():
    return random.randint(0, 736), random.randint(50, 150)
