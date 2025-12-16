from enum import Enum, auto
import pygame
from scripts.entities.settings import TILE_SIZE

class Position:
    def __init__(self, pos=None):
        if pos is None:
            self.pos = pygame.Vector2(0, 0)
        else:
            self.pos = pygame.Vector2(pos)

class Velocity:
    def __init__(self, pos=None):
        if pos is None:
            self.vel = pygame.Vector2(0, 0)
        else:
            self.vel = pygame.Vector2(pos)

class Acceleration:
    def __init__(self, pos=None):
        if pos is None:
            self.acc = pygame.Vector2(0, 0)
        else:
            self.acc = pygame.Vector2(pos)

class Sprite:
    def __init__(self, image_surface=None, image_path='assets/dirt.png', size=TILE_SIZE):
        if image_surface is None:
            img = pygame.image.load(image_path).convert_alpha()
            img = pygame.transform.scale(img, size)
            self.image = img
        else:
            self.image = pygame.transform.scale(image_surface, size)

        self.rect = self.image.get_rect()

class CameraOffset:
    def __init__(self, offset: pygame.Vector2 = pygame.Vector2(0,0)):
        self.offset = offset

class State(Enum):
    IDLE_UP = auto()
    IDLE_DOWN = auto()
    IDLE_RIGHT = auto()
    IDLE_LEFT = auto()

    WALK_UP = auto()
    WALK_DOWN = auto()
    WALK_RIGHT = auto()
    WALK_LEFT = auto()

class SpriteSheet:

    def __init__(self, file_name, columns, rows, size, frame_time=0.5):
        self.file_name = file_name
        self.image = pygame.image.load(file_name).convert()
        self.columns = columns
        self.rows = rows
        self.size = size
        self.current_frame = 0
        self.animations = {}
        self.current_state = None
        self.timer = 0
        self.frame_time = frame_time
        


        