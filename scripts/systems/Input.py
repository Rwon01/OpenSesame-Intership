import pygame

from scripts.components.Components import Acceleration, SpriteSheet, State
from scripts.entities.EntityManager import EntityManager
import random as rand


class Inputs:
    def process_inputs(self, keys, entity_manager: EntityManager):
        acc = entity_manager.get(0, Acceleration).acc
        sheet = entity_manager.get(0, SpriteSheet)
        
        speed = 2000
        acc.x = 0
        acc.y = 0

        if keys[pygame.K_a]:
            acc.x -= speed
            
        if keys[pygame.K_d]:
            acc.x += speed

        if keys[pygame.K_w]:
            acc.y -= speed

        if keys[pygame.K_s]:
            acc.y += speed

        choices = [State.IDLE_DOWN, State.IDLE_LEFT, State.IDLE_RIGHT, State.IDLE_UP, 
                   State.WALK_UP, State.WALK_DOWN, State.WALK_LEFT, State.WALK_RIGHT]
        if keys[pygame.K_1]:
            sheet.current_state = State.WALK_DOWN
            
