import pygame
import sys
from brain import NeuralNetwork

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BLOCK_SIZE = 32
WHITE = (255,255,255)

pygame.init()

frame = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

all_rects = []
for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
    row = []
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        rect = pygame.Rect(x, y, BLOCK_SIZE-1, BLOCK_SIZE-1)
        row.append([rect, (0, 0, 0)])
    all_rects.append(row)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for row in all_rects:
                for item in row:
                    rect, color = item
                    if rect.collidepoint(event.pos):
                        if color == (0, 0, 0):
                            item[1] = (255, 255, 255)
                        else:
                            item[1] = (0, 0, 0)
        elif event.type == pygame.KEYDOWN:

            input_vals = []

            for row in all_rects:
                for item in row:
                    color = item[1]
                    if color == (0,0,0):
                        input_vals.append(0)
                    elif color == (255,255,255):
                        input_vals.append(1)

            brain = NeuralNetwork()
            brain.calculate(input_vals)

    for row in all_rects:
        for item in row:
            rect, color = item
            pygame.draw.rect(frame, color, rect)

    pygame.display.flip()