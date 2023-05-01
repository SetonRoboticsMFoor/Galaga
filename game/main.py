import pygame
from Ship import Ship
import Constants as c
from Background import BG
from EnemySpawner import EnemySpawner


# display setup
display = pygame.display.set_mode(c.DISPLAY_SIZE)
fps = 60
clock = pygame.time.Clock()
black = (0,  0,  0)

#bg setup
bg = BG()
bg_group = pygame.sprite.Group(bg)
#bg_group.add(bg)
player = Ship()
sprite_group = pygame.sprite.Group(player)
#sprite_group.add(player)
enemy_spawner = EnemySpawner()


running = True
while running:
    clock.tick(fps)  # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.vel_x = -player.speed
            elif event.key == pygame.K_RIGHT:
                player.vel_x = player.speed
            elif event.key == pygame.K_UP:
                player.vel_y = -player.speed
            elif event.key == pygame.K_DOWN:
                player.vel_y = player.speed
            if event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.vel_x = 0
            elif event.key == pygame.K_RIGHT:
                player.vel_x = 0
            elif event.key == pygame.K_UP:
                player.vel_y = 0
            elif event.key == pygame.K_DOWN:
                player.vel_y = 0

    # handle events

    # tick the Clock
    clock.tick(fps)

    # handle events

    # update all the objects
    bg_group.update()
    sprite_group.update()
    enemy_spawner.update()

    # render the display
    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    pygame.display.update()



