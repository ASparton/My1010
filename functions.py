import pygame
from pygame.locals import *

import piece_class
import cell_class
import constants

import random

"""Cells creation to create pieces.
    -Take: list of arguments to create cells
    -Return: the piece created"""
def create_piece(cellList):
    
    pieceList = []
    
    for cell in cellList:
        pieceList.append(cell_class.Cell(cell["x"], cell["y"], cell["textureUnselected"], cell["textureSelected"], cell["textureNot"]))
        
    piece = piece_class.Piece(pieceList)
        
    return piece

def generate_pieces():

    randomCellList = random.choice(constants.pieceList)
    piece1 = [create_piece(randomCellList)]

    randomCellList = random.choice(constants.pieceList)
    piece2 = [create_piece(randomCellList)]

    randomCellList = random.choice(constants.pieceList)
    piece3 = [create_piece(randomCellList)]

    return piece1, piece2, piece3

def get_best_score():

    with open("Score.txt", 'r') as scoreFile:
        bestScore = scoreFile.read()

    return bestScore

def set_new_best_score_or_not(actualScore, newBestScore):

    if actualScore > newBestScore:
        with open("Score.txt", "w") as scoreFile:
            scoreFile.write(str(actualScore))

def check_game_over(boardPlaceTestList):

    gameOverTest = False

    for currentTest in boardPlaceTestList:
        if currentTest == True:
            gameOverTest = False
            break
        elif currentTest == False:
            gameOverTest = True

    return gameOverTest
