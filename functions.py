import pygame
from pygame.locals import *

import piece_class
import cell_class
import constants

import random

def create_piece(cellsArgumentList):
    """Create cells from the cellsArgumentList and return a piece"""

    pieceList = []
    
    for cell in cellsArgumentList:
        pieceList.append(cell_class.Cell(cell["x"], cell["y"]))
        
    piece = piece_class.Piece(pieceList)
        
    return piece

def generate_pieces():
    """Generate and return 3 random pieces using "create_piece" function."""

    randomCellsArgumentList = random.choice(constants.PIECELIST)
    piece1 = [create_piece(randomCellsArgumentList)]

    randomCellsArgumentList = random.choice(constants.PIECELIST)
    piece2 = [create_piece(randomCellsArgumentList)]

    randomCellsArgumentList = random.choice(constants.PIECELIST)
    piece3 = [create_piece(randomCellsArgumentList)]

    return piece1, piece2, piece3

def get_best_score():
    """Read the file "Score.txt" to get the best score from the last run of the project."""

    with open("Score.txt", 'r') as scoreFile:
        bestScore = scoreFile.read()

    return bestScore

def set_new_best_score_or_not(actualScore, newBestScore):
    """If the actual score is higher than the best score, set the actual score as best score,
    replacing it in the file "Score.txt"."""

    if actualScore > newBestScore:
        with open("Score.txt", "w") as scoreFile:
            scoreFile.write(str(actualScore))

def check_game_over(boardPlaceTestList):
    """Check in the "boardPlaceTestList" if there is still a piece that can be placed on the board.
    If there is not, retrun gameOverTest as true else as false."""

    gameOverTest = False

    for currentTest in boardPlaceTestList:
        if currentTest == True:
            gameOverTest = False
            break
        elif currentTest == False:
            gameOverTest = True

    return gameOverTest

def check_moove(piece, cellsPiecePositionBeforeAction):
    """Check if a piece has mooved
    Take in argument: -an array that contain the position of each cell before a possible action of the player
                      -the piece after the possible to compare to the array
    Return: -True if the arrays are the same, it means the position of the piece did not change
            -False if the arrays are diferent, it means that the position of the piece changed"""

    counter = 0
    didNotMoove = True
    for cells in piece[0].cellsList:
        if cellsPiecePositionBeforeAction[counter][0] == cells.x and cellsPiecePositionBeforeAction[counter][1] == cells.y:
            didNotMoove = True
        else:
            didNotMoove = False
            break
        counter += 1
    return didNotMoove
