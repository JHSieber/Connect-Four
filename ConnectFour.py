import pygame
#import numpy as np
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
YELLOW = (255,255,0)

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
    positions = []
    for i in range(ROWS): #create 3d array with rows and columns
        positions.append([])
        for j in range(COLS):
            positions[i].append(0)
    #positions = np.zeros((ROWS,COLS))
    run = True
    res = -1
    won = False

    while run:
        for event in pygame.event.get(): #allows us to quit when we hit the close button
            if event.type == pygame.QUIT:
                quitGame()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(win, BLACK, (0,0,canvasWidth, BOX))
                mx = event.pos[0]
                if color == PLAYER1:
                    pygame.draw.circle(win, RED, (mx, int(BOX/2)), RADIUS)
                else:
                    pygame.draw.circle(win, YELLOW, (mx, int(BOX/2)), RADIUS)

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
                            mediumText = pygame.font.SysFont("comicsansms", 75)
                            if res == 1:
                                print("red")
                                textSurf, textRect = textObjects("Player 1 wins!", mediumText, RED)
                                textRect.center = ( (canvasWidth/2), (BOX/2) )
                                win.blit(textSurf, textRect)
                                pygame.display.update()
                                pygame.time.wait(3000)
                    
                            else:
                                print("blue")
                                textSurf, textRect = textObjects("Player 2 wins!", mediumText, BLUE)
                                textRect.center = ( (canvasWidth/2), (BOX/2) )
                                win.blit(textSurf, textRect)
                                pygame.display.update()
                                pygame.time.wait(3000)
                            run = False
                            #endScreen

                        color = PLAYER1

                pygame.display.update()
        

def drawMove(color, position):

    if color == PLAYER1:
        co = RED
    else:
        co = YELLOW
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
    win.fill(BLACK)
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(win, BLUE, (c*BOX, r*BOX+BOX, BOX, BOX))
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

# def textObjects(text, font):
#     textSurface = font.render(text, True, (0,0,0))
#     return textSurface, textSurface.get_rect()

#Helper function to create button functionality
def button(msg,x,y,w,h,ic,ac,action=None):
    global gameMode

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            #print(action)
            gameMode = action
            action()
    else:
        pygame.draw.rect(win, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = textObjects(msg, smallText, BLUE)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)

def quitGame():
    pygame.quit()
    quit()
    
clock = pygame.time.Clock()    


def intro():
    intro = True
    #image = pygame.image.load("bg.png")
    #imgRect = image.get_rect()
    #imgRect.left, imgRect.top = 44,44

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        
        win.fill((228,233,244))
        #screen.blit(image, imgRect)
        largeText = pygame.font.SysFont("comicsansms",100)
        TextSurf, TextRect = textObjects("Connect Four", largeText, RED)
        TextRect.center = ((canvasWidth/2),100)
        win.blit(TextSurf, TextRect)

        #button("Solo",(canvasWidth/2 - 50),250,100,50,(0, 255, 0),(0, 200, 0),solo)
        button("Duo",(canvasWidth/2 - 50),350,100,50,(0, 255, 0),(0, 200, 0),main)
        button("Quit", (canvasWidth/2 - 50), 450, 100, 50, (255,0,0), (200,0,0), quitGame)
        
        pygame.display.update()
        clock.tick(30)

    

intro()
#main()
