import pygame
from pygame.locals import *
import constants

"""Classe qui va nous permettre de manipuler les pièces au cours du jeu.
               Une pièce est une liste de cases, elle se créera donc grâce à la classe "Case" précédemment écrite.
    
               Attributs:
                   - piece : Pièce choisie lors de la création de l'objet
                   - selected : Permet de savoir si la pièce est sélectionnée ou non
                   - NbCase : Correspond au nombres de cases de la pièce
                   - NbCasex : Correspond au nombres de cases horizontales de la pièce 
                   - NbCasey : Correspond au nombres de cases verticales de la pièce 
                    
               Méthodes:
                   - defNbCase : Méthode permettant d'obtenir les "NbCase" 
                   - selectPiece : Méthode qui sélectionne chaque case de la pièce et modifie l'attribut selected
                   - moove : Méthode qui permet de déplacer la pièce d'une case vers le haut, le bas, la droite ou la gauche
                   - testBordure : Méthode qui permet de replacer la pièce dans la plateau si jamais elle se retrouve à l'extèrieur
                   - placePiece : Méthode qui permet de "poser" la pièce dans le plateau et changer son statut placed."""


class Piece:
        
    def __init__(self, pieceType, select=False):
        
        self.piece = pieceType
        
        self.selected = select
        self.placed = False
        self.canBePlaced = True
        
        self.cellNumber = 0
        self.cellNumberX = 0
        self.cellNumberY = 0
        
    def def_cell_number(self):
        """Méthode permettant d'obtenir le nombre de case présent dans la pièce"""
        
        xmax = 0
        ymax = 0
        
        for cell in self.piece:
            self.cellNumber = self.cellNumber + 1
            
            if xmax < cell.x:
                xmax = cell.x
                
            if ymax < cell.y:
                ymax = cell.y
                
        self.cellNumberX = xmax
        self.cellNumberY = ymax
          
    def select(self):
        """Méthode qui permet de sélectionner chaque case de la pièce et de modifier l'attribut selected"""
        
        for cell in self.piece:
            cell.select = True
            cell.texture = cell.selectedTexture
            
        self.selected = True
        
    def unselect(self):
        
        for cell in self.piece:
            cell.texture = cell.unselectedTexture
            cell.select = False
            
        self.selected = False
        
    def moove(self, direction):
        """Method to moove the piece to the 4 directions"""
        
         #Variable that allow or not a piece to moove after testing if each cell of that piece will still be in the board
        canMoove = True

        if direction == "right":
            for cell in self.piece:
                if (cell.x + 1) > 9:
                    canMoove = False
            
            if canMoove == True:
                for cell in self.piece:
                    cell.x += 1
                
        if direction == "left":
            for cell in self.piece:
                if (cell.x - 1) < 0:
                    canMoove = False

            if canMoove == True:
                for cell in self.piece:        
                    cell.x -=1
                
        if direction == "up":
            for cell in self.piece:
                if (cell.y - 1) < 0:
                    canMoove = False

            if canMoove == True:
                for cell in self.piece:
                    cell.y -=1
                
        if direction == "down":
            for cell in self.piece:
                if (cell.y + 1) > 9:
                    canMoove = False

            if canMoove == True:
                for cell in self.piece:
                    cell.y +=1
            
    def place_piece(self, board, piece):
        """Méthode qui permet de poser la pièce dans le plateau :
        - D'abord on a besoin de connaître le nombre de cases de la pièce pour pouvoir utiliser la méthode "PutDownPiece", donc on utilise "defNbCase" 
        - On désélectionne la pièce puisqu'elle va maintenant se placée grâce à la méthode "unselectPiece" 
        - On change les propriétés des cases du plateau correspondantes en mimétisme avec ceux de la pièce (texture, vide/plein...)
        avec la méthode "PutDownPiece" de la classe Plateau.
        
        - L'attribut "placed" est maintenant vrai car la pièce est placée."""
        
        piece.unselect()
        board.put_down_piece(piece)
        
        self.placed = True
        for cell in piece.piece:
            cell.x = 20 + cell.x
            cell.y = 20 + cell.y
