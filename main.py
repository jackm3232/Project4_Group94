import pygame, sys
#from sudoku_generator import *


pygame.init()
screen = pygame.display.set_mode((675, 675))
pygame.display.set_caption('Sudoku')
screen.fill((255, 255, 255))
pygame.display.update()

while True:
    for event in pygame.event.get(): # event loop
        pygame.draw.line(screen, (0, 0, 0), (225, 0), (225, 600), width=10)
        pygame.draw.line(screen, (0, 0, 0), (450, 0), (450, 600), width=10)
        pygame.draw.line(screen, (0, 0, 0), (0, 200), (675, 200), width=10)
        pygame.draw.line(screen, (0, 0, 0), (0, 400), (675, 400), width=10)
        pygame.draw.line(screen, (0, 0, 0), (0, 600), (675, 600), width=10)
        pygame.draw.line(screen, (0, 0, 0), (0, 4), (675, 4), width=10)
        pygame.draw.line(screen, (0, 0, 0), (4, 0), (4, 600), width=10)
        pygame.draw.line(screen, (0, 0, 0), (669, 0), (669, 600), width=10)
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
