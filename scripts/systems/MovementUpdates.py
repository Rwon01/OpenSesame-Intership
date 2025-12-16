from scripts.entities.EntityManager import EntityManager
from scripts.components.Components import Acceleration, CameraOffset, Position, Sprite, SpriteSheet, Velocity
from scripts.entities.settings import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
FRICTION = 0.80


class Movement():

    def update_positions(self, entity_manager: EntityManager, dt):

        for eid, comps in entity_manager.entities_with(SpriteSheet, Position, Velocity, Acceleration):

            position = comps[Position].pos
            velocity = comps[Velocity].vel
            acceleration = comps[Acceleration].acc

            velocity.x += acceleration.x * dt * 2
            velocity.y += acceleration.y * dt * 2
            
            max_speed = 2200
            if velocity.length() > max_speed:
                velocity.scale_to_length(max_speed)

            position.x += velocity.x * dt
            position.y += velocity.y * dt

            velocity.x *= FRICTION
            velocity.y *= FRICTION




        



            