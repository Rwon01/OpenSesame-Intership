import pygame

from scripts.components.Components import Acceleration, CameraOffset, Position, Sprite, Velocity
from scripts.entities.EntityManager import EntityManager
from scripts.entities.settings import SCREEN_HEIGHT, SCREEN_WIDTH

OFFSET = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

class CameraSystem:

    def update_camera(self, entity_manager: EntityManager, dt):

        camera_comps = None
        player_comps = None

        for eid, comps in entity_manager.entities_with(CameraOffset, Position):
            camera_comps = comps
            break

        for eid, comps in entity_manager.entities_with(Position, Velocity, Acceleration):
            player_comps = comps
            break
        
        camera_offset = camera_comps[CameraOffset].offset
        player_position = player_comps[Position].pos

        target_offset = player_position - pygame.Vector2(OFFSET) + pygame.Vector2(0,2*48)
        camera_offset += (target_offset - camera_offset) * 5 * dt