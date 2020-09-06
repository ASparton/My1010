import pygame
from pygame.locals import *
import constants

"""Mother's class of "Board" and "Piece".
                  Contain all the informations about a cell :
                  - it's position (X an Y axis)
                  - empty attribute
                  - the texture when it's selected
                  - the texture when it's not selected
                  - the texture when it can't be placed on the board"""
class Cell:
        
    def __init__(self, x_pos, y_pos, unselected_texture=constants.UNSELECTEDCELLTEXTURE, selected_texture=constants.SELECTEDCELLTEXTURE, cant_place_texture=constants.CANTPLACECELLTEXTURE, empty=True, selected=False):
        
        self.x = x_pos
        self.y = y_pos

        self._initialX = x_pos
        self._initialY = y_pos
        
        self.selected = selected
        self.empty = empty
        
        self.unselectedTexture = pygame.image.load(unselected_texture).convert_alpha()
        self.selectedTexture = pygame.image.load(selected_texture).convert_alpha()
        self.cantPlaceTexture = pygame.image.load(cant_place_texture).convert_alpha()
        self.texture = self.unselectedTexture

    #initialPosition properties
    def _get_initialX(self):
        return self._initialX
    initialX = property(_get_initialX)
    def _get_initialY(self):
        return self._initialY
    initialY = property(_get_initialY)