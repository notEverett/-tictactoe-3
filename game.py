import pygame
import numpy as np

black = (0,0,0)
white = (255,255,255)
green = (141,242,78)
red = (219,59,59)
blue = (64,115,227)
color = white

pygame.init()

size = [530,530]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('(tictactoe)^3')

clock = pygame.time.Clock()

done = False

grid = np.array([[[[0 for x in range(0,3)] for y in range(0,3)]\
    for X in range(0,3)] for Y in range(0,3)])

h = 50
w = 50
m = 10
def sub_table(x_i, y_i):
    for x in range(0,3):
        for y in range(0,3):
            pygame.draw.rect(screen, color, [x_i+(m+w)*x,y_i+(m+h)*y, w, h])

while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            (a, b) = pygame.mouse.get_pos()
            C = (X, Y) = (a//180, b//180)
            c = (x, y) = (a//60 - 3*X, b//60 - 3*Y)
            print(f'{C}\n{c}\n')
    # Game Logic:

    # Drawing Code:
    screen.fill(black)
    # Drawing individual boxes
    for X in range(0,361,180):
        for Y in range(0,361,180):
            sub_table(X, Y)

    pygame.display.flip() # Displays drawing code on screen

    clock.tick(60) # Limits game to 60 frames/second

pygame.quit()
