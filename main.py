import pygame, sys

from Project4_Group94.sudoku_generator import generate_sudoku
# from sudoku_generator import *
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')
screen.fill(BG)
pygame.display.update()
num_font = pygame.font.Font(None, NUM_FONT)
game_over_font = pygame.font.Font(None, OVER_FONT)
button_font = pygame.font.Font(None, BUTTON_FONT)

size = 0
remove = 0


# initialize game state
# board = generate_sudoku(size, remove)  # create board


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


def highlight_cell(row, col):
    pygame.draw.line(screen, RED, (SMALL_SQUARE * col, SMALL_SQUARE * row),
                     (SMALL_SQUARE * col, SMALL_SQUARE * row + SMALL_SQUARE),
                     SMALL_LINE_WIDTH)
    pygame.draw.line(screen, RED, (SMALL_SQUARE * col, SMALL_SQUARE * row),
                     (SMALL_SQUARE * col + SMALL_SQUARE, SMALL_SQUARE * row),
                     SMALL_LINE_WIDTH)
    pygame.draw.line(screen, RED, (SMALL_SQUARE * col + SMALL_SQUARE, SMALL_SQUARE * row),
                     (SMALL_SQUARE * col + SMALL_SQUARE, SMALL_SQUARE * row + SMALL_SQUARE),
                     SMALL_LINE_WIDTH)
    pygame.draw.line(screen, RED, (SMALL_SQUARE * col, SMALL_SQUARE * row + SMALL_SQUARE),
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
    if win == 0:
        end_text = "Game Over :("
    else:
        end_text = "Game Won!"
    end_surf = game_over_font.render(end_text, 0, BLACK)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(end_surf, end_rect)


def draw_og_board(b):
    offset = 20
    for i in range(len(b)):
        for j in range(len(b[i])):
            num = b[i][j]
            if num != 0:
                num_text = num_font.render(str(num), 0, BLACK)
                screen.blit(num_text, ((i * SMALL_SQUARE) + offset + 5, (j * SMALL_SQUARE) + offset - 5))


# initialize board with all empty cells
diff = 30
board = generate_sudoku(9, diff)
draw_big_grid()
draw_small_grid()
draw_og_board(board)
buttons()
pygame.display.update()
while True:
    game_over = False
    for event in pygame.event.get():  # event loop
        draw_big_grid()
        draw_small_grid()
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            r = y // SMALL_SQUARE
            c = x // SMALL_SQUARE
            if y <= 675:
                highlight_cell(r, c)
            else:
                if 739 >= y >= 691:
                    if 112 <= x <= 224:
                        print('reset')  # reset board
                    elif 263 <= x <= 411:
                        print('restart')  # return to home screen
                    if 460 <= x <= 548:
                        print('exit')  # end program
        if game_over:
            pygame.display.update()
            pygame.time.delay(100)
            draw_game_over(win)

    pygame.display.update()
