import pygame
from scripts.entities.EntityManager import EntityManager
from scripts.entities.settings import TILE_SIZE
from scripts.components.Components import SpriteSheet, Velocity, State


class AnimationSystem:

    def __init__(self):
        pass
    
    def load_sprites(self, em: EntityManager):
        for eid, comps in em.entities_with(SpriteSheet):
            sheet = comps[SpriteSheet]
            sheet.current_state = State.IDLE_LEFT
            def grab(col, row, is_flipped = False):
                surf = pygame.Surface((sheet.size, sheet.size)).convert()
                surf.set_colorkey((0,0,0))
                surf.blit(
                    sheet.image,
                    (0, 0),
                    (col * sheet.size, row * sheet.size, sheet.size, sheet.size)
                )
                
                s = pygame.transform.scale(
                    surf,
                    (TILE_SIZE[0]*2, TILE_SIZE[1]*2)
                )

                if not is_flipped: 
                    return s
                else:
                    return pygame.transform.flip(s, True, False)
           
                    
            sheet.animations[State.IDLE_DOWN] = [
                    grab(col, 0) for col in range(sheet.columns)
                ]
    
            sheet.animations[State.IDLE_UP] = [
                    grab(col, 2) for col in range(sheet.columns)
                ]
    
            sheet.animations[State.IDLE_RIGHT] = [
                    grab(col, 1) for col in range(sheet.columns)
                ]
    
            sheet.animations[State.IDLE_LEFT] = [
                    grab(col, 1, True) for col in range(sheet.columns)
                ]
            
            #WALKING
            sheet.animations[State.WALK_UP] = [
                    grab(col, 5) for col in range(sheet.columns)
                ]
    
            sheet.animations[State.WALK_DOWN] = [
                    grab(col, 3) for col in range(sheet.columns)
                ]
    
            sheet.animations[State.WALK_RIGHT] = [
                    grab(col, 4) for col in range(sheet.columns)
                ]
    
            sheet.animations[State.WALK_LEFT] = [
                    grab(col, 4, True) for col in range(sheet.columns)
                ]
            
    

    def update(self, dt, em: EntityManager):
            
            for eid, comps in em.entities_with(SpriteSheet, Velocity):
                sheet = comps[SpriteSheet]
                vel = comps[Velocity].vel
                
               

        # --- Determine state ---
                if vel.length_squared() < 0.9:
                    if sheet.current_state in (State.WALK_UP, State.IDLE_UP):
                        new_state = State.IDLE_UP
                    elif sheet.current_state in (State.WALK_RIGHT, State.IDLE_RIGHT):
                        new_state = State.IDLE_RIGHT
                    elif sheet.current_state in (State.WALK_LEFT, State.IDLE_LEFT):
                        new_state = State.IDLE_LEFT
                    else:
                        new_state = State.IDLE_DOWN
                else:
                    if abs(vel.x) > abs(vel.y):
                        new_state = State.WALK_RIGHT if vel.x > 0 else State.WALK_LEFT
                    else:
                        new_state = State.WALK_DOWN if vel.y > 0 else State.WALK_UP

                if new_state != sheet.current_state:
                    sheet.current_state = new_state
                    sheet.current_frame = 0
                    sheet.timer = 0
                
                sheet.timer += dt
                if sheet.timer >= sheet.frame_time:
                    sheet.timer = 0
                    frames = sheet.animations[sheet.current_state]
                    sheet.current_frame = (sheet.current_frame + 1) % len(frames)




            
                


        

             

