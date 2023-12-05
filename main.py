import pygame, sys
# from sudoku_generator import *
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')
screen.fill(BG)
pygame.display.update()
num_font = pygame.font.Font(None, NUM_FONT)
game_over_font = pygame.font.Font(None, OVER_FONT)

size = 0
remove = 0
# intitalize game state
#board = generate_sudoku(size, remove)  # create board



def draw_big_grid():  # large grid
    # draws vertical lines
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (BIG_SQUARE * i, START), (BIG_SQUARE * i, END),
                         BIG_LINE_WIDTH)
    # draws horizontal lines
    for i in range(1, 4):
        pygame.draw.line(screen, BLACK, (START, BIG_SQUARE * i), (END, BIG_SQUARE * i),
                         BIG_LINE_WIDTH)


def draw_small_grid():  # inner, smaller grid
    # draws horizontal lines
    for i in range(1, 9):
        pygame.draw.line(screen, BLACK, (SMALL_SQUARE * i, START), (SMALL_SQUARE * i, END),
                         SMALL_LINE_WIDTH)
    # draws vertical lines
    for i in range(1, 9):
        pygame.draw.line(screen, BLACK, (START, SMALL_SQUARE * i), (END, SMALL_SQUARE * i),
                         SMALL_LINE_WIDTH)

def draw_numbers():
    num_one_surf = num_font.render("1", 0, BLACK)
    num_one_rect = num_one_surf.get_rect(center = (340,340))

    screen.blit(num_one_surf, num_one_rect)

def draw_game_over(win):
    screen.fill(BG)
    if win == 0:
        end_text = "Game Over :("
    else:
        end_text = "Game Won!"
    end_surf = game_over_font.render(end_text, 0, BLACK)
    end_rect = end_surf.get_rect(center = (WIDTH // 2, HEIGHT // 3))
    screen.blit(end_surf, end_text)

while True:
    game_over = False
    for event in pygame.event.get():  # event loop
        # initialize board with all empty cells
        draw_big_grid()
        draw_small_grid()
        pygame.display.update()
        draw_numbers()
        # initialize board with basic fill in
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // SMALL_SQUARE
            col = x // SMALL_SQUARE
        if game_over:
            pygame.display.update()
            pygame.time.delay(100)
            draw_game_over(win)

    pygame.display.update()
