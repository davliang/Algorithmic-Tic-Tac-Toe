import pygame
import sys
from itertools import chain
from random import randint
import math

pygame.init()

_WIDTH = 800
_HEIGHT = 800

screen = pygame.display.set_mode((_WIDTH, _HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Import and rescale images
scale_img_x = int(_WIDTH / 4)
scale_img_y = int(_HEIGHT / 4)
x_move = pygame.transform.scale(pygame.image.load("img/x.png"), (scale_img_x , scale_img_y))
o_move = pygame.transform.scale(pygame.image.load("img/o.png"), (scale_img_x , scale_img_y))

# Initialize players (Human is True, Computer is False)
player_turn = True
can_move = True

# Initialize game board to blank
def init_board():

    # Reset game board
    global board
    board = [[None] * 3, [None] * 3, [None] * 3]

    # Reset turns and player move
    global player_turn
    global can_move
    player_turn = True
    can_move = True

    # Set background color to white
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    # Draw black border around game board
    border_color = (0, 0, 0)
    border_location = (0, 0, _WIDTH, _HEIGHT)
    border = pygame.draw.rect(background, border_color, border_location, 5)

    # Draw crossing game board
    line_width = int((1/3) * _WIDTH)
    line_height = int((1/3) * _HEIGHT)
    pygame.draw.line(background, (0, 0, 0), (line_width, 25), (line_width, _HEIGHT - 25), 2)
    pygame.draw.line(background, (0, 0, 0), (line_width * 2, 25), (line_width * 2, _HEIGHT - 25), 2)
    pygame.draw.line(background, (0, 0, 0), (25, line_height), (_WIDTH - 25, line_height), 2)
    pygame.draw.line(background, (0, 0, 0), (25, line_height * 2), (_WIDTH - 25, line_height * 2), 2)

    # Update screen with background
    screen.blit(background, (0, 0))
init_board()

# Draws strikes on board and declares winner
def declare_winner(winner):
    global can_move
    can_move = False

    if winner == (5, 5, 5, 5, 5):
        print("Draw")
        return

    grid_width = (1/6) * _WIDTH
    grid_height = (1/6) * _HEIGHT

    p_begin = (int(grid_width + winner[1] * grid_width * 2), int(grid_height + winner[2] * grid_height * 2))
    p_end = (int(grid_width + winner[3] * grid_width * 2), int(grid_height + winner[4] * grid_height * 2))

    pygame.draw.line(screen, (255, 0, 0), p_begin, p_end, 15)

# Check board for winner
def check_board():
    global board

    for x in range(0, 3):
        if board[x][0] == board[x][1] == board[x][2] and board[x][0] is not None:
            return (board[x][0], x, 0, x, 2)
    for y in range(0, 3):
        if board[0][y] == board[1][y] == board[2][y] and board[0][y] is not None:
            return (board[0][y], 0, y, 2, y)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return (board[0][0], 0, 0, 2, 2)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return (board[0][2], 0, 2, 2, 0)
    if not None in chain.from_iterable(board):
        return (5, 5, 5, 5, 5)
    return None

########################
# Minimax Implementation
def testMoves():
    global board
    global player_turn

    maxScore = -math.inf
    bestMove = None

    for x in range(0, 3):
        for y in range(0, 3):
            if board[x][y] is None:
                board[x][y] = player_turn
                score = minimax(0, True)
                board[x][y] = None
                if score > maxScore:
                    maxScore = score
                    bestMove = (x, y)
    print(maxScore, "testMove")
    board[bestMove[0]][bestMove[1]] = player_turn

def minimax(depth, bMax):
    global board

    status = check_board()
    print(status)
    if status == 1:
        score = -1
        return score
    elif status == 0:
        score = 1
        return score
    elif status == 5:
        score = 0
        return score
    else:
        if bMax:
            maxScore = -math.inf
            for x in range(0, 3):
                for y in range(0, 3):
                    if board[x][y] is None:
                        board[x][y] = player_turn
                        score = minimax(depth + 1, False)
                        board[x][y] = None
                        if score > maxScore:
                            maxScore = score
            print(maxScore, "maxScore")
            return maxScore
        else:
            minScore = math.inf
            for x in range(0, 3):
                for y in range(0, 3):
                    if board[x][y] is None:
                        board[x][y] = not player_turn
                        score = minimax(depth + 1, True)
                        board[x][y] = None
                        if score < minScore:
                            minScore = score
            print(minScore, "minScore")
            return minScore
    
########################

# Change board state
def click_event():
    global board
    global mouse_loc
    global player_turn
    global can_move

    if player_turn and mouse_loc == round_mouse_loc() and can_move:
        if board[mouse_loc[0]][mouse_loc[1]] is None:
            board[mouse_loc[0]][mouse_loc[1]] = player_turn
            player_turn = not player_turn

    if not player_turn and check_board() is None:
        testMoves()
        player_turn = not player_turn

# Returns mouse position as a tuple of grid
def round_mouse_loc():
    x_pos, y_pos = pygame.mouse.get_pos()

    if x_pos < _WIDTH / 3:
        x = 0
    elif _WIDTH / 3 <= x_pos < (2/3) * _WIDTH:
        x = 1
    else:
        x = 2

    if y_pos < _HEIGHT / 3:
        y = 0
    elif _HEIGHT / 3 <= y_pos < (2/3) * _HEIGHT:
        y = 1
    else:
        y = 2

    return (x, y)

# Draw current state of the board
def draw_board():
    global board

    for x_index in range(0, 3):
            for y_index in range(0, 3):
                if board[x_index][y_index] is not None:
                    x = ((1/6) + (2/6) * x_index) * _WIDTH
                    y = ((1/6) + (2/6) * y_index) * _HEIGHT
                    if board[x_index][y_index]:
                        screen.blit(x_move, (int(x - scale_img_x / 2), int(y - scale_img_y / 2)))
                    else:
                        screen.blit(o_move, (int(x - scale_img_x / 2), int(y - scale_img_y / 2)))

game_end = False
while not game_end:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit(0)

        # If event is mouseclickdown
        elif event.type == 5:
            # Later used to check if mouse moved and to do no move if mouse moved
            mouse_loc = round_mouse_loc()

        # If event is mouseclickup
        elif event.type == 6:
            click_event()
            draw_board()

            winner = check_board()
            if winner is not None:
                declare_winner(winner)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                init_board()
    
    pygame.display.update()