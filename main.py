import pygame, sys

from Project4_Group94.sudoku_generator import generate_sudoku
# from sudoku_generator import *
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')
screen.fill(BG)
pygame.display.update()
sketch_font = pygame.font.Font(None, SKETCH_FONT)
num_font = pygame.font.Font(None, NUM_FONT)
game_over_font = pygame.font.Font(None, OVER_FONT)
button_font = pygame.font.Font(None, BUTTON_FONT)

size = 0
remove = 0


# initialize game state

def draw_big_grid():  # large grid
    # draws vertical lines
    for i in range(3):
        pygame.draw.line(screen, BLACK, (BIG_SQUARE * i, START), (BIG_SQUARE * i, END),
                         BIG_LINE_WIDTH)
    # draws horizontal lines
    for i in range(4):
        pygame.draw.line(screen, BLACK, (START, BIG_SQUARE * i), (END, BIG_SQUARE * i),
                         BIG_LINE_WIDTH)


def draw_small_grid():  # inner, smaller grid
    # draws vertical lines
    for i in range(10):
        pygame.draw.line(screen, BLACK, (SMALL_SQUARE * i, START), (SMALL_SQUARE * i, END),
                         SMALL_LINE_WIDTH)
    # draws horizontal lines
    for i in range(9):
        pygame.draw.line(screen, BLACK, (START, SMALL_SQUARE * i), (END, SMALL_SQUARE * i),
                         SMALL_LINE_WIDTH)


def highlight_cell(row, col, color):
    pygame.draw.line(screen, color, (SMALL_SQUARE * col, SMALL_SQUARE * row),
                     (SMALL_SQUARE * col, SMALL_SQUARE * row + SMALL_SQUARE),
                     SMALL_LINE_WIDTH)
    pygame.draw.line(screen, color, (SMALL_SQUARE * col, SMALL_SQUARE * row),
                     (SMALL_SQUARE * col + SMALL_SQUARE, SMALL_SQUARE * row),
                     SMALL_LINE_WIDTH)
    pygame.draw.line(screen, color, (SMALL_SQUARE * col + SMALL_SQUARE, SMALL_SQUARE * row),
                     (SMALL_SQUARE * col + SMALL_SQUARE, SMALL_SQUARE * row + SMALL_SQUARE),
                     SMALL_LINE_WIDTH)
    pygame.draw.line(screen, color, (SMALL_SQUARE * col, SMALL_SQUARE * row + SMALL_SQUARE),
                     (SMALL_SQUARE * col + SMALL_SQUARE, SMALL_SQUARE * row + SMALL_SQUARE),
                     SMALL_LINE_WIDTH)


def draw_numbers(row, col):
    num_one_surf = num_font.render("1", 0, BLACK)
    num_one_rect = num_one_surf.get_rect(center=(row * 40 + SMALL_SQUARE, col * 40 + SMALL_SQUARE))

    screen.blit(num_one_surf, num_one_rect)


