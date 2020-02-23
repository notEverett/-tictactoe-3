import pygame
import numpy as np

# Variables holding the RGB color information
black = (0,0,0)
white = (255,255,255)
green = (141,242,78)
red = (219,59,59)
blue = (64,115,227)

pygame.init()

# Creates the screen of a specified size and caption
size = [530,530]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('(tictactoe)^3')

clock = pygame.time.Clock()

# Array holding information on the players' positions
master_grid = np.array([[[[0 for x in range(0,3)] for y in range(0,3)]\
    for X in range(0,3)] for Y in range(0,3)])
# Array holding information on the position of the next table that must be played on
next_turn_grid = np.array([[0 for x in range(0,3)] for y in range(0,3)])

# Dimensions of each individual box + margin in between them
h = 50
w = 50
m = 10

# Variable that determines which player's turn it is
turn = 0
# Varibale that ensures the game loop continues until told otherwise
done = False

while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            next_turn_grid = np.array([[0 for x in range(0,3)] for y in range(0,3)])
            (a, b) = pygame.mouse.get_pos() # Screen coordinates
            C = (X, Y) = (a//180, b//180) # Table coordinates
            c = (x, y) = (a//60 - 3*X, b//60 - 3*Y) # Sub-Table coordinates

            if turn%2==0:
                master_grid[X][Y][x][y] = 1
                turn += 1
            else:
                master_grid[X][Y][x][y] = 2
                turn += 1

            next_turn_grid[x][y] = -1

            print(f'{C}\n{c}')

    # Game Logic:


    # Drawing Code:
    screen.fill(black)

    color = green
    for X in range(0,3):
        for Y in range(0,3):
            if next_turn_grid[X][Y] == -1:
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
