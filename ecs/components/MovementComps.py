import pygame

class Position:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Velocity:
    def __init__(self, vx=0, vy=0):
        self.vx = vx
        self.vy = vy

class Input:
    def __init__(self, can_jump = False):
        self.can_jump = can_jump    


class Sprite(pygame.sprite.Sprite):
    def __init__(self, surface):
        self.surface = surface
