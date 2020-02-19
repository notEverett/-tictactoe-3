import pygame

black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
green = (0, 255, 0)
red = (255, 0, 0)
color = white

pygame.init()

size = [530, 530]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('(TicTacToe)^3')

clock = pygame.time.Clock()
done = False
#Dimensions and Margin of individual boxes
h = 50
w = 50
m = 10

def sub_table(x_i, y_i):
    for c in range(0,3):
        for r in range(0,3):
            pygame.draw.rect(screen, color, [x_i+(m+w)*c,y_i+(m+h)*r, w, h])

# Creation of 2D array backing the grid/playing surface
grid = [[0 for x in range(0,9)] for y in range(0,9)]
turn = 0

table_11 = [tuple([x,y]) for x in range(1,4) for y in range(1,4)]
table_12 = [tuple([x,y]) for x in range(4,7) for y in range(1,4)]
table_13 = [tuple([x,y]) for x in range(7,10) for y in range(1,4)]
table_21 = [tuple([x,y]) for x in range(1,4) for y in range(4,7)]
table_22 = [tuple([x,y]) for x in range(4,7) for y in range(4,7)]
table_23 = [tuple([x,y]) for x in range(7,10) for y in range(4,7)]
table_31 = [tuple([x,y]) for x in range(1,4) for y in range(7,10)]
table_32 = [tuple([x,y]) for x in range(4,7) for y in range(7,10)]
table_33 = [tuple([x,y]) for x in range(7,10) for y in range(7,10)]

# Main Program Loop
while not done:
    # Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT: # If the user clicked the exit button
            done = True               # Exit the game
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            coord_table = (x_table, y_table) = (x//180 + 1, y//180 + 1)
            coord_board = (x_board, y_board) = (x//60 + 1, y//60 + 1)
            print(f'Board Coordinates:{coord_board}\nTable Coordinates: {coord_table}')
    # Game Logic:




# Drawing Code:
    screen.fill(black)
    # Drawing individual boxes
    for tx in range(0,361,180):
        for ty in range(0,361,180):
            sub_table(tx, ty)

    pygame.display.flip() # Displays drawing code on screen

    clock.tick(60) # Limits game to 60 frames/second

pygame.quit()
