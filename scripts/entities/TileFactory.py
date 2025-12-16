import pygame
from scripts.entities.Map import map_data
from scripts.components.Components import *
from scripts.entities.EntityManager import EntityManager
from scripts.entities.settings import TILE_SIZE
import random as rand
choices = [0, 90, 180, 270]

class TileFactory:
    
    def __init__(self):

        self.stone_surf = pygame.image.load("assets/stone.jpg").convert_alpha()
        self.stone_surf = pygame.transform.scale(self.stone_surf, TILE_SIZE)

        self.grass_surf = pygame.image.load("assets/grass.png").convert_alpha()


    def populate_map(self, entity_manager: EntityManager):
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                img = self.stone_surf if tile == 1 else pygame.transform.rotate(self.grass_surf, rand.choice(choices))
                #img = self.stone_surf if tile == 1 else self.grass_surf
                self.create_tile_entity(entity_manager, img=img, pos=(x*TILE_SIZE[0], y*TILE_SIZE[1]))

        

    def create_tile_entity(self, entity_manager: EntityManager, img, pos):
        tile = entity_manager.create()
        entity_manager.add_components(
            tile,
            Position(pos),
            Sprite(image_surface=img)
        )

    

