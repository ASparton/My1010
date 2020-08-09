import pygame
from pygame.locals import *

import constantes
import c_Case

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
class Plateau:
        
    def __init__(self, x=10, y=10):
        
        self.taille_x = x
        self.taille_y = y
        self.listeCase = []
        
        """taille_x = nombre de case en longueur du plateau"""
        """taille_y = nombre de case en largeur du plateau"""
        """listeCase = liste des cases qui composent le plateau (Longueur*Largeur)"""
           
    def Construct(self):
        """Méthode de construction du plateau"""
        
        compteur_x = 0
        compteur_y = 0
        
        while(compteur_y < self.taille_y):
            while(compteur_x < self.taille_x):
                self.listeCase.append(c_Case.Case(compteur_x, compteur_y))
                compteur_x += 1
            
            compteur_y += 1
            compteur_x = 0
            
    def PlaceVerification(self, piece):
        """Méthode pour vérifier si une pièce est posable sur le plateau: 
           - Prend en paramêtre la pièce que l'on veut tester
           - Renvoie le booléen "test", pour dire si oui ou non la pièce est posable sur le plateau."""
        
        test = False
        testEnCours = False
        caseATester = [0,0]
        
        xmaxTest = 10 - piece.NbCasex
        ymaxTest = 10 - piece.NbCasey
        
        for casePlateau in self.listeCase:
            
            if casePlateau.x < xmaxTest and casePlateau.y < ymaxTest:            
            
                for casePiece in piece.piece:
                
                    caseATester[0] = casePlateau.x + casePiece.x
                    caseATester[1] = casePlateau.y + casePiece.y
                    
                    for casePlateauTest in self.listeCase:
                        if casePlateauTest.x == caseATester[0] and casePlateauTest.y == caseATester[1]:
                            if casePlateauTest.vide == False:
                                testEnCours = False
                                break
                            elif casePlateauTest.vide == True:
                                testEnCours = True
                                break
                                
                    if testEnCours == False:
                        break
                        
                if testEnCours == True:
                    test = True
                    break
                    
                elif testEnCours == False:
                    test = False
        
        return test
        
    def PlayerPlaceVerification(self, piece):
        """Méthode pour vérifier si là où le joueur décide de poser sa pièce est bien libre:
           - Prend en paramêtre la pièce que le joueur veut essayer de poser
           - Retourn le booléen "test" pour dire si oui ou non la pièce est posable là où l'utilisateur veut la poser."""
        
        test = True
        
        for casePiece in piece.piece:
            for casePlateau in self.listeCase:
                
                if casePlateau.x == casePiece.x and casePlateau.y == casePiece.y:
                    if casePlateau.vide == False:
                        test = False
                    break
            
            if test == False:
                return test
                
        return test
        
    def LineVerificationSuppression(self):
        """Méthode qui permet de vérifier si une ou plusieurs lignes du plateau sont pleines, et si c'est le cas, les effacent."""
        
        NbCaseLine = 0
        
        caseATester = [0,0]
        test = 0
        
        for case in self.listeCase:
            
            caseATester[0] = case.x
            caseATester[1] = case.y
        

            """Vérification de l'attribut "vide" de chaque case sur les lignes horizontales."""
            if case.x == 0 and case.y != 0:
            
                while caseATester[0] < 10:
                    for casePlateauTest in self.listeCase:
                    
                        if casePlateauTest.x == caseATester[0] and casePlateauTest.y == caseATester[1]:
                            if casePlateauTest.vide == True:
                                test = False
                                break
                            elif casePlateauTest.vide == False:
                                test = True
                            break
                    
                    if test == False:
                        break
                        
                    caseATester[0] += 1
                    
                caseATester[0] -= 1
                
                """Suppression de la ligne horizontale si chaque case qui la compose sont pleines (vide == False)."""
                if test == True:
                    while caseATester[0] >= 0:
                        for case in self.listeCase:
                            if case.x == caseATester[0] and case.y == caseATester[1]:
                                case.vide = True
                                case.texture = pygame.image.load(constantes._CasePlateau).convert_alpha()
                                
                                NbCaseLine += 1
                                
                                break
                                
                        caseATester[0] -= 1
            
            

            
            elif case.y == 0:
                
                while caseATester[1] < 10:
                    for casePlateauTest in self.listeCase:
                    
                        if casePlateauTest.x == caseATester[0] and casePlateauTest.y == caseATester[1]:
                            if casePlateauTest.vide == True:
                                test = False
                                break
                            elif casePlateauTest.vide == False:
                                test = True
                                break
                    
                    if test == False:
                        break
                        
                    caseATester[1] += 1
                    
                caseATester[1] -= 1
                
                """Suppression de la ligne verticale si chaque case qui la compose sont pleines (vide == False)."""
                if test == True:
                    while caseATester[1] >= 0:
                        for case in self.listeCase:
                            if case.x == caseATester[0] and case.y == caseATester[1]:
                                case.vide = True
                                case.texture = pygame.image.load(constantes._CasePlateau).convert_alpha()
                                    
                                NbCaseLine += 1
                                    
                                break
                                
                        caseATester[1] -= 1
                            
        return NbCaseLine
                            
    def PutDownPiece(self, piece):
        """Méthode permettant de poser une pièce dans le plateau (côté développeur):
            - Prend en paramêtre la pièce à poser"""
        
        compteur = piece.NbCase
        
        for casePlateau in self.listeCase:
        
            """Si toutes les cases ont étaient posées (compteur == 0), alors on arrête de parcourir le plateau inutilement."""
            if compteur == 0:
                break
            
            for casePiece in piece.piece:
                
                if casePlateau.x == casePiece.x and casePlateau.y == casePiece.y:
                
                    """Modification des propriétés des cases du plateau correspondantes aux cases de la pièce.
                    Elles sont maintenant pleines (vide == False) et prennent la texture de la pièce."""
                    casePlateau.vide = False
                    casePlateau.texture = casePiece.texture
                    compteur -= 1
                    
                    break