def buttons():
    reset_text = button_font.render("RESET", 0, WHITE)
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(ORANGE)
    reset_surface.blit(reset_text, (10, 10))
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 4, 715))
    screen.blit(reset_surface, reset_rectangle)
    restart_text = button_font.render("RESTART", 0, WHITE)
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(ORANGE)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, 715))
    screen.blit(restart_surface, restart_rectangle)
    exit_text = button_font.render("EXIT", 0, WHITE)
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(ORANGE)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(
        center=(3 * WIDTH // 4 - 10, 715))
    screen.blit(exit_surface, exit_rectangle)


def draw_game_over(win):
    screen.fill(BG)
    if win == 1:
        end_text = "Game Won!"
    else:
        end_text = "Game Over :("
    end_surf = game_over_font.render(end_text, 0, BLACK)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(end_surf, end_rect)
    if end_text == "Game Won!":
        exit_text = button_font.render("EXIT", 0, WHITE)
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(ORANGE)
        exit_surface.blit(exit_text, (10, 10))
        exit_rectangle = exit_surface.get_rect(
            center=(WIDTH // 2, HEIGHT//2))
        screen.blit(exit_surface, exit_rectangle)



def draw_og_board(b):
    offset = 20
    for i in range(len(b)):
        for j in range(len(b[i])):
            num = b[i][j]
            if num != 0:
                num_text = num_font.render(str(num), 0, BLACK)
                screen.blit(num_text, ((j * SMALL_SQUARE) + offset + 5, (i * SMALL_SQUARE) + offset - 5))


def draw_changed_board(b, sketch):
    for i in range(len(b)):
        for j in range(len(b[i])):
            num = sketch[i][j]
            if num != b[i][j] and num != 0:
                num_text = sketch_font.render(str(num), 0, GRAY)
                screen.blit(num_text, ((j * SMALL_SQUARE) + 5, (i * SMALL_SQUARE) + 5))


# initialize board with all empty cells
diff = 1
board_call = generate_sudoku(9, diff)
solved = board_call[1]
board = board_call[0]
og_board = []
for i in range(len(board)):
    og = []
    for j in range(len(board[i])):
        og.append(board[i][j])
    og_board.append(og)
draw_big_grid()
draw_small_grid()
draw_og_board(board)
buttons()
pygame.display.update()
guess = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
r, c, win = 0, 0, 0
while True:
    game_over = False
    for event in pygame.event.get():  # event loop
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            if (y // SMALL_SQUARE) != r or (x // SMALL_SQUARE) != c:
                draw_big_grid()
                draw_small_grid()
            r = y // SMALL_SQUARE
            c = x // SMALL_SQUARE
            if y <= 675:
                highlight_cell(r, c, RED)
            else:
                if 739 >= y >= 691:
                    if 112 <= x <= 224:
                        screen.fill(BG)
                        screen.fill(BG)
                        draw_big_grid()
                        draw_small_grid()
                        board = og_board
                        draw_og_board(board)
                        buttons()
                    elif 263 <= x <= 411:
                        print('restart')  # return to home screen
                    elif 460 <= x <= 548:
                        pygame.quit()
                        sys.exit()
                        # end program
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not game_over:
                draw_big_grid()
                draw_small_grid()
                if c != 0:
                    c -= 1
                    highlight_cell(r, c, RED)
            elif event.key == pygame.K_RIGHT and not game_over:
                draw_big_grid()
                draw_small_grid()
                if c != 8:
                    c += 1
                    highlight_cell(r, c, RED)
            elif event.key == pygame.K_UP and not game_over:
                draw_big_grid()
                draw_small_grid()
                if r != 0:
                    r -= 1
                    highlight_cell(r, c, RED)
            elif event.key == pygame.K_DOWN and not game_over:
                draw_big_grid()
                draw_small_grid()
                if r != 8:
                    r += 1
                    highlight_cell(r, c, RED)
            elif event.key == pygame.K_RETURN:
                if guess[r][c] != 0:
                    board[r][c] = guess[r][c]
                    guess[r][c] = 0
                screen.fill(BG)
                draw_big_grid()
                draw_small_grid()
                draw_og_board(board)
                buttons()
                pygame.display.update()
                draw_changed_board(board, guess)
            elif event.key == pygame.K_1:  # if key 1 is pressed
                if board[r][c] == 0:
                    num_text = sketch_font.render('1', 0, GRAY)
                    screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                    guess[r][c] = 1
            elif event.key == pygame.K_2:  # if key 2 is pressed
                if board[r][c] == 0:
                    num_text = sketch_font.render('2', 0, GRAY)
                    screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                    guess[r][c] = 2
            elif event.key == pygame.K_3:  # if key 3 is pressed
                if board[r][c] == 0:
                    num_text = sketch_font.render('3', 0, GRAY)
                    screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                    guess[r][c] = 3
            elif event.key == pygame.K_4:  # if key 4 is pressed
                if board[r][c] == 0:
                    num_text = sketch_font.render('4', 0, GRAY)
                    screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                    guess[r][c] = 4
            elif event.key == pygame.K_5:  # if key 5 is pressed
                if board[r][c] == 0:
                    num_text = sketch_font.render('5', 0, GRAY)
                    screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                    guess[r][c] = 5
            elif event.key == pygame.K_6:  # if key 6 is pressed
                if board[r][c] == 0:
                    num_text = sketch_font.render('6', 0, GRAY)
                    screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                    guess[r][c] = 6
            elif event.key == pygame.K_7:  # if key 7 is pressed
                if board[r][c] == 0:
                    num_text = sketch_font.render('7', 0, GRAY)
                    screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                    guess[r][c] = 7
            elif event.key == pygame.K_8:  # if key 8 is pressed
                if board[r][c] == 0:
                    num_text = sketch_font.render('8', 0, GRAY)
                    screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                    guess[r][c] = 8
            elif event.key == pygame.K_9:  # if key 9 is pressed
                if board[r][c] == 0:
                    num_text = sketch_font.render('9', 0, GRAY)
                    screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                    guess[r][c] = 9
        zero_check = False
        for b in board:
            for num in b:
                if num == 0:
                    zero_check = True
        if not zero_check:
            game_over = True
            if board != solved:
                win = 123
            else:
                win = 1
        if game_over:
            pygame.display.update()
            pygame.time.delay(100)
            draw_game_over(win)
    pygame.display.update()
