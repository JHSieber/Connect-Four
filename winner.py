def main():
    positionsRed = [
        ['','','','','','',''],
        ['','','','','','',''],
        ['red','','','','','',''],
        ['','red','','','','',''],
        ['','','red','','','',''],
        ['','','','red','','','']]
    positionsBlue = [
        ['','','','','','blue',''],
        ['','','','','blue','',''],
        ['','','','blue','','',''],
        ['','','blue','','','',''],
        ['','','','','','',''],
        ['','','','','','','']]
    if winner(positionsBlue, 4,2, 'blue'):
        print(winner(positionsBlue, 4,2, 'blue'), 'is the winner')

def winner(positions, row, col, color):
    if checkDownLeft(positions, row, col, color) + checkUpRight(positions, row, col, color) >= 4: #check for the right diagonal
        return color
    elif checkDownRight(positions, row, col, color) + checkUpLeft(positions, row, col, color) >= 4: #check for the left diagonal
        return color
    elif checkDown(positions, row, col, color) + checkUp(positions, row, col, color) >= 4: #check for vertical win
        return color
    elif checkRight(positions, row, col, color) + checkLeft(positions, row, col, color) >=4: #check for horizontal win
        return color
    else:
        return False

def checkDownLeft(positions, row, col, color):
    if row > 4 or col < 1: #the cell is out of bounds
        return 1
    elif positions[row][col] != ' ' and positions[row][col] == positions[row+1][col-1]: #the current cell is not empty and is the same as the next cell in the line
        return 1 + checkDownLeft(positions, row+1, col-1, color) #recurse with the next cell
    else: #either the current cell is empty or the current cell does not equal the next cell
        return 1
    
    
def checkUpLeft(positions, row, col, color):
    if col < 1 or row < 1:
        return 1
    elif positions[row][col] == positions[row-1][col-1] and positions[row][col] != ' ':
        return 1 + checkUpLeft(positions, row-1, col-1, color)
    else:
        return 1
    
def checkUpRight(positions, row, col, color):
    if col > 5 or row < 1:
        return 1
    elif positions[row][col] == positions[row-1][col+1] and positions[row][col] != ' ':
        return 1 + checkUpRight(positions, row-1, col+1, color)
    else:
        return 1
    
def checkDownRight(positions, row, col, color):
    if col > 5 or row > 4:
        return 1
    elif positions[row][col] == positions[row+1][col+1] and positions[row][col] != ' ':
        return 1 + checkDownRight(positions, row+1, col+1, color)
    else:
        return 1
    
def checkUp(positions, row, col, color):
    if row < 1:
        return 1
    elif positions[row][col] == positions[row-1][col] and positions[row][col] != ' ':
        return 1 + checkUp(positions, row-1, col, color)
    else:
        return 1
    
def checkDown(positions, row, col, color):
    if row > 4:
        return 1
    elif positions[row][col] == positions[row+1][col] and positions[row][col] != ' ':
        return 1 + checkDown(positions, row+1, col, color)
    else:
        return 1
    
def checkRight(positions, row, col, color):
    if col > 5:
        return 1
    elif positions[row][col] == positions[row][col+1] and positions[row][col] != ' ':
        return 1 + checkRight(positions, row, col+1, color)
    else:
        return 1
    
def checkLeft(positions, row, col, color):
    if col < 1:
        return 1
    elif positions[row][col] == positions[row][col-1] and positions[row][col] != ' ':
        return 1 + checkLeft(positions, row, col-1, color)
    else:
        return 1
    
main()
