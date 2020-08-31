import pygame
import sys

pygame.init()

_WIDTH = 800
_HEIGHT = 800

screen = pygame.display.set_mode((_WIDTH, _HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Import and rescale images
scale_img_x = int(_WIDTH / 4)
scale_img_y = int(_HEIGHT / 4)

x_move = pygame.image.load("img/x.png")
x_move = pygame.transform.scale(x_move, (scale_img_x , scale_img_y))
o_move = pygame.image.load("img/o.png")
o_move = pygame.transform.scale(o_move, (scale_img_x , scale_img_y))

board = [[None] * 3, [None] * 3, [None] * 3]

# Initialize game board to blank
def init_board():
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

    # Update screen with background
    screen.blit(background, (0, 0))
init_board()

# Check board for winner
def check_board():
    global board

# Draw current state of the board
def draw_board():

    init_board()

    global board

    for x_index in range(0, 3):
            for y_index in range(0, 3):
                if board[x_index][y_index] is not None:
                    if board[x_index][y_index]:
                        screen.blit(x_move, (x - scale_img_x / 2, y - scale_img_y / 2))
                    else:
                        screen.blit(o_move, (x - scale_img_x / 2, y - scale_img_y / 2))


# Debug function to test mouse drawing
move = False
def test_draw():
    global move
    x, y = pygame.mouse.get_pos()
    if move:
        screen.blit(o_move, ((3/6) * _WIDTH - scale_img_x / 2, (1/6) * _HEIGHT - scale_img_y / 2))
    else:
        screen.blit(x_move, ((3/6) * _WIDTH - scale_img_x / 2, (1/6) *  _HEIGHT - scale_img_y / 2))
    move = not move


game_end = False

while not game_end:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit(0)

        # If event is mouseclickup
        elif event.type == 6:
            test_draw()

        pygame.display.flip()

        print(event.type)

    
    pygame.display.update()