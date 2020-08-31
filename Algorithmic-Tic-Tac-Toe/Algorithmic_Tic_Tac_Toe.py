import pygame
from itertools import chain
import math

pygame.init()

WIDTH = 800
HEIGHT = 800

# Set window size to variables and window title
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Import X and O and rescale
scale_img_x = int(WIDTH / 4)
scale_img_y = int(HEIGHT / 4)
x_img = pygame.transform.scale(pygame.image.load("img/x.png"), (scale_img_x, scale_img_y))
o_img = pygame.transform.scale(pygame.image.load("img/o.png"), (scale_img_x, scale_img_y))

# Set all global game variables to default values
def reset_variables():
    # Reset game board
    global board
    board = [[None] * 3, [None] * 3, [None] * 3]

    # Reset player turns
    global player_turn
    player_turn = True

    # Reset can_move status
    global can_move
    can_move = True

    global mouse_loc
    mouse_loc = None

# Initialize game board background draw
def init_board():
    # Set background color to white
    background = pygame.Surface(screen.get_size()).convert()
    background.fill((255, 255, 255))

    # Draw game board border
    pygame.draw.rect(background, (0, 0, 0), (0, 0, WIDTH, HEIGHT), 5)

    # Draw cross hatches
    line_width = int((1/3) * WIDTH)
    line_height = int((1/3) * HEIGHT)
    pygame.draw.line(background, (0, 0, 0), (line_width, 25), (line_width, HEIGHT - 25), 2)
    pygame.draw.line(background, (0, 0, 0), (line_width * 2, 25), (line_width * 2, HEIGHT - 25), 2)
    pygame.draw.line(background, (0, 0, 0), (25, line_height), (WIDTH - 25, line_height), 2)
    pygame.draw.line(background, (0, 0, 0), (25, line_height * 2), (WIDTH - 25, line_height * 2), 2)
    
    # Push background to screen
    screen.blit(background, (0, 0))

# Returns all possible moves of the current board as a list
def get_all_possible_moves(board):
    moves = []

    for x in range(0, 3):
        for y in range(0, 3):
            if board[x][y] is None:
                moves.append((x, y))
    return moves

# Draws the crosses through winning moves
def end_game(status):
    if status == (None, None, None, None, None):
        return

    global can_move
    can_move = False
    if status == (5, 5, 5, 5, 5):
        print("Draw")
        return

    grid_width = (1/6) * WIDTH
    grid_height = (1/6) * HEIGHT

    p_begin = (int(grid_width + status[1] * grid_width * 2), int(grid_height + status[2] * grid_height * 2))
    p_end = (int(grid_width + status[3] * grid_width * 2), int(grid_height + status[4] * grid_height * 2))

    pygame.draw.line(screen, (255, 0, 0), p_begin, p_end, 15)


# Returns the status of the current board i.e who won or draw
def check_status(board):
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
    return (None, None, None, None, None)

# Minimax implementation: Shuffles through all possible moves and chooses best move
def minimax(board, isMax):
    status = check_status(board)
    if status[0] == 5:
        return 0
    elif status[0] == True:
        return -1
    elif status[0] == False:
        return 1
    else:
        scores = []
        for move in get_all_possible_moves(board):
            board[move[0]][move[1]] = not isMax
            scores.append(minimax(board, not isMax))
            board[move[0]][move[1]] = None
        return max(scores) if isMax else min(scores)

# Setup to start recursive minimax function
def compute_next_move(board):
    if not get_all_possible_moves(board):
        return

    ideal_score = -math.inf
    ideal_move = None
    for move in get_all_possible_moves(board):
        board[move[0]][move[1]] = False
        score = minimax(board, False)
        board[move[0]][move[1]] = None
        if score > ideal_score:
            ideal_score = score
            ideal_move = move
    board[ideal_move[0]][ideal_move[1]] = False

# Change board state based on player move
def player_move(board, mouse_pos, player_turn, can_move):
    if not mouse_pos == round_mouse_loc():
        return False
    
    if player_turn and (mouse_pos[0], mouse_pos[1]) in get_all_possible_moves(board) and can_move:
            board[mouse_pos[0]][mouse_pos[1]] = True
            return True
    else:
        return False

# Returns mouse position as grid value
def round_mouse_loc():
    x_pos, y_pos = pygame.mouse.get_pos()
    if x_pos < WIDTH / 3:
        x = 0
    elif WIDTH / 3 <= x_pos < (2/3) * WIDTH:
        x = 1
    else:
        x = 2
    if y_pos < HEIGHT / 3:
        y = 0
    elif HEIGHT / 3 <= y_pos < (2/3) * HEIGHT:
        y = 1
    else:
        y = 2
    return (x, y)

# Draws the current state of the given board object
def draw_game(board):
    init_board()
    for x in range(0, 3):
        for y in range(0, 3):
            if not board[x][y] is None:
                x_pos_for_move = ((1/6) + (2/6) * x) * WIDTH
                y_pos_for_move = ((1/6) + (2/6) * y) * HEIGHT
                if board[x][y]:
                    screen.blit(x_img, (int(x_pos_for_move - scale_img_x / 2), int(y_pos_for_move - scale_img_y / 2)))
                else:
                    screen.blit(o_img, (int(x_pos_for_move - scale_img_x / 2), int(y_pos_for_move - scale_img_y / 2)))

reset_variables()
init_board()

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    
        elif event.type == 5:
            mouse_loc = round_mouse_loc()

        elif event.type == 6 and can_move:
            if player_move(board, mouse_loc, player_turn, can_move):
                player_turn = not player_turn
            draw_game(board)
            end_game(check_status(board))
            print(can_move)
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                reset_variables()
                init_board()

    if not player_turn and can_move:
        compute_next_move(board)
        player_turn = not player_turn
        draw_game(board)
        end_game(check_status(board))
    
    pygame.display.update()


