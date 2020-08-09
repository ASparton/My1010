import pygame
from pygame.locals import *
import constantes

"""ARAMIS + ALEXANDRE: Classe qui va nous permettre de manipuler les pièces au cours du jeu.
               Une pièce est une liste de cases, elle se créera donc grâce à la classe "Case" précédemment écrite.
    
               Attributs:
                   - piece : Pièce choisie lors de la création de l'objet (ARAMIS)
                   - selected : Permet de savoir si la pièce est sélectionnée ou non (ARAMIS)
                   - NbCase : Correspond au nombres de cases de la pièce (ALEXANDRE)
                   - NbCasex : Correspond au nombres de cases horizontales de la pièce (ALEXANDRE)
                   - NbCasey : Correspond au nombres de cases verticales de la pièce (ALEXANDRE)
                    
               Méthodes:
                   - defNbCase : Méthode permettant d'obtenir les "NbCase" (ALEXANDRE)
                   - selectPiece : Méthode qui sélectionne chaque case de la pièce et modifie l'attribut selected (ARAMIS)
                   - moove : Méthode qui permet de déplacer la pièce d'une case vers le haut, le bas, la droite ou la gauche (ARAMIS)
                   - testBordure : Méthode qui permet de replacer la pièce dans la plateau si jamais elle se retrouve à l'extèrieur (ARAMIS)
                   - placePiece : Méthode qui permet de "poser" la pièce dans le plateau et changer son statut placed. (ALEXANDRE)"""


class Piece:
        
    def __init__(self, typePiece, select=False):
        
        self.piece = typePiece
        
        self.selected = select
        self.placed = False
        self.placable = True
        
        self.NbCase = 0
        self.NbCasex = 0
        self.NbCasey = 0
        
    def defNbCase(self):
        """Méthode permettant d'obtenir le nombre de case présent dans la pièce"""
        
        xmax = 0
        ymax = 0
        
        for Case in self.piece:
            self.NbCase = self.NbCase + 1
            
            if xmax < Case.x:
                xmax = Case.x
                
            if ymax < Case.y:
                ymax = Case.y
                
        self.NbCasex = xmax
        self.NbCasey = ymax
          
    def selectPiece(self):
        """Méthode qui permet de sélectionner chaque case de la pièce et de modifier l'attribut selected"""
        
        for Case in self.piece:
            Case.select = True
            Case.texture = Case.texture_selected
            
        self.selected = True
        
    def unselectPiece(self):
        
        for Case in self.piece:
            Case.texture = Case.texture_unselected
            Case.select = False
            
        self.selected = False
        
    def moove(self, direction):
        """Méthode qui permet de déplacer la pièce d'une case vers le haut, le bas, la droite ou la gauche"""
        
        if direction == "droite":
            for Case in self.piece:
                Case.x +=1
                
        if direction == "gauche":
            for Case in self.piece:
                Case.x -=1
                
        if direction == "haut":
            for Case in self.piece:
                Case.y -=1
                
        if direction == "bas":
            for Case in self.piece:
                Case.y +=1
            
    def testBordure(self, piece):
        """Méthode qui a 2 buts:
        - Tester si la pièce est en dehors le plateau
        - Si elle est en dehors du plateau, la faire revenir à sa position précédente grâce à la méthode "moove". """
        
        for case in self.piece:
            if case.x < 0:
                piece.moove("droite")
                break
                
            if case.x > 9:
                piece.moove("gauche")
                break
                
            if case.y < 0:
                piece.moove("bas")
                break
                
            if case.y > 9:
                piece.moove("haut")
                break
                
    def placePiece(self, plateau, piece):
        """Méthode qui permet de poser la pièce dans le plateau :
        - D'abord on a besoin de connaître le nombre de cases de la pièce pour pouvoir utiliser la méthode "PutDownPiece", donc on utilise "defNbCase" 
        - On désélectionne la pièce puisqu'elle va maintenant se placée grâce à la méthode "unselectPiece" 
        - On change les propriétés du plateau des cases du plateau correspondantes en mimétisme avec ceux de la pièce (texture, vide/plein...)
        avec la méthode "PutDownPiece" de la classe Plateau.
        
        - L'attribut "placed" est mainntenant vrai car la pièce est placée."""
        
        piece.unselectPiece()
        plateau.PutDownPiece(piece)
        
        self.placed = True
        for case in piece.piece:
            case.x = 20 + case.x
            case.y = 20 + case.y
