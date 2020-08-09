import pygame
from pygame.locals import *
pygame.init()

"""Screen"""
tailleScreen = [640, 544]

tailleCase = 32

xChoixPiece = 12
yChoixPiece1 = 0
yChoixPiece2 = 6
yChoixPiece3 = 12

"""Textures"""
_Background = "Textures\Background.png"
_Background_game_over = "Textures\Background_game_over.png"

_CasePlateau = "Textures\CaseVide.png"
    
#Cases colorées
_CaseRed = "Textures\CaseRed.png"
_CaseLightBlue = "Textures\CaseLightBlue.png"
_CaseOrange = "Textures\CaseOrange.png"
_CaseYellow = "Textures\CaseYellow.png"
_CaseBlue = "Textures\CaseBlue.png"
_CaseBlack = "Textures\CaseBlack.png"
_CaseBrown = "Textures\CaseBrown.png"
_CaseGreen = "Textures\CaseGreen.png"
_CasePink = "Textures\CasePink.png"
_CasePurple = "Textures\CasePurple.png"

#Cases sélectionnées

_CaseRedSelected = "Textures\CaseRedSelected.png"
_CaseLightBlueSelected = "Textures\CaseLightBlueSelected.png"
_CaseOrangeSelected = "Textures\CaseOrangeSelected.png"
_CaseYellowSelected = "Textures\CaseYellowSelected.png"
_CaseBlueSelected = "Textures\CaseBlueSelected.png"
_CaseBlackSelected = "Textures\CaseBlackSelected.png"
_CaseBrownSelected = "Textures\CaseBrownSelected.png"
_CaseGreenSelected = "Textures\CaseGreenSelected.png"
_CasePinkSelected = "Textures\CasePinkSelected.png"
_CasePurpleSelected = "Textures\CasePurpleSelected.png"

#Cases Impossible à placer

_CaseRedNot = "Textures\CaseRedNot.png"
_CaseLightBlueNot = "Textures\CaseLightBlueNot.png"
_CaseOrangeNot = "Textures\CaseOrangeNot.png"
_CaseYellowNot = "Textures\CaseYellowNot.png"
_CaseBlueNot = "Textures\CaseBlueNot.png"
_CaseBlackNot = "Textures\CaseBlackNot.png"
_CaseBrownNot = "Textures\CaseBrownNot.png"
_CaseGreenNot = "Textures\CaseGreenNot.png"
_CasePinkNot = "Textures\CasePinkNot.png"
_CasePurpleNot = "Textures\CasePurpleNot.png"

