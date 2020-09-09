import pygame
from pygame.locals import *
import constants

import button_class

class SoundSettings:
        
    def __init__(self, xPos, yPos, texture=constants.SOUNDSETTINGSTEXTURE):
        
        self._x = xPos
        self._y = yPos

        self._musicOn = True
        self._soundOn = True
        self._musicOnButton = button_class.Button("music", 12, 25, "", True, constants.MUSICONBUTTONTEXTURE, constants.MUSICONBUTTONSELECTEDTEXTURE)
        self._musicOffButton = button_class.Button("music", 12, 25, "", False, constants.MUSICOFFBUTTONTEXTURE, constants.MUSICOFFBUTTONSELECTEDTEXTURE)
        self._soundOnButton = button_class.Button("sound", 138, 25, "", False, constants.SOUNDONBUTTONTEXTURE, constants.SOUNDONBUTTONSELECTEDTEXTURE)
        self._soundOffButton = button_class.Button("sound", 138, 25, "", False, constants.SOUNDOFFBUTTONTEXTURE, constants.SOUNDOFFBUTTONSELECTEDTEXTURE)

        self._close = True
        self._exitButton = button_class.Button("exitSettings", 0, 0, "EXIT")
        self._exitButton.selectedTexture = pygame.transform.scale(self._exitButton.selectedTexture, (self._exitButton.selectedTexture.get_size()[0]//4, self._exitButton.selectedTexture.get_size()[1]//4))
        self._exitButton.unselectedTexture = pygame.transform.scale(self._exitButton.unselectedTexture, (self._exitButton.unselectedTexture.get_size()[0]//4, self._exitButton.unselectedTexture.get_size()[1]//4))
        self._exitButton.texture = self._exitButton.unselectedTexture
        self._exitButton.set_button_title("EXIT", 18)

        self._selectedButton = 0

        self._texture = pygame.image.load(texture).convert_alpha()

    """Properties"""
    #Position properties
    def _get_x(self):
        return self._x
    def _set_x(self, xPos):
        self._x = xPos
    x = property(_get_x, _set_x)
    def _get_y(self):
        return self._y
    def _set_y(self, yPos):
        self._y = yPos
    y = property(_get_y, _set_y)
    #Exit property
    def _get_close(self):
        return self._close
    def _set_close(self, close):
        self._close = close
        self._exitButton.selected = False
        if self._musicOn:
            self._musicOnButton.selected = True
            self._selectedButton = self._musicOnButton
        else:
            self._musicOffButton.selected = True
            self._selectedButton = self._musicOffButton
    close = property(_get_close, _set_close)
    #Exit button property
    def _get_exitButton(self):
        return self._exitButton
    exitButton = property(_get_exitButton)
    #Texture property
    def _get_texture(self):
        return self._texture
    texture = property(_get_texture)
    #Music/Sound on properties
    def _get_soundOn(self):
        return self._soundOn
    def _set_soundOn(self, onOrOff):
        self._soundOn = onOrOff
    soundOn = property(_get_soundOn, _set_soundOn)
    def _get_musicOn(self):
        return self._musicOn
    def _set_musicOn(self, onOrOff):
        self._musicOn = onOrOff
    musicOn = property(_get_musicOn, _set_musicOn)
    #Buttons properties
    def _get_musicOnButton(self):
        return self._musicOnButton
    musicOnButton = property(_get_musicOnButton)
    def _get_musicOffButton(self):
        return self._musicOffButton
    musicOffButton = property(_get_musicOffButton)
    def _get_soundOnButton(self):
        return self._soundOnButton
    soundOnButton = property(_get_soundOnButton)
    def _get_soundOffButton(self):
        return self._soundOffButton
    soundOffButton = property(_get_soundOffButton)
    #SelectedButton property
    def _get_selectedButton(self):
        return self._selectedButton
    selectedButton = property(_get_selectedButton)

    def selectNextButton(self, direction):
        if direction == "left":
            if self._soundOnButton.selected:
                self._soundOnButton.selected = False

                if self._musicOn:
                    self._musicOnButton.selected = True
                    self._selectedButton = self._musicOnButton
                elif not self._musicOn:
                    self._musicOffButton.selected = True
                    self._selectButton = self._musicOffButton

            elif self._soundOffButton.selected:
                self._soundOffButton.selected = False

                if self._musicOn:
                    self._musicOnButton.selected = True
                    self._selectButton = self._musicOnButton
                elif not self._musicOn:
                    self._musicOffButton.selected = True
                    self._selectedButton = self._musicOffButton

        elif direction == "right":
            if self._musicOnButton.selected:
                self._musicOnButton.selected = False

                if self._soundOn:
                    self._soundOnButton.selected = True
                    self._selectedButton = self._soundOnButton
                elif not self._soundOn:
                    self._soundOffButton.selected = True
                    self._selectedButton = self._soundOffButton
            
            elif self._musicOffButton.selected:
                self._musicOffButton.selected = False

                if self._soundOn:
                    self._soundOnButton.selected = True
                    self._selectedButton = self._soundOnButton
                elif not self._soundOn:
                    self._soundOffButton.selected = True
                    self._selectedButton = self._soundOffButton

        elif direction == "up":
            if self._musicOnButton.selected:
                self._musicOnButton.selected = False
            elif self._musicOffButton.selected:
                self._musicOffButton.selected = False
            elif self._soundOnButton.selected:
                self._soundOnButton.selected = False
            elif self._soundOffButton.selected:
                self._soundOffButton.selected = False
            self._exitButton.selected = True
            self._selectedButton = self._exitButton

        elif direction == "down" and self._selectedButton == self._exitButton:
            self._exitButton.selected = False
            if self._musicOn:
                self._musicOnButton.selected = True
                self._selectedButton = self._musicOnButton
            else:
                self._musicOffButton.selected = True
                self._selectedButton = self._musicOffButton

    def set_music(self, onOrOff):
        self._musicOn = onOrOff
        if onOrOff:
            self.musicOnButton.selected = True
            self._selectedButton = self._musicOnButton
            self.musicOffButton.selected = False
        else:
            self.musicOffButton.selected = True
            self._selectedButton = self._musicOffButton
            self.musicOnButton.selected = False
            
    def set_sound(self, onOrOff):
        self._soundOn = onOrOff
        if onOrOff:
            self.soundOnButton.selected = True
            self._selectedButton = self._soundOnButton
            self.soundOffButton.selected = False
        else:
            self.soundOffButton.selected = True
            self._selectedButton = self._soundOffButton
            self.soundOnButton.selected = False