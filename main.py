import pygame, sys
#from sudoku_generator import *

pygame.init()
pygame.display.set_caption('Sudoku')

screen = pygame.display.set_mode((675, 675))
screen.fill((255, 255, 255))
pygame.display.update()

while True:
    for event in pygame.event.get():
        pygame.draw.line(screen, (0, 0, 0), (225, 0), (225, 600))
        pygame.draw.line(screen, (0, 0, 0), (450, 0), (450, 600))
        pygame.draw.line(screen, (0, 0, 0), (0, 225), (675, 225))
        pygame.draw.line(screen, (0, 0, 0), (0, 450), (675, 450))
        pygame.display.update()
    if event.type == pygame.QUIT:
        break
      