#Liste des arguments permettant de créer différentes pièces
listePiece = [
    
    [{"x":0, "y":0,"textureUnselected": _CaseRed, "textureSelected": _CaseRedSelected, 'textureNot': _CaseRedNot}],

    [{"x":0, "y":0,"textureUnselected": _CaseBlue, "textureSelected": _CaseBlueSelected, "textureNot": _CaseBlueNot}, {"x":0, "y":1,"textureUnselected": _CaseBlue, "textureSelected": _CaseBlueSelected, "textureNot": _CaseBlueNot}],
    [{"x":0, "y":0,"textureUnselected": _CaseBlue, "textureSelected": _CaseBlueSelected, "textureNot": _CaseBlueNot}, {"x":1, "y":0,"textureUnselected": _CaseBlue, "textureSelected": _CaseBlueSelected, "textureNot": _CaseBlueNot}],

    [{"x":0, "y":0,"textureUnselected": _CaseLightBlue, "textureSelected": _CaseLightBlueSelected, "textureNot": _CaseLightBlueNot}, {"x":0, "y":1,"textureUnselected": _CaseLightBlue, "textureSelected": _CaseLightBlueSelected, "textureNot": _CaseLightBlueNot}, {"x":0, "y":2,"textureUnselected": _CaseLightBlue, "textureSelected": _CaseLightBlueSelected, "textureNot": _CaseLightBlueNot}],
    [{"x":0, "y":0,"textureUnselected": _CaseLightBlue, "textureSelected": _CaseLightBlueSelected, "textureNot": _CaseLightBlueNot}, {"x":1, "y":0,"textureUnselected": _CaseLightBlue, "textureSelected": _CaseLightBlueSelected, "textureNot": _CaseLightBlueNot}, {"x":2, "y":0,"textureUnselected": _CaseLightBlue, "textureSelected": _CaseLightBlueSelected, "textureNot": _CaseLightBlueNot}],

    [{"x":0, "y":0,"textureUnselected": _CasePurple, "textureSelected": _CasePurpleSelected, "textureNot": _CasePurpleNot}, {"x":0, "y":1,"textureUnselected": _CasePurple, "textureSelected": _CasePurpleSelected, "textureNot": _CasePurpleNot}, {"x":0, "y":2,"textureUnselected": _CasePurple, "textureSelected": _CasePurpleSelected, "textureNot": _CasePurpleNot}, {"x":0, "y":3,"textureUnselected": _CasePurple, "textureSelected": _CasePurpleSelected, "textureNot": _CasePurpleNot}],
    [{"x":0, "y":0,"textureUnselected": _CasePurple, "textureSelected": _CasePurpleSelected, "textureNot": _CasePurpleNot}, {"x":1, "y":0,"textureUnselected": _CasePurple, "textureSelected": _CasePurpleSelected, "textureNot": _CasePurpleNot}, {"x":2, "y":0,"textureUnselected": _CasePurple, "textureSelected": _CasePurpleSelected, "textureNot": _CasePurpleNot}, {"x":3, "y":0,"textureUnselected": _CasePurple, "textureSelected": _CasePurpleSelected, "textureNot": _CasePurpleNot}],
    
    [{"x":0, "y":0,"textureUnselected": _CaseBrown, "textureSelected": _CaseBrownSelected, "textureNot": _CaseBrownNot}, {"x":0, "y":1,"textureUnselected": _CaseBrown, "textureSelected": _CaseBrownSelected, "textureNot": _CaseBrownNot}, {"x":0, "y":2,"textureUnselected": _CaseBrown, "textureSelected": _CaseBrownSelected, "textureNot": _CaseBrownNot}, {"x":0, "y":3,"textureUnselected": _CaseBrown, "textureSelected": _CaseBrownSelected, "textureNot": _CaseBrownNot}, {"x":0, "y":4,"textureUnselected": _CaseBrown, "textureSelected": _CaseBrownSelected, "textureNot": _CaseBrownNot}],
    [{"x":0, "y":0,"textureUnselected": _CaseBrown, "textureSelected": _CaseBrownSelected, "textureNot": _CaseBrownNot}, {"x":1, "y":0,"textureUnselected": _CaseBrown, "textureSelected": _CaseBrownSelected, "textureNot": _CaseBrownNot}, {"x":2, "y":0,"textureUnselected": _CaseBrown, "textureSelected": _CaseBrownSelected, "textureNot": _CaseBrownNot}, {"x":3, "y":0,"textureUnselected": _CaseBrown, "textureSelected": _CaseBrownSelected, "textureNot": _CaseBrownNot}, {"x":4, "y":0,"textureUnselected": _CaseBrown, "textureSelected": _CaseBrownSelected, "textureNot": _CaseBrownNot}],

    [{"x":0, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":1, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":2, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":2, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}],
    [{"x":0, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":1, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":2, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":0, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}],
    [{"x":0, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":1, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":2, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":2, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}],
    [{"x":0, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":1, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":2, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":0, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}],
    [{"x":0, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":0, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":0, "y":2,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":1, "y":2,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}],
    [{"x":0, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":1, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":0, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":0, "y":2,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}],
    [{"x":0, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":1, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":1, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":1, "y":2,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}],
    [{"x":1, "y":0,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":1, "y":1,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":1, "y":2,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}, {"x":0, "y":2,"textureUnselected": _CaseGreen, "textureSelected": _CaseGreenSelected, "textureNot": _CaseGreenNot}],


    [{"x":0, "y":0,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}, {"x":0, "y":1,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}, {"x":1, "y":1,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}],
    [{"x":1, "y":0,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}, {"x":1, "y":1,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}, {"x":0, "y":1,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}],
    [{"x":0, "y":0,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}, {"x":1, "y":0,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}, {"x":0, "y":1,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}],
    [{"x":0, "y":0,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}, {"x":1, "y":0,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}, {"x":1, "y":1,"textureUnselected": _CaseYellow, "textureSelected": _CaseYellowSelected, "textureNot": _CaseYellowNot}],

    [{"x":0, "y":0,"textureUnselected": _CaseBlack, "textureSelected": _CaseBlackSelected, "textureNot": _CaseBlackNot}, {"x":0, "y":1,"textureUnselected": _CaseBlack, "textureSelected": _CaseBlackSelected, "textureNot": _CaseBlackNot}, {"x":1, "y":0,"textureUnselected": _CaseBlack, "textureSelected": _CaseBlackSelected, "textureNot": _CaseBlackNot}, {"x":1, "y":1,"textureUnselected": _CaseBlack, "textureSelected": _CaseBlackSelected, "textureNot": _CaseBlackNot}],

    [{"x":0, "y":0,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":0, "y":1,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":0, "y":2,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":1, "y":2,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":2, "y":2,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}],
    [{"x":2, "y":0,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":2, "y":1,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":2, "y":2,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":1, "y":2,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":0, "y":2,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}],
    [{"x":0, "y":0,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":1, "y":0,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":2, "y":0,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":0, "y":1,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":0, "y":2,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}],
    [{"x":0, "y":0,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":1, "y":0,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":2, "y":0,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":2, "y":1,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}, {"x":2, "y":2,"textureUnselected": _CasePink, "textureSelected": _CasePinkSelected, "textureNot": _CasePinkNot}],

    [{"x":0, "y":0,"textureUnselected": _CaseOrange, "textureSelected": _CaseOrangeSelected, "textureNot": _CaseOrangeNot}, {"x":0, "y":1,"textureUnselected": _CaseOrange, "textureSelected": _CaseOrangeSelected, "textureNot": _CaseOrangeNot}, {"x":0, "y":2,"textureUnselected": _CaseOrange, "textureSelected": _CaseOrangeSelected, "textureNot": _CaseOrangeNot}, {"x":1, "y":0,"textureUnselected": _CaseOrange, "textureSelected": _CaseOrangeSelected, "textureNot": _CaseOrangeNot}, {"x":1, "y":1,"textureUnselected": _CaseOrange, "textureSelected": _CaseOrangeSelected, "textureNot": _CaseOrangeNot}, {"x":1, "y":2,"textureUnselected": _CaseOrange, "textureSelected": _CaseOrangeSelected, "textureNot": _CaseOrangeNot}, {"x":2, "y":0,"textureUnselected": _CaseOrange, "textureSelected": _CaseOrangeSelected, "textureNot": _CaseOrangeNot}, {"x":2, "y":1,"textureUnselected": _CaseOrange, "textureSelected": _CaseOrangeSelected, "textureNot": _CaseOrangeNot}, {"x":2, "y":2,"textureUnselected": _CaseOrange, "textureSelected": _CaseOrangeSelected, "textureNot": _CaseOrangeNot}],
]

#Police pour le text(game over)
font = pygame.font.SysFont("dearsunshine", 64)
