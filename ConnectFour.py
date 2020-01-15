import pygame
pygame.init()

canvasWidth = 500 # sets size of window
canvasHeight = 500
#TODO move everything down and add a title at the top to say whos turn it is
win = pygame.display.set_mode((canvasWidth, canvasHeight)) #creates the surface for everything to be drawn on
pygame.display.set_caption("Connect Four")  #sets the name of the window



def main():
    makeBoard()
    positions = []
    for i in range(6):
        positions.append([])
        for j in range(7):
            positions[i].append(' ')
    # make the initiol board
    # initialize a 2D array of 6 by 7
    # fill the array with empty strings
    


def makeBoard():
    #TODO
    