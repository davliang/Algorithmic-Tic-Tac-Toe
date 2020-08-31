import pygame
import sys

pygame.init()

_WIDTH = 800
_HEIGHT = 800

screen = pygame.display.set_mode((_WIDTH, _HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Set background color to white
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

# Draw black border around game board
border_color = (0, 0, 0)
border_location = (0, 0, _WIDTH, _HEIGHT)
border = pygame.draw.rect(background, border_color, border_location, 5)

# Draw crossing game board
pygame.draw.line(background, (0, 0, 0), ((1/3) * _WIDTH, 25), ((1/3) * _WIDTH, _HEIGHT - 25), 2)
pygame.draw.line(background, (0, 0, 0), ((2/3) * _WIDTH, 25), ((2/3) * _WIDTH, _HEIGHT - 25), 2)
pygame.draw.line(background, (0, 0, 0), (25, (1/3) * _HEIGHT), (_WIDTH - 25, (1/3) * _HEIGHT), 2)
pygame.draw.line(background, (0, 0, 0), (25, (2/3) * _HEIGHT), (_WIDTH - 25, (2/3) * _HEIGHT), 2)

def check_board():
    global board

screen.blit(background, (0, 0))

game_end = False

while not game_end:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit(0)

        pygame.display.flip()

        print(event)

    
    pygame.display.update()