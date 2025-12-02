import time
import pygame

from ecs.components.MovementComp import *
from ecs.entities.EntityManager import EntityManager
from ecs.systems.RenderSystem import RenderSystem

exit = False

pygame.init()
size = (1200,600)

em = EntityManager()
rendersystem = RenderSystem()
movement = None


clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
grass = pygame.image.load("assets\grass.png").convert_alpha()

player = em.create()
em.add_component(player, Position(375, 275))
em.add_component(player, Velocity(0, 0))
em.add_component(player, Sprite(grass))


while not exit:
    screen.fill('WHITE')
    dt = clock.tick(60) / 1000

    rendersystem.update(screen, em)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.flip()