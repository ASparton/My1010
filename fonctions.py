import pygame
from pygame.locals import *

import c_Piece
import c_Case
import constantes

"""Creation des cases (pour créer les pièces)
    -Argument: liste d'argument de création pour la case
    -Retourne: L'objet piece correspondant"""
def create_piece(listeCase):
    
    pieceList = []
    
    for case in listeCase:
        pieceList.append(c_Case.Case(case["x"], case["y"], case["textureUnselected"], case["textureSelected"], case["textureNot"]))
        
    piece = c_Piece.Piece(pieceList)
        
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
