import pygame

from scripts.entities.EntityManager import EntityManager
from scripts.components.Components import CameraOffset, Position, Sprite, SpriteSheet


class Renderer():
    
    def render(self, screen: pygame.surface.Surface, entity_manager: EntityManager):
        
        
        render_ids = [eid for eid, _ in entity_manager.entities_with(Position, Sprite)]
        render_ids.sort(key= lambda eid: entity_manager.get(eid, Position).pos.y, reverse=True)
        
        camera_offset = pygame.Vector2(0, 0)


        for _, comps in entity_manager.entities_with(CameraOffset, Position):
            camera_offset = comps[CameraOffset].offset
            break

        for eid in render_ids:
            pos = entity_manager.get(eid, Position).pos
            sprite = entity_manager.get(eid, Sprite).image
            screen.blit(sprite, (pos.x - camera_offset.x, 
                                 pos.y - camera_offset.y))
            
        for eid, comps in entity_manager.entities_with(SpriteSheet, Position):
            sheet = comps[SpriteSheet]
            pos = comps[Position].pos
            frame = sheet.animations[sheet.current_state][sheet.current_frame]
            screen.blit(frame, (pos.x - camera_offset.x, pos.y - camera_offset.y))


