import pygame
from Bullet import Bullet
import Constants


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self). __init__()
        self.image = pygame.image.load('spaceshipsmall__1_-removebg-preview.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2/4, self.image.get_height()*2/4))
        self.rect = self.image.get_rect()
        self.rect.x = Constants.DISPLAY_WIDTH / 2 #####
        self.rect.y = Constants.DISPLAY_HEIGHT - self.rect.height #######moved these up
        self.bullets = pygame.sprite.Group()
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5


    def update(self):
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self.rect.x += self.vel_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= Constants.DISPLAY_WIDTH - self.rect.width:
            self.rect.x =   Constants.DISPLAY_WIDTH
        self.rect.y += self.vel_y

    def shoot(self):
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + (self.rect.width // 2) - 1
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)
