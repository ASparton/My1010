import pygame
from pygame.locals import *
import constantes

"""ALEXANDRE: Classe mère de la classe "Plateau" et "Piece".
                  Elle contiendra toutes les informations d'une case :
                  - sa position x (int)
                  - sa position y (int)
                  - si la case est sélectionnée ou non (bool)
                  - si la case est rempli ou non (bool)
                  - la texture de la case lorsqu'elle n'est pas sélectionnée
                  - la texture de la case lorsqu'elle n'est pas sélectionnée
                  - la texture de la case qui sera utilisé pour l'afficher (par défaut = texture non sélectionnée)"""


class Case:
        
    def __init__(self, pos_x, pos_y, texture_unselected=constantes._CasePlateau, texture_selected=constantes._CasePlateau, texture_not=constantes._CasePlateau, vide=True, select=False):
        
        self.x = pos_x
        self.y = pos_y
        
        self.vide = vide
        self.select = select
        
        self.texture_unselected = pygame.image.load(texture_unselected).convert_alpha()
        self.texture_selected = pygame.image.load(texture_selected).convert_alpha()
        self.texture_not = pygame.image.load(texture_not).convert_alpha()
        self.texture = self.texture_unselected
