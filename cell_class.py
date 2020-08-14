import pygame
from pygame.locals import *
import constants

"""ALEXANDRE: Classe mère de la classe "Plateau" et "Piece".
                  Elle contiendra toutes les informations d'une case :
                  - sa position x (int)
                  - sa position y (int)
                  - si la case est sélectionnée ou non (bool)
                  - si la case est rempli ou non (bool)
                  - la texture de la case lorsqu'elle est sélectionnée
                  - la texture de la case lorsqu'elle n'est pas sélectionnée
                  - la texture de la case qui sera utilisé pour l'afficher (par défaut = texture non sélectionnée)"""


class Cell:
        
    def __init__(self, x_pos, y_pos, unselected_texture=constants.boardCellTexture, selected_texture=constants.boardCellTexture, cant_place_texture=constants.boardCellTexture, empty=True, select=False):
        
        self.x = x_pos
        self.y = y_pos
        
        self.empty = empty
        self.select = select
        
        self.unselectedTexture = pygame.image.load(unselected_texture).convert_alpha()
        self.selectedTexture = pygame.image.load(selected_texture).convert_alpha()
        self.cantPlaceTexture = pygame.image.load(cant_place_texture).convert_alpha()
        self.texture = self.unselectedTexture
