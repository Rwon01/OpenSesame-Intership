import pygame

from ecs.components.MovementComps import Position, Sprite
from ecs.entities.EntityManager import EntityManager


class RenderSystem:
    
    def update(self, screen, entitymanager: EntityManager):

        for eid, comps in entitymanager.entities_with(Position, Sprite):
            pos = comps[Position]
            sprite = comps[Sprite]
            screen.blit(sprite.surface, (pos.x, pos.y))

