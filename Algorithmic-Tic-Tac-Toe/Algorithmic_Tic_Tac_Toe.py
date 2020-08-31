import pygame
import sys

pygame.init()

_WIDTH = 800
_HEIGHT = 600

screen = pygame.display.set_mode((_WIDTH, _HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

border = pygame.draw.rect(background, (0, 0, 0), (0, 0, _WIDTH, _HEIGHT), 5)

screen.blit(background, (0, 0))

game_end = False

while not game_end:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit(0)

        pygame.display.flip()

        print(event)

    
    pygame.display.update()