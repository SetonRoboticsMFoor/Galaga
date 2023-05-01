import pygame
import Constants as c
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('Images/enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/8, self.image.get_height()/ 8))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.vel_x = 0
        self.vel_y = random.randrange(3,8)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
