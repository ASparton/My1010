import pygame
from pygame.locals import *

import piece_class
import cell_class
import constants

"""Creation des cases (pour créer les pièces)
    -Argument: liste d'argument de création pour la case
    -Retourne: L'objet piece correspondant"""
def create_piece(cellList):
    
    pieceList = []
    
    for cell in cellList:
        pieceList.append(cell_class.Cell(cell["x"], cell["y"], cell["textureUnselected"], cell["textureSelected"], cell["textureNot"]))
        
    piece = piece_class.Piece(pieceList)
        
    return piece

"""Fonction appelée lors d'un game over.
    -Argument: gameOver (true or false)
    -Retourne: True si on est bien en game over"""
def game_over(gameOver, gameOverSound):

    if gameOver == True:
        gameOverSound.play()
        return True
    else:
        return False
