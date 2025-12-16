import pygame
from scripts.entities.TileFactory import TileFactory
from scripts.systems.CameraSystem import CameraSystem
from scripts.systems.Input import Inputs
from scripts.systems.MovementUpdates import Movement
from scripts.systems.Renderer import Renderer
from scripts.entities.EntityManager import EntityManager
from scripts.components.Components import Acceleration, CameraOffset, Position, Sprite, SpriteSheet, Velocity
from scripts.systems.animations.animation import AnimationSystem


class Context:
    def __init__(self):
        self.entity_manager = EntityManager()
        self.movement = Movement()
        self.renderer = Renderer()
        self.inputs = Inputs()
        self.camera_system = CameraSystem()
        self.tile_factory = TileFactory()
        self.animation_system = AnimationSystem()

        self.player = self.entity_manager.create()
        self.entity_manager.add_components(
            self.player,
            Position(pygame.Vector2(x=200, y=100)),
            Velocity(),
            Acceleration(pygame.Vector2(0,0)),
            SpriteSheet("assets\mystic_woods_free_2.2\sprites\characters\player.png"
                                                            , 6, 7, 48, 0.12)
        )
        self.animation_system.load_sprites(self.entity_manager)
        self.tile_factory.populate_map(self.entity_manager)
        self.camera = self.entity_manager.create()
        self.entity_manager.add_components(self.camera, CameraOffset(), Position())
 


    
