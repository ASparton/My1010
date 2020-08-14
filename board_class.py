import pygame
from pygame.locals import *

import constantes
import cell_class

"""ALEXANDRE: Classe permettant de gérer le plateau. 
    
                  Le plateau est un liste de cases, on utilisera ainsi la classe "Case" précédemment écrite.
                
                  Atrributs:
                      -taille_x : nombre de case en longueur du plateau
                      -taille_y : nombre de case en largeur du plateau
                      -listeCase : liste des cases qui composent le plateau (Longueur*Largeur)
                
                  Méthodes:
                      - Construct : Construction du plateau
                      - PlaceVerification : Vérifie si la ou les pièces sont posables sur plateau
                      - PlayerPlaceVerification : Vérifie si l'emplacement où le joueur décide de poser la pièce est libre
                      - LineVerificationSuppression : Vérifie si une ligne du plateau est remplie, et si oui, supprime la ligne"""
class Board:
        
    def __init__(self, x=10, y=10):
        
        self.x_size = x
        self.y_size = y
        self.cellList = []
           
    def construct(self):
        """Méthode de construction du plateau"""
        
        x_counter = 0
        y_counter = 0
        
        while(y_counter < self.y_size):
            while(x_counter < self.x_size):
                self.cellList.append(cell_class.Cell(x_counter, y_counter))
                x_counter += 1
            
            y_counter += 1
            x_counter = 0
            
    def place_verification(self, piece):
        """Méthode pour vérifier si une pièce est posable sur le plateau: 
           - Prend en paramêtre la pièce que l'on veut tester
           - Renvoie le booléen "test", pour dire si oui ou non la pièce est posable sur le plateau."""
        
        test = False
        currentTest = False
        cellToTest = [0,0]
        
        xMaxTest = 10 - piece.cellNumberX
        yMaxTest = 10 - piece.cellNumberY
        
        for boardCell in self.cellList:
            
            if boardCell.x < xMaxTest and boardCell.y < yMaxTest:         
            
                for pieceCell in piece.piece:
                
                    cellToTest[0] = boardCell.x + pieceCell.x
                    cellToTest[1] = boardCell.y + pieceCell.y
                    
                    for boardCellToTest in self.cellList:
                        if boardCellToTest.x == cellToTest[0] and boardCellToTest.y == cellToTest[1]:
                            if boardCellToTest.empty == False:
                                currentTest = False
                                break
                            elif boardCellToTest.empty == True:
                                currentTest = True
                                break
                                
                    if currentTest == False:
                        break
                        
                if currentTest == True:
                    test = True
                    break
                    
                elif currentTest == False:
                    test = False
        
        return test
        
    def player_place_verification(self, piece):
        """Méthode pour vérifier si là où le joueur décide de poser sa pièce est bien libre:
           - Prend en paramêtre la pièce que le joueur veut essayer de poser
           - Retourn le booléen "test" pour dire si oui ou non la pièce est posable là où l'utilisateur veut la poser."""
        
        test = True
        
        for pieceCell in piece.piece:
            for boardCell in self.cellList:
                
                if boardCell.x == pieceCell.x and boardCell.y == pieceCell.y:
                    if boardCell.empty == False:
                        test = False
                    break
            
            if test == False:
                return test
                
        return test
        
    def line_verification_suppression(self):
        """Méthode qui permet de vérifier si une ou plusieurs lignes du plateau sont pleines, et si c'est le cas, les effacent."""
        
        LineCellNumber = 0
        
        cellToTest = [0,0]
        test = 0
        
        for cell in self.cellList:
            
            cellToTest[0] = cell.x
            cellToTest[1] = cell.y
        

            """Vérification de l'attribut "vide" de chaque case sur les lignes horizontales."""
            if cell.x == 0 and cell.y != 0:
            
                while cellToTest[0] < 10:
                    for boardCellToTest in self.cellList:
                    
                        if boardCellToTest.x == cellToTest[0] and boardCellToTest.y == cellToTest[1]:
                            if boardCellToTest.empty == True:
                                test = False
                                break
                            elif boardCellToTest.empty == False:
                                test = True
                            break
                    
                    if test == False:
                        break
                        
                    cellToTest[0] += 1
                    
                cellToTest[0] -= 1
                
                """Suppression de la ligne horizontale si chaque case qui la compose sont pleines (vide == False)."""
                if test == True:
                    while cellToTest[0] >= 0:
                        for cell in self.cellList:
                            if cell.x == cellToTest[0] and cell.y == cellToTest[1]:
                                cell.empty = True
                                cell.texture = pygame.image.load(constantes.boardCellTexture).convert_alpha()
                                
                                LineCellNumber += 1
                                
                                break
                                
                        cellToTest[0] -= 1
            
            

            
            elif cell.y == 0:
                
                while cellToTest[1] < 10:
                    for boardCellToTest in self.cellList:
                    
                        if boardCellToTest.x == cellToTest[0] and boardCellToTest.y == cellToTest[1]:
                            if boardCellToTest.empty == True:
                                test = False
                                break
                            elif boardCellToTest.empty == False:
                                test = True
                                break
                    
                    if test == False:
                        break
                        
                    cellToTest[1] += 1
                    
                cellToTest[1] -= 1
                
                """Suppression de la ligne verticale si chaque case qui la compose sont pleines (vide == False)."""
                if test == True:
                    while cellToTest[1] >= 0:
                        for cell in self.cellList:
                            if cell.x == cellToTest[0] and cell.y == cellToTest[1]:
                                cell.empty = True
                                cell.texture = pygame.image.load(constantes.boardCellTexture).convert_alpha()
                                    
                                LineCellNumber += 1
                                    
                                break
                                
                        cellToTest[1] -= 1
                            
        return LineCellNumber
                            
    def put_down_piece(self, piece):
        """Méthode permettant de poser une pièce dans le plateau (côté développeur):
            - Prend en paramêtre la pièce à poser"""
        
        counter = piece.cellNumber
        
        for boardCell in self.cellList:
        
            """Si toutes les cases ont étaient posées (compteur == 0), alors on arrête de parcourir le plateau inutilement."""
            if counter == 0:
                break
            
            for pieceCell in piece.piece:
                
                if boardCell.x == pieceCell.x and boardCell.y == pieceCell.y:
                
                    """Modification des propriétés des cases du plateau correspondantes aux cases de la pièce.
                    Elles sont maintenant pleines (vide == False) et prennent la texture de la pièce."""
                    boardCell.empty = False
                    boardCell.texture = pieceCell.texture
                    counter -= 1
                    
                    break
