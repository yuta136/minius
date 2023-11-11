# player.py
import pygame
screen = pygame.display.set_mode((800, 650))

playerimg = pygame.image.load('player.png')
playerX,playerY= 370,500
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerimg, (x, y))
