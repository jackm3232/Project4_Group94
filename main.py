import pygame, sys
#from sudoku_generator import *
from constants import *


pygame.init()
screen = pygame.display.set_mode((675, 675))
pygame.display.set_caption('Sudoku')
screen.fill(BG)
pygame.display.update()

def draw_big_grid():
    # draws horizontal lines
    for i in range(1,3):
        pygame.draw.line(screen, BLACK, (BIG_SQUARE*i, START), (BIG_SQUARE*i, END), BIG_LINE_WIDTH)
    # draws vertical lines
    for i in range(1,3):
        pygame.draw.line(screen, BLACK, (START, BIG_SQUARE * i), (END, BIG_SQUARE * i), BIG_LINE_WIDTH)

def draw_small_grid():
    # draws horizontal lines
    for i in range(1,9):
        pygame.draw.line(screen, BLACK, (SMALL_SQUARE*i, START), (SMALL_SQUARE*i, END), SMALL_LINE_WIDTH)
    # draws vertical lines
    for i in range(1,9):
        pygame.draw.line(screen, BLACK, (START, SMALL_SQUARE * i), (END, SMALL_SQUARE * i), SMALL_LINE_WIDTH)
while True:
    for event in pygame.event.get(): # event loop
        draw_big_grid()
        draw_small_grid()
        """ pygame.draw.line(screen, WHITE, (225, 0), (225, 600), width=10)
        pygame.draw.line(screen, WHITE, (450, 0), (450, 600), width=10)
        pygame.draw.line(screen, WHITE, (0, 200), (675, 200), width=10)
        pygame.draw.line(screen, WHITE, (0, 400), (675, 400), width=10)
        pygame.draw.line(screen, WHITE, (0, 600), (675, 600), width=10)
        pygame.draw.line(screen, WHITE, (0, 4), (675, 4), width=10)
        pygame.draw.line(screen, WHITE, (4, 0), (4, 600), width=10)
        pygame.draw.line(screen, WHITE, (669, 0), (669, 600), width=10)"""
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
