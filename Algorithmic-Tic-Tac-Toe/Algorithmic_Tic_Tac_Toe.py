import pygame

pygame.init()

_WIDTH = 800
_HEIGHT = 600

_DISPLAY = pygame.display.set_mode((_WIDTH, _HEIGHT))

game_end = False

while not game_end:
    for event in pygame.event.get():
        print(event)