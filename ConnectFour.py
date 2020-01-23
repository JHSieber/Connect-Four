import pygame
import numpy as np
import math

pygame.init()

ROWS = 6
COLS = 7

BOX = 100
canvasWidth = BOX*COLS # sets size of window
canvasHeight = BOX*ROWS + BOX

PLAYER1 = 1
PLAYER2 = 2

color = PLAYER1

RED = (216,31,42)
BLUE = (0,33,203)
BLACK = (0,0,0)
WHITE = (255,255,255)

RADIUS = int(BOX/2 -5)

win = pygame.display.set_mode((canvasWidth, canvasHeight)) #creates the surface for everything to be drawn on
pygame.display.set_caption("Connect Four")  #sets the name of the window

#Helper function to create text Objects
def textObjects(text, font, hue):
    textSurface = font.render(text, True, hue)
    return textSurface, textSurface.get_rect()

def isValidMove(board, col):
    return board[0][col] == 0

def main():
    global color
    makeBoard()
    # positions = []
    # for i in range(ROWS):
    #     positions.append([])
    #     for j in range(COLS):
    #         positions[i].append(' ')
    positions = np.zeros((ROWS,COLS))
    run = True
    res = -1
    won = False

    while run:
        for event in pygame.event.get(): #allows us to quit when we hit the close button
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(win, BLACK, (0,0,canvasWidth, BOX))
                mx = event.pos[0]
                if color == PLAYER1:
                    pygame.draw.circle(win, RED, (mx, int(BOX/2)), RADIUS)
                else:
                    pygame.draw.circle(win, BLUE, (mx, int(BOX/2)), RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(win, BLACK, (0,0,canvasWidth, BOX))

                if color == PLAYER1 :

                    mouseX = event.pos[0] #gets the current x and y of the mouse
                    col = int(math.floor(mouseX/BOX))
                    if isValidMove(positions, col):

                        positions, position = makeTurn(positions, col)
                        drawMove(color, position)

                        won, res = winner(positions, color)
                        if won:
                            print(res, "is the winner")
                            run = False

                        color = PLAYER2
                else:

                    mouseX = event.pos[0] #gets the current x and y of the mouse
                    col = int(math.floor(mouseX/BOX))
                    if isValidMove(positions, col):

                        positions, position = makeTurn(positions, col)
                        drawMove(color, position)

                        won, res = winner(positions, color)
                        if won:
                            print(res, "is the winner")
                            run = False

                        color = PLAYER1

                pygame.display.update()
    if won:
        mediumText = pygame.font.SysFont("comicsansms", 75)

        if res == 1:
            textSurf, textRect = textObjects("Player 1 wins!", mediumText, RED)
            textRect.center = ( (canvasWidth/2), (BOX/2) )
            win.blit(textSurf, textRect)
            pygame.time.wait(3000)

        else:
            textSurf, textRect = textObjects("Player 2 wins!", mediumText, BLUE)
            textRect.center = ( (canvasWidth/2), (BOX/2) )
            win.blit(textSurf, textRect)
            pygame.time.wait(3000)

def drawMove(color, position):

    if color == PLAYER1:
        co = RED
    else:
        co = BLUE
    column, row = position
    drawX = int((column*2+1)*canvasWidth/14)
    drawY = int((row*2+1)*canvasWidth/12)
    pygame.draw.circle(win, co, (int(column*BOX+BOX/2), int(row*BOX+BOX+BOX/2)), RADIUS, 0)

def makeTurn(positions, col): #had to change some stuff so if something doesnt work it may be here
    global color
    #if mouseX > 0 and mouseX < canvasWidth/COLS: #first column
    for i in range(ROWS-1,-1,-1): #iterate backwards through each row of the columnn from the bottom to the top
        if positions[i][col] == 0: #check if there is already one there
            positions[i][col] = color #fill spot in array with correct color
            position = col, i #save the column and the row of the most recent move to draw
            return positions, position #return updated variables
        else:
            continue

def makeBoard():
    run = True
    #win.fill(WHITE)
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(win, WHITE, (c*BOX, r*BOX+BOX, BOX, BOX))
            pygame.draw.circle(win, BLACK, (int(c*BOX+BOX/2), int(r*BOX+BOX+BOX/2)), RADIUS)
    pygame.display.update()

def winner(positions, color):
    #check for horizontal wins
    for i in range(ROWS): #iterate through each row
        total = 1
        for j in range(1,COLS): #iterate through all but the first column
            if positions[i][j] == positions[i][j-1]: #if the next color on the line is the same as the previous then increase total
                if positions[i][j] != 0 and positions[i][j-1] != 0:
                    total+=1
                    if total == 4:
                        return True, color
            else:
                total = 1

    #check for verticle wins
    for i in range(COLS): #iterate through each column
        total = 1
        for j in range(1,ROWS): #iterate through each row in the column
            if positions[j][i] == positions[j-1][i]: #check if the color is the same as the one above it
                if positions[j][i] != 0 and positions[j-1][i] != 0:
                    total+=1
                    if total == 4:
                        return True, color

    # Check positively sloped diaganols
    for c in range(COLS-3):
        for r in range(ROWS-3):
            if positions[r][c] == color and positions[r+1][c+1] == color and positions[r+2][c+2] == color and positions[r+3][c+3] == color:
                return True, color

    # Check negatively sloped diaganols
    for c in range(COLS-3):
        for r in range(3, ROWS):
            if positions[r][c] == color and positions[r-1][c+1] == color and positions[r-2][c+2] == color and positions[r-3][c+3] == color:
                return True, color
    #check for diagonal left
    # for i in range(5,2,-1): #checks bottom 3 rows
    #     for j in range (3,COLS): #checks right 4 columns
    #         #print(checkUpLeft(positions, i, j))
    #         if checkUpLeft(positions, i, j) == 4:
    #             return True, positions[i][j]
    return False, 0

def checkUpLeft(positions, row, col):
    if col < 0 or row < 0:
        return 0
    if positions[row][col] == positions[row-1][col-1] and positions[row][col] != 0:
        return 1 + checkUpLeft(positions, col-1, row-1)
    else:
        return 0



def horizontalWin(positions):
    for i in range(COLS):
        total = 0
        for j in range(8):
            if positions[i][j] == positions[i][j-1]:
                total+=1
            else:
                total = 0
            if total == 4:
                return True, positions[i][j]
    return False, ''



main()
