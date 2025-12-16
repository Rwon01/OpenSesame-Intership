import pygame
import os


from scripts.systems import *
from scripts.entities.EntityManager import EntityManager
from scripts.components.Components import Position, Sprite, Velocity
from scripts.systems.GameContext import Context



class Game():

    def __init__(self):
        pygame.init()
        os.environ['SDL_VIDEO_CENTER'] = '1'
        self.screen = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
        
        pygame.display.set_caption("Scroller")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial Black", 32)
        self.running = True
        self.ctx = Context()


    def run(self):
        
        while self.running:
            self.screen.fill("white")
            dt = self.clock.tick(60) / 1000

            keys = pygame.key.get_pressed()

            self.ctx.inputs.process_inputs(keys, self.ctx.entity_manager)
            self.ctx.movement.update_positions(self.ctx.entity_manager, dt)
            self.ctx.camera_system.update_camera(self.ctx.entity_manager, dt)
            self.ctx.animation_system.update(dt, self.ctx.entity_manager)
            self.ctx.renderer.render(self.screen, self.ctx.entity_manager)            
            

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


if __name__ == "__main__":
    game = Game()
    game.run()


