import pygame
from pygame.locals import *
import constants

"""Mother's class of "Board" and "Piece".
                  Contain all the informations about a cell :
                  - it's position (X an Y axis)
                  - selected attribute
                  - empty attribute
                  - the texture when it's selected
                  - the texture when it's not selected
                  - the texture when it can't be placed on the board"""
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