#importations

#pygame importations
import pygame
from pygame.locals import *

#intern python importations
import time
import random

#created files importations
import constants
import functions
import cell_class
import board_class
import piece_class

pygame.init()

#Création de l'écran
screen = pygame.display.set_mode((constants.screenSize[0], constants.screenSize[1]), RESIZABLE)

#Importation des background + Affichage du background
background = pygame.image.load(constants.backgroundTexture).convert_alpha()
screen.blit(background, (0,0))

backgroundGameOver = pygame.image.load(constants.gameOverBackgroundTexture).convert_alpha()

#Police pour le text
font = pygame.font.SysFont("dearsunshine", 64)

#ALEXANDRE: Création du plateau
#EVA: Affichage du plateau
board = board_class.Board()
board.construct()
for cell in board.cellList:
    screen.blit(cell.texture, (cell.x * constants.cellSize, cell.y * constants.cellSize))


#ALEXANDRE: Création des pièces aléatoires
randomCellList = random.choice(constants.pieceList)
piece1 = functions.create_piece(randomCellList)
piece1.def_cell_number()

randomCellList = random.choice(constants.pieceList)
piece2 = functions.create_piece(randomCellList)
piece2.def_cell_number()

randomCellList = random.choice(constants.pieceList)
piece3 = functions.create_piece(randomCellList)
piece3.def_cell_number()

#EVA: Affichage des 3 pièces générées
for cell in piece1.piece:
    screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))
for cell in piece2.piece:
    screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
for cell in piece3.piece:
    screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))

#ALEXANDRE + EVA + ARMAMIS: On sélectionne d'entrée la pièce 1.
piece1.select()

score = 0

#Game music
pygame.mixer.music.load("Sons/Music.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

#Initialisation des sons
winingLineSound = pygame.mixer.Sound("Sons/Ouh_nice_!.wav")
cantPlaceSound = pygame.mixer.Sound("Sons/Nope.wav")
gameOverSound = pygame.mixer.Sound("Sons/Game_over.wav")

#Game over variable initialization
gameOver = False
gameOverText = font.render("Game Over", False, (255, 255, 255))

#EVA : Rafraichissement de l'écran.
pygame.display.flip()

"""EVA : Variable qui va nous permettre de différencier les 2 phases de jeux:
         - Quand phase == 1, on est dans la première phase (sélection)
         - Quand phase == 2, on est dans la seconde phase (placement de la pièce dans le plateau)"""
    
phase = 1

#ALEXANDRE: Variable qui permet de gérer la sortie de la boucle principale du programme, et donc de le fermer.
loop = 1
while loop:
    
    #ALEXANDRE: Evènement de fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
        
        if gameOver == False:

            score_conversion_text = str(score)
            score_text = font.render(score_conversion_text, False, (1,1,1))
    
            if phase == 1:
        
                """ARAMIS : Lorsque l'on est en phase 1, on sélectionne les différentes pièces en appuyant sur flèche bas ou flèche haut,
                            sans oublier de désélectionner la pièce séléctionnée auparavant. On utilise donc les méthodes à voir dans la classe pièce:
                            - "selectPiece"
                            - "unselectPiece"
                ALEXANDRE : Enfin, on sélectionne une pièce uniquement si elle n'est pas déjà placée sur le plateau, si l'attribut "placed" est donc égale à false.
                            Sinon on sélectionne la pièce suivante, si elle aussi n'a pas été posée."""
        
                #Evenèments clavier
                if event.type == KEYDOWN:
                
                    #Flèche bas
                    if event.key == K_DOWN:
                        
                        if piece1.selected == True:
                            piece1.unselect()
                            
                            if piece2.placed == False:
                                piece2.select()
                                
                            elif piece2.placed == True:
                                if piece3.placed == False:
                                    piece3.select()
                                    
                                elif piece3.placed == True:
                                    piece1.select()
                            
                        elif piece2.selected == True:
                            piece2.unselect()
                            
                            if piece3.placed == False:
                                piece3.select()
                                
                            elif piece3.placed == True:
                                if piece1.placed == False:
                                    piece1.select()
                                    
                                elif piece1.placed == True:
                                    piece2.select()
                            
                        elif piece3.selected == True:
                            piece3.unselect()
                            
                            if piece1.placed == False:
                                piece1.select()
                                
                            elif piece1.placed == True:
                                if piece2.placed == False:
                                    piece2.select()
                                    
                                elif piece2.placed == True:
                                    piece3.select()
                                    
                    #Flèche haut
                    if event.key == K_UP:
                    
                        if piece1.selected == True:
                            piece1.unselect()
                        
                            if piece3.placed == False:
                                piece3.select()
                            
                            elif piece3.placed == True:
                                if piece2.placed == False:
                                    piece2.select()
                                
                                elif piece2.placed == True:
                                    piece1.select()
                        
                        elif piece2.selected == True:
                            piece2.unselect()
                        
                            if piece1.placed == False:
                                piece1.select()
                            
                            elif piece1.placed == True:
                                if piece3.placed == False:
                                    piece3.select()
                                
                                elif piece3.placed == True:
                                    piece2.select()
                        
                        elif piece3.selected == True:
                            piece3.unselect()
                        
                            if piece2.placed == False:
                                piece2.select()
                            
                            elif piece2.placed == True:
                                if piece1.placed == False:
                                    piece1.select()
                                
                                elif piece1.placed == True:
                                    piece3.select()
                                
                    """EVA: Une fois la pièce choisie par le joueur, donc sélectionée, s'il appuie sur "Entrée" voici ce qu'il se passe:
                            - La pièce qu'il a sélectionné se place en haut à gauche du plateau (0,0) et reste sélectionée,
                            - Les autres pièces gardent les mêmes caractéristiques et gardent la même position (selected = false...),
                            - On passe dans la seconde phase de jeu (phase = 2)."""
                            
                                
                    #Entrée
                    if event.key == K_c:
                    
                        if piece1.selected == True:
                            for cell in piece1.piece:
                                cell.x = 0 + cell.x
                                cell.y = 0 + cell.y
                        
                        elif piece2.selected == True:
                            for cell in piece1.piece:
                                cell.x = 0 + cell.x
                                cell.y = 0 + cell.y
                    
                        elif piece3.selected == True:
                            for cell in piece1.piece:
                                cell.x = 0 + cell.x
                                cell.y = 0 + cell.y
                            
                        phase = 2
                
            if phase == 2:
        
                """En phase 2 :
                - ARAMIS : Les flèches directionnels permettent de déplacer la pièce dans le plateau avec "moove".
                           On test à chaque déplacement si la pièce est en dehors du plateau, et si c'est le cas, on la remet à sa position précédente avec "testBordure". 
            
                - ALEXANDRE : Quand l'utilisateur appuie sur "Entrée", on test si la place est libre avec "PlayerPlaceVerification" de la classe Plateau.
                        Si la place est libre, on appelle la méthode "placePiece"
                        Lorsqu'une pièce a été posée ou que des nouvelles pièces se génèrent, on test s'il y a encore de la place, sinon game over.
                    
                - EVA : Quand la pièce a été posée on repasse en phase 1,
                        puis on sélectionne les pièces manquantes ou si toute les pièces ont été placées, on en génère des nouvelles."""
        
                #Evenèments clavier
                if event.type == KEYDOWN:
                
                    #Flèche bas
                    if event.key == K_DOWN:
                
                        if piece1.selected == True:
                            piece1.moove("bas")
                            piece1.testBordure(piece1)
                
                        elif piece2.selected == True:
                            piece2.moove("bas")
                            piece2.testBordure(piece2)
                   
                        elif piece3.selected == True:
                            piece3.moove("bas")
                            piece3.testBordure(piece3)
                
                    #Flèche haut
                    if event.key == K_UP:
                
                        if piece1.selected == True:
                            piece1.moove("haut")
                            piece1.testBordure(piece1)
                    
                        elif piece2.selected == True:
                            piece2.moove("haut")
                            piece2.testBordure(piece2)
                   
                        elif piece3.selected == True:
                            piece3.moove("haut")
                            piece3.testBordure(piece3)
                    
                    #Flèche droite
                    if event.key == K_RIGHT:
                
                        if piece1.selected == True:
                            piece1.moove("droite")
                            piece1.testBordure(piece1)
                    
                        elif piece2.selected == True:
                            piece2.moove("droite")
                            piece2.testBordure(piece2)
                   
                        elif piece3.selected == True:
                            piece3.moove("droite")
                            piece3.testBordure(piece3)
           
                    #Flèche gauche
                    if event.key == K_LEFT:
                
                        if piece1.selected == True:
                            piece1.moove("gauche")
                            piece1.testBordure(piece1)
                    
                        elif piece2.selected == True:
                            piece2.moove("gauche")
                            piece2.testBordure(piece2)
                   
                        elif piece3.selected == True:
                            piece3.moove("gauche")
                            piece3.testBordure(piece3)
            
            
                    #Entrée
                    if event.key == K_RETURN:
                    
                        if piece1.selected == True:
                            canBePlaced = board.player_place_verification(piece1)
                            if canBePlaced:
                                piece1.place_piece(board, piece1)
                                score += piece1.cellNumber
                            elif canBePlaced == False:
                            
                                for cell in piece1.piece:
                                    cell.texture = cell.cantPlaceTexture
                            
                                piece1.canBePlaced = False
                                cantPlaceSound.play()
                            
                        elif piece2.selected == True:
                            canBePlaced = board.player_place_verification(piece2)
                            if canBePlaced:
                                piece2.place_piece(board, piece2)
                                score += piece2.cellNumber
                            elif canBePlaced == False:
                        
                                for cell in piece2.piece:
                                    cell.texture = cell.cantPlaceTexture
                                
                                piece2.canBePlaced = False
                                cantPlaceSound.play()
                            
                        elif piece3.selected == True:
                            canBePlaced = board.player_place_verification(piece3)
                            if canBePlaced:
                                piece3.place_piece(board, piece3)
                                score += piece3.cellNumber
                            elif canBePlaced == False:
                            
                                for cell in piece3.piece:
                                    cell.texture = cell.cantPlaceTexture
                                
                                piece3.canBePlaced = False
                                cantPlaceSound.play()
                                        
                        if canBePlaced == True: #la piece a été placée on peut repasser en phase 1, celle de sélection.
                    
                            lineCellNumber = board.line_verification_suppression()
                        
                            if lineCellNumber > 0:
                                score += lineCellNumber
                                winingLineSound.play()
                        
                            testList = []
                            test = True
                            
                            if piece1.placed == False:
                            
                                testList.append(board.place_verification(piece1))
                                if piece2.placed == False:
                                    testList.append(board.place_verification(piece2))
                                if piece3.placed == False:
                                    testList.append(board.place_verification(piece3))
                            
                                piece1.select()
                                
                            elif piece1.placed == True:
                                if piece2.placed == False:
                            
                                    testList.append(board.place_verification(piece2))
                                    if piece3.placed == False:
                                        testList.append(board.place_verification(piece3))
                                
                                    piece2.select()
                                    
                                elif piece2.placed == True:
                                    if piece3.placed == False:
                                
                                        testList.append(board.place_verification(piece3))
                                    
                                        piece3.select()
                                        
                                    elif piece3.placed == True:
                                
                                        #Si les 3 pièces sont placées, on en génère trois nouvelles et on vérifie si elles sont posables.
                                    
                                        randomCellList = random.choice(constants.pieceList)
                                        piece1 = functions.create_piece(randomCellList)
                                        piece1.def_cell_number()

                                        randomCellList = random.choice(constants.pieceList)
                                        piece2 = functions.create_piece(randomCellList)
                                        piece2.def_cell_number()

                                        randomCellList = random.choice(constants.pieceList)
                                        piece3 = functions.create_piece(randomCellList)
                                        piece3.def_cell_number()
                                    
                                        testList.append(board.place_verification(piece1))
                                        testList.append(board.place_verification(piece2))
                                        testList.append(board.place_verification(piece3))
                                    
                                        piece1.select()
                        
                            for currentTest in testList:
                                if currentTest == True:
                                    test = True
                                    break
                                elif currentTest == False:
                                    test = False
                                
                            if test == False:
                                gameOver = True
                                functions.game_over(gameOver, gameOverSound)

                            phase = 1
            
        """EVA: Affichage des éléments(textures) du jeu puis actualisation de l'écran à chaque tour de boucle."""
    
        #D'abord le background
        screen.blit(background, (0,0))
    
        #Puis le plateau
        for cell in board.cellList:
            screen.blit(cell.texture, (cell.x * constants.cellSize, cell.y * constants.cellSize))
    
        #Si on est en phase 1, on affiche les pièces à partir de la droite du plateau (xChoixPiece & yChoixPiece)
        if phase == 1:
            for cell in piece1.piece:
                screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))
            for cell in piece2.piece:
                screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
            for cell in piece3.piece:
                screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))
    
        #Si on est en phase 2, on affiche la pièce sélectionnée à partir du (0,0), en haut à gauche du plateau, et les autres à droite.
        if phase == 2:
        
            if piece1.selected == True:
        
                if piece1.canBePlaced == False:
                    for cell in piece1.piece:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
                    
                    for cell in piece2.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
                    for cell in piece3.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))    
                    
                    pygame.display.flip()
                    time.sleep(0.6)
                
                    for cell in piece1.piece:
                        cell.texture = cell.selectedTexture
                        piece1.canBePlaced = True
                
                else:
                    for cell in piece1.piece:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
                
                    for cell in piece2.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
                    for cell in piece3.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))
                    
            elif piece2.selected == True:
        
                if piece2.canBePlaced == False:
                    for cell in piece2.piece:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
                    
                    for cell in piece1.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))
                    for cell in piece3.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))    
                    
                    pygame.display.flip()
                    time.sleep(0.6)
                
                    for cell in piece2.piece:
                        cell.texture = cell.selectedTexture
                        piece2.canBePlaced = True
                    
                else:
                    for cell in piece2.piece:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
                
                    for cell in piece1.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))
                    for cell in piece3.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))
                
            elif piece3.selected == True:
        
                if piece3.canBePlaced == False:
                    for cell in piece3.piece:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
                    
                    for cell in piece2.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
                    for cell in piece1.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))
                    
                    pygame.display.flip()
                    time.sleep(0.6)
                
                    for cell in piece3.piece:
                        cell.texture = cell.selectedTexture
                        piece3.canBePlaced = True
                    
                else:
                    for cell in piece3.piece:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
            
                    for cell in piece2.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
                    for cell in piece1.piece:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))


        #EVA: Affichage d'un nouvel écran lors d'un game over.
        if gameOver == True:
            screen.blit(backgroundGameOver,(0,0))
            screen.blit(gameOverText, (6*constants.cellSize, 7*constants.cellSize))
    
        pygame.display.flip()

        #EVA: Affichage du score constantes
        screen.blit(score_text, (1*constants.cellSize, 15*constants.cellSize))
