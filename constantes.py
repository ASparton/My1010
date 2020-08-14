import pygame
from pygame.locals import *
pygame.init()

"""Screen"""
screenSize = [640, 544]

cellSize = 32

pieceChoosePlaceX = 12
pieceChoosePlaceY1 = 0
pieceChoosePlaceY2 = 6
pieceChoosePlaceY3 = 12

"""Textures"""
backgroundTexture = "Textures\Background.png"
gameOverBackgroundTexture = "Textures\Background_game_over.png"

boardCellTexture = "Textures\CaseVide.png"
    
#Cases colorées
redCellTexture = "Textures\CaseRed.png"
lightBlueCellTexture = "Textures\CaseLightBlue.png"
orangeCellTexture = "Textures\CaseOrange.png"
yellowCellTexture = "Textures\CaseYellow.png"
blueCellTexture = "Textures\CaseBlue.png"
blackCellTexture = "Textures\CaseBlack.png"
brownCellTexture = "Textures\CaseBrown.png"
greenCellTexture = "Textures\CaseGreen.png"
pinkCellTexture = "Textures\CasePink.png"
purpleCellTexture = "Textures\CasePurple.png"

#Cases sélectionnées

redCellSelectedTexture = "Textures\CaseRedSelected.png"
lightBlueCellSelectedTexture = "Textures\CaseLightBlueSelected.png"
orangeCellSelectedTexture = "Textures\CaseOrangeSelected.png"
yellowCellSelectedTexture = "Textures\CaseYellowSelected.png"
blueCellSelectedTexture = "Textures\CaseBlueSelected.png"
blackCellSelectedTexture = "Textures\CaseBlackSelected.png"
brownCellSelectedTexture = "Textures\CaseBrownSelected.png"
greenCellSelectedTexture = "Textures\CaseGreenSelected.png"
pinkCellSelectedTexture = "Textures\CasePinkSelected.png"
purpleCellSelectedTexture = "Textures\CasePurpleSelected.png"

#Cases Impossible à placer

redCantPlaceTexture = "Textures\CaseRedNot.png"
lightBlueCantPlaceTexture = "Textures\CaseLightBlueNot.png"
orangeCantPlaceTexture = "Textures\CaseOrangeNot.png"
yellowCantPlaceTexture = "Textures\CaseYellowNot.png"
blueCantPlaceTexture = "Textures\CaseBlueNot.png"
blackCantPlaceTexture = "Textures\CaseBlackNot.png"
brownCantPlaceTexture = "Textures\CaseBrownNot.png"
greenCantPlaceTexture = "Textures\CaseGreenNot.png"
pinkCantPlaceTexture = "Textures\CasePinkNot.png"
purpleCantPlaceTexture = "Textures\CasePurpleNot.png"

#Liste des arguments permettant de créer différentes pièces
pieceList = [
    
    [{"x":0, "y":0,"textureUnselected": redCellTexture, "textureSelected": redCellSelectedTexture, "textureNot": redCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": blueCellTexture, "textureSelected": blueCellSelectedTexture, "textureNot": blueCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": blueCellTexture, "textureSelected": blueCellSelectedTexture, "textureNot": blueCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": blueCellTexture, "textureSelected": blueCellSelectedTexture, "textureNot": blueCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": blueCellTexture, "textureSelected": blueCellSelectedTexture, "textureNot": blueCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":0, "y":3,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":3, "y":0,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}],
    
    [{"x":0, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":0, "y":3,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":0, "y":4,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":3, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":4, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":1, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],


    [{"x":0, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}],
    [{"x":1, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": blackCellTexture, "textureSelected": blackCellSelectedTexture, "textureNot": blackCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": blackCellTexture, "textureSelected": blackCellSelectedTexture, "textureNot": blackCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": blackCellTexture, "textureSelected": blackCellSelectedTexture, "textureNot": blackCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": blackCellTexture, "textureSelected": blackCellSelectedTexture, "textureNot": blackCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}],
    [{"x":2, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":2, "y":2,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}],
]

#Police pour le text(game over)
font = pygame.font.SysFont("dearsunshine", 64)
