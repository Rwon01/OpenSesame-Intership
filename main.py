import pygame

exit = False

pygame.init()
size = (1200,600)
screen = pygame.display.set_mode(size)

grass = pygame.image.load("assets\grass.png").convert_alpha()

while not exit:

    screen.fill((0,0,0))
    screen.blit(grass, (120,120))
    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True