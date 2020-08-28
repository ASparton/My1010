import pygame
from pygame.locals import *
import constants

"""Class that create a button:
   - Position
   - Unselected and selected textures
   - Function of the button: "play", "exit", "mainMenu", "settings". """
class Button:
        
    def __init__(self, function, x_pos, y_pos, unselected_texture, selected_texture, selected=False):
        """function = "play" OR "exit" OR "home" OR "settings" """
        self._function = function

        self._x = x_pos
        self._y = y_pos
        
        self._selected = selected
        
        self._unselectedTexture = pygame.image.load(unselected_texture).convert_alpha()
        self._selectedTexture = pygame.image.load(selected_texture).convert_alpha()
        
        if self._selected:
            self._texture = self._selectedTexture
        else:
            self._texture = self._unselectedTexture

    """Properties"""
    #Position (x and y) properties
    def _get_x(self):
        return self._x
    def _set_x(self, x_pos):
        self._x = x_pos
    x = property(_get_x, _set_x)
    def _get_y(self):
        return self._y
    def _set_y(self, y_pos):
        self._y = x_pos
    y = property(_get_y, _set_y)
    #Textures properties
    def _get_unselectedTexture(self):
        return self._unselectedTexture
    def _set_unselectedTexture(self, unselectedTexture):
        self._unselectedTexture = unselectedTexture
    unselectedTexture = property(_get_unselectedTexture, _set_unselectedTexture)
    def _get_selectedTexture(self):
        return self._selectedTexture
    def _set_selectedTexture(self, selectedTexture):
        self._selectedTexture = selectedTexture
    selectedTexture = property(_get_selectedTexture, _set_selectedTexture)
    def _get_texture(self):
        return self._texture
    def _set_texture(self, texture):
        self._texture = texture
    texture = property(_get_texture, _set_texture)
    #selected propertie
    def _get_selected(self):
        return self._selected
    def _set_selected(self, selected):
        self._selected = selected

        if self._selected == True:
            self.texture = self.selectedTexture
        else:
            self.texture = self.unselectedTexture

    selected = property(_get_selected, _set_selected)

    def do_function(self):
        phase = 0
        runGame = True
        boardSettingsClosed = True

        if self._function == "play":
            phase = "game"
            return phase
            
        elif self._function == "exit":
            runGame = False
            return runGame

        elif self._function == "home":
            phase = "main_menu"
            return  phase

        elif self._function == "settings":
            boardSettingsClosed = False
            return boardSettingsClosed
            