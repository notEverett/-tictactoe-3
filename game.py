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

master_grid = np.array([[[[0 for x in range(0,3)] for y in range(0,3)]\
    for X in range(0,3)] for Y in range(0,3)])

next_turn_grid = np.array([[0 for x in range(0,3)] for y in range(0,3)])

# Dimensions of each individual box + margin in between them
h = 50
w = 50
m = 10

turn = 0
done = False
while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            next_turn_grid = np.array([[0 for x in range(0,3)] for y in range(0,3)])
            (a, b) = pygame.mouse.get_pos() # Screen coordinates
            X = a//180
            Y = b//180
            x = a//60 - 3*X
            y = b//60 - 3*Y
            if turn%2==0:
                master_grid[X][Y][x][y] = 1
                turn += 1
            else:
                master_grid[X][Y][x][y] = 2
                turn += 1

            next_turn_grid[x][y] = 5

            C = (X,Y)
            c = (x,y)

            print(f'{C}\n{c}')

    # Game Logic:


    # Drawing Code:
    screen.fill(black)

    color = green
    for X in range(0,3):
        for Y in range(0,3):
            if next_turn_grid[X][Y] == 5:
                pygame.draw.rect(screen, color, [X*180, Y*180, 170, 170])


    # Drawing individual boxes
    for X in range(0,3):
        for Y in range(0,3):
            for x in range(0,3):
                for y in range(0,3):
                    color = white
                    if master_grid[X][Y][x][y] == 1:
                        color = blue
                    if master_grid[X][Y][x][y] == 2:
                        color = red
                    pygame.draw.rect(screen, color, [X*180+(m+w)*x, Y*180+(m+h)*y, w, h])

    pygame.display.flip() # Displays drawing code on screen

    clock.tick(60) # Limits game to 60 frames/second

pygame.quit()
