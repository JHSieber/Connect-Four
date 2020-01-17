import pygame
pygame.init()

canvasWidth = 500 # sets size of window
canvasHeight = 500
win = pygame.display.set_mode((canvasWidth, canvasHeight)) #creates the surface for everything to be drawn on
pygame.display.set_caption("Connect Four")  #sets the name of the window



def main():
    makeBoard()
    positions = []
    for i in range(7):
        positions.append([])
        for j in range(8):
            positions[i].append(' ')
    run = True
    color = 'red'
    while run:
        pygame.time.delay(100)
        
        for event in pygame.event.get(): #allows us to quit when we hit the close button
            if event.type == pygame.QUIT:
                run = False
        
        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos() #gets the current x and y of the mouse
            color, positions, position = makeTurn(positions, color, mouseX)
            drawMove(color, position)
        won = False
        win = 'red'
        won, win = winner(positions)
        if won:
            print(win, "is the winner")
        pygame.display.update()
        
    # make the initiol board
    # initialize a 2D array of 6 by 7
    # fill the array with empty strings
    
def drawMove(color, position):
    if color == 'red':
        co = 216,31,42
    else:
        co = 0,33,203
    column, row = position
    drawX = int((column*2+1)*canvasWidth/14)
    drawY = int((row*2+1)*canvasWidth/12)
    pygame.draw.circle(win, co, (drawX, drawY), int(canvasWidth/14), 0)

def makeTurn(positions, color, mouseX):
    if mouseX > 0 and mouseX < canvasWidth/7: #first column
        for i in range(5,-1,-1): #iterate backwards through each row of the columnn from the bottom to the top 
            if positions[0][i] == ' ': #check if there is already one there
                positions[0][i] = color #fill spot in array with correct color
                position = 0, i #save the column and the row of the most recent move to draw
                if color == 'red': #alternate colors
                    color = 'blue'
                else:
                    color = 'red'
                return color, positions, position #return updated variables
            else:
                continue
    if mouseX > canvasWidth/7 and mouseX < 2*canvasWidth/7: #second Column
        for i in range(5,-1,-1):
            if positions[1][i] == ' ':
                positions[1][i] = color
                position = 1, i 
                if color == 'red':
                    color = 'blue'
                else:
                    color = 'red'
                return color, positions, position
            else:
                continue
    if mouseX > 2*canvasWidth/7 and mouseX < 3*canvasWidth/7: #third column
        for i in range(5,-1,-1):
            if positions[2][i] == ' ':
                positions[2][i] = color
                position = 2, i 
                if color == 'red':
                    color = 'blue'
                else:
                    color = 'red'
                return color, positions, position
            else:
                continue
    if mouseX > 3*canvasWidth/7 and mouseX < 4*canvasWidth/7: #fourth column
        for i in range(5,-1,-1):
            if positions[3][i] == ' ':
                positions[3][i] = color
                position = 3, i 
                if color == 'red':
                    color = 'blue'
                else:
                    color = 'red'
                return color, positions, position
            else:
                continue
    if mouseX > 4*canvasWidth/7 and mouseX < 5*canvasWidth/7: #fifth column
        for i in range(5,-1,-1):
            if positions[4][i] == ' ':
                positions[4][i] = color
                position = 4, i 
                if color == 'red':
                    color = 'blue'
                else:
                    color = 'red'
                return color, positions, position
            else:
                continue
    if mouseX > 5*canvasWidth/7 and mouseX < 6*canvasWidth/7: #sixth column
        for i in range(5,-1,-1):
            if positions[5][i] == ' ':
                positions[5][i] = color
                position = 5, i 
                if color == 'red':
                    color = 'blue'
                else:
                    color = 'red'
                return color, positions, position
            else:
                continue
    if mouseX > 6*canvasWidth/7 and mouseX < canvasWidth: #seventh column
        for i in range(5,-1,-1):
            if positions[6][i] == ' ':
                positions[6][i] = color
                position = 6, i 
                if color == 'red':
                    color = 'blue'
                else:
                    color = 'red'
                return color, positions, position
            else:
                continue
    

def makeBoard():
    run = True
    #TODO


def winner(positions):
    won = False
    win = 'red'
    won, win = horizontalWin(positions)
    return won, win
    
            

def horizontalWin(positions):
    for i in range(7):
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
    