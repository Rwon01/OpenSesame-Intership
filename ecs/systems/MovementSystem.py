
import pygame
from ecs.entities.EntityManager import EntityManager
from ecs.components.MovementComps import *

class MovementSystem:

    max_speed = 100

    def process_movement(self, keys, dt, entitymanager: EntityManager):
        
        for eid, comps in entitymanager.entities_with(Position, Velocity, Input):
            vel = comps[Velocity]
            pos = comps[Position]
            input = comps[Input]

            if keys[pygame.K_a]:
                vel.vx += -100
            if keys[pygame.K_d]:
                vel.vx += 100
            vel.vx = vel.vx * 0.85

            if keys[pygame.K_0]:
                pos.y = 100

            if keys[pygame.K_w] or keys[pygame.K_SPACE] and input.can_jump:
                input.can_jump = False
                vel.vy = -500
               
            vel.vy += 1500 * dt
            pos.y += vel.vy * dt
            pos.x += vel.vx * dt
