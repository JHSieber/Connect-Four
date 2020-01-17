import pygame
pygame.init()

canvasWidth = 500 # sets size of window
canvasHeight = 500
win = pygame.display.set_mode((canvasWidth, canvasHeight)) #creates the surface for everything to be drawn on
pygame.display.set_caption("Connect Four")  #sets the name of the window



def main():
    makeBoard()
    positions = []
    for i in range(6):
        positions.append([])
        for j in range(7):
            positions[i].append(' ')
    run = True
    color = 'red'
    won = False
    #win = 'red'
    while run:
        pygame.time.delay(100)
        
        for event in pygame.event.get(): #allows us to quit when we hit the close button
            if event.type == pygame.QUIT:
                run = False
        
        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos() #gets the current x and y of the mouse
            color, positions, position = makeTurn(positions, color, mouseX)
            drawMove(color, position)
        won, win = winner(positions, color)
        if won:
            print(win, "is the winner")
            run = False
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

def makeTurn(positions, color, mouseX): #had to change some stuff so if something doesnt work it may be here
    if mouseX > 0 and mouseX < canvasWidth/7: #first column
        for i in range(5,-1,-1): #iterate backwards through each row of the columnn from the bottom to the top 
            if positions[i][0] == ' ': #check if there is already one there
                positions[i][0] = color #fill spot in array with correct color
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
            if positions[i][1] == ' ':
                positions[i][1] = color
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
            if positions[i][2] == ' ':
                positions[i][2] = color
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
            if positions[i][3] == ' ':
                positions[i][3] = color
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
            if positions[i][4] == ' ':
                positions[i][4] = color
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
            if positions[i][5] == ' ':
                positions[i][5] = color
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
            if positions[i][6] == ' ':
                positions[i][6] = color
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

def winner(positions, color):
    #check for horizontal wins
    for i in range(6): #iterate through each row
        total = 1
        for j in range(1,7): #iterate through all but the first column
            if positions[i][j] == positions[i][j-1]: #if the next color on the line is the same as the previous then increase total
                if positions[i][j] != ' ' and positions[i][j-1] != ' ':
                    total+=1
                    if total == 4:
                        return True, color
            else:
                total = 1
    
    #check for verticle wins
    for i in range(7): #iterate through each column
        total = 1
        for j in range(1,6): #iterate through each row in the column
            if positions[j][i] == positions[j-1][i]: #check if the color is the same as the one above it
                if positions[j][i] != ' ' and positions[j-1][i] != ' ':
                    total+=1
                    if total == 4:
                        return True, color
    
    #check for diagonal left
    for i in range(5,2,-1): #checks bottom 3 rows
        for j in range (3,7): #checks right 4 columns
            print(checkUpLeft(positions, i, j))
            if checkUpLeft(positions, i, j) == 4:
                return True, positions[i][j]
    return False, ' '

def checkUpLeft(positions, row, col):
    if col < 0 or row < 0:
        return 0
    if positions[row][col] == positions[row-1][col-1] and positions[row][col] != ' ':
        return 1 + checkUpLeft(positions, col-1, row-1)
    else:
        return 0
    
            

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
    