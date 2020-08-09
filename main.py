#importations

#pygame importations
import pygame
from pygame.locals import *

#intern python importations
import time
import random

#created files importations
import constantes
import fonctions
import c_Case
import c_Plateau
import c_Piece

pygame.init()

#ALEXANDRE: Création de l'écran
screen = pygame.display.set_mode((constantes.tailleScreen[0], constantes.tailleScreen[1]), RESIZABLE)

#ALEXANDRE: Importation des background
#EVA: Affichage du background
background = pygame.image.load(constantes._Background).convert_alpha()
screen.blit(background, (0,0))

backgroundGameOver = pygame.image.load(constantes._Background_game_over).convert_alpha()

#ALEXANDRE: Création du plateau
#EVA: Affichage du plateau
plateau = c_Plateau.Plateau()
plateau.Construct()
for case in plateau.listeCase:
    screen.blit(case.texture, (case.x * constantes.tailleCase, case.y * constantes.tailleCase))


#ALEXANDRE: Création des pièces aléatoires
randomListeCase = random.choice(constantes.listePiece)
Piece1 = fonctions.create_piece(randomListeCase)
Piece1.defNbCase()

randomListeCase = random.choice(constantes.listePiece)
Piece2 = fonctions.create_piece(randomListeCase)
Piece2.defNbCase()

randomListeCase = random.choice(constantes.listePiece)
Piece3 = fonctions.create_piece(randomListeCase)
Piece3.defNbCase()

#EVA: Affichage des 3 pièces générées
for case in Piece1.piece:
    screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece1 + case.y) * constantes.tailleCase)))
for case in Piece2.piece:
    screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece2 + case.y) * constantes.tailleCase)))
for case in Piece3.piece:
    screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece3 + case.y) * constantes.tailleCase)))

#ALEXANDRE + EVA + ARMAMIS: On sélectionne d'entrée la pièce 1.
Piece1.selectPiece()

score = 0

#Game music
pygame.mixer.music.load("Sons/Music.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

#Initialisation des sons
winingLineSound = pygame.mixer.Sound("Sons/Ouh_nice_!.wav")
unplacableSound = pygame.mixer.Sound("Sons/Nope.wav")
gameOverSound = pygame.mixer.Sound("Sons/Game_over.wav")

#Game over variable initialization
gameOver = False
gameOverText = constantes.font.render("Game Over", False, (255, 255, 255))

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
            score_text = constantes.font.render(score_conversion_text, False, (0,0,0))
    
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
                        
                        if Piece1.selected == True:
                            Piece1.unselectPiece()
                            
                            if Piece2.placed == False:
                                Piece2.selectPiece()
                                
                            elif Piece2.placed == True:
                                if Piece3.placed == False:
                                    Piece3.selectPiece()
                                    
                                elif Piece3.placed == True:
                                    Piece1.selectPiece()
                            
                        elif Piece2.selected == True:
                            Piece2.unselectPiece()
                            
                            if Piece3.placed == False:
                                Piece3.selectPiece()
                                
                            elif Piece3.placed == True:
                                if Piece1.placed == False:
                                    Piece1.selectPiece()
                                    
                                elif Piece1.placed == True:
                                    Piece2.selectPiece()
                            
                        elif Piece3.selected == True:
                            Piece3.unselectPiece()
                            
                            if Piece1.placed == False:
                                Piece1.selectPiece()
                                
                            elif Piece1.placed == True:
                                if Piece2.placed == False:
                                    Piece2.selectPiece()
                                    
                                elif Piece2.placed == True:
                                    Piece3.selectPiece()
                                    
                    #Flèche haut
                    if event.key == K_UP:
                    
                        if Piece1.selected == True:
                            Piece1.unselectPiece()
                        
                            if Piece3.placed == False:
                                Piece3.selectPiece()
                            
                            elif Piece3.placed == True:
                                if Piece2.placed == False:
                                    Piece2.selectPiece()
                                
                                elif Piece2.placed == True:
                                    Piece1.selectPiece()
                        
                        elif Piece2.selected == True:
                            Piece2.unselectPiece()
                        
                            if Piece1.placed == False:
                                Piece1.selectPiece()
                            
                            elif Piece1.placed == True:
                                if Piece3.placed == False:
                                    Piece3.selectPiece()
                                
                                elif Piece3.placed == True:
                                    Piece2.selectPiece()
                        
                        elif Piece3.selected == True:
                            Piece3.unselectPiece()
                        
                            if Piece2.placed == False:
                                Piece2.selectPiece()
                            
                            elif Piece2.placed == True:
                                if Piece1.placed == False:
                                    Piece1.selectPiece()
                                
                                elif Piece1.placed == True:
                                    Piece3.selectPiece()
                                
                    """EVA: Une fois la pièce choisie par le joueur, donc sélectionée, s'il appuie sur "Entrée" voici ce qu'il se passe:
                            - La pièce qu'il a sélectionné se place en haut à gauche du plateau (0,0) et reste sélectionée,
                            - Les autres pièces gardent les mêmes caractéristiques et gardent la même position (selected = false...),
                            - On passe dans la seconde phase de jeu (phase = 2)."""
                            
                                
                    #Entrée
                    if event.key == K_c:
                    
                        if Piece1.selected == True:
                            for case in Piece1.piece:
                                case.x = 0 + case.x
                                case.y = 0 + case.y
                        
                        elif Piece2.selected == True:
                            for case in Piece1.piece:
                                case.x = 0 + case.x
                                case.y = 0 + case.y
                    
                        elif Piece3.selected == True:
                            for case in Piece1.piece:
                                case.x = 0 + case.x
                                case.y = 0 + case.y
                            
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
                
                        if Piece1.selected == True:
                            Piece1.moove("bas")
                            Piece1.testBordure(Piece1)
                
                        elif Piece2.selected == True:
                            Piece2.moove("bas")
                            Piece2.testBordure(Piece2)
                   
                        elif Piece3.selected == True:
                            Piece3.moove("bas")
                            Piece3.testBordure(Piece3)
                
                    #Flèche haut
                    if event.key == K_UP:
                
                        if Piece1.selected == True:
                            Piece1.moove("haut")
                            Piece1.testBordure(Piece1)
                    
                        elif Piece2.selected == True:
                            Piece2.moove("haut")
                            Piece2.testBordure(Piece2)
                   
                        elif Piece3.selected == True:
                            Piece3.moove("haut")
                            Piece3.testBordure(Piece3)
                    
                    #Flèche droite
                    if event.key == K_RIGHT:
                
                        if Piece1.selected == True:
                            Piece1.moove("droite")
                            Piece1.testBordure(Piece1)
                    
                        elif Piece2.selected == True:
                            Piece2.moove("droite")
                            Piece2.testBordure(Piece2)
                   
                        elif Piece3.selected == True:
                            Piece3.moove("droite")
                            Piece3.testBordure(Piece3)
           
                    #Flèche gauche
                    if event.key == K_LEFT:
                
                        if Piece1.selected == True:
                            Piece1.moove("gauche")
                            Piece1.testBordure(Piece1)
                    
                        elif Piece2.selected == True:
                            Piece2.moove("gauche")
                            Piece2.testBordure(Piece2)
                   
                        elif Piece3.selected == True:
                            Piece3.moove("gauche")
                            Piece3.testBordure(Piece3)
            
            
                    #Entrée
                    if event.key == K_RETURN:
                    
                        if Piece1.selected == True:
                            okay = plateau.PlayerPlaceVerification(Piece1)
                            if okay:
                                Piece1.placePiece(plateau, Piece1)
                                score += Piece1.NbCase
                            elif okay == False:
                            
                                for case in Piece1.piece:
                                    case.texture = case.texture_not
                            
                                Piece1.placable = False
                                unplacableSound.play()
                            
                        elif Piece2.selected == True:
                            okay = plateau.PlayerPlaceVerification(Piece2)
                            if okay:
                                Piece2.placePiece(plateau, Piece2)
                                score += Piece2.NbCase
                            elif okay == False:
                        
                                for case in Piece2.piece:
                                    case.texture = case.texture_not
                                
                                Piece2.placable = False
                                unplacableSound.play()
                            
                        elif Piece3.selected == True:
                            okay = plateau.PlayerPlaceVerification(Piece3)
                            if okay:
                                Piece3.placePiece(plateau, Piece3)
                                score += Piece3.NbCase
                            elif okay == False:
                            
                                for case in Piece3.piece:
                                    case.texture = case.texture_not
                                
                                Piece3.placable = False
                                unplacableSound.play()
                                        
                        if okay == True: #la piece a été placée on peut repasser en phase 1, celle de sélection.
                    
                            NbCaseLine = plateau.LineVerificationSuppression()
                        
                            if NbCaseLine > 0:
                                score += NbCaseLine
                                winingLineSound.play()
                        
                            testListe = []
                            test = True
                            
                            if Piece1.placed == False:
                            
                                testListe.append(plateau.PlaceVerification(Piece1))
                                if Piece2.placed == False:
                                    testListe.append(plateau.PlaceVerification(Piece2))
                                if Piece3.placed == False:
                                    testListe.append(plateau.PlaceVerification(Piece3))
                            
                                Piece1.selectPiece()
                                
                            elif Piece1.placed == True:
                                if Piece2.placed == False:
                            
                                    testListe.append(plateau.PlaceVerification(Piece2))
                                    if Piece3.placed == False:
                                        testListe.append(plateau.PlaceVerification(Piece3))
                                
                                    Piece2.selectPiece()
                                    
                                elif Piece2.placed == True:
                                    if Piece3.placed == False:
                                
                                        testListe.append(plateau.PlaceVerification(Piece3))
                                    
                                        Piece3.selectPiece()
                                        
                                    elif Piece3.placed == True:
                                
                                        #Si les 3 pièces sont placées, on en génère trois nouvelles et on vérifie si elles sont posables.
                                    
                                        randomListeCase = random.choice(constantes.listePiece)
                                        Piece1 = fonctions.create_piece(randomListeCase)
                                        Piece1.defNbCase()

                                        randomListeCase = random.choice(constantes.listePiece)
                                        Piece2 = fonctions.create_piece(randomListeCase)
                                        Piece2.defNbCase()

                                        randomListeCase = random.choice(constantes.listePiece)
                                        Piece3 = fonctions.create_piece(randomListeCase)
                                        Piece3.defNbCase()
                                    
                                        testListe.append(plateau.PlaceVerification(Piece1))
                                        testListe.append(plateau.PlaceVerification(Piece2))
                                        testListe.append(plateau.PlaceVerification(Piece3))
                                    
                                        Piece1.selectPiece()
                        
                            for testEnCours in testListe:
                                if testEnCours == True:
                                    test = True
                                    break
                                elif testEnCours == False:
                                    test = False
                                
                            if test == False:
                                gameOver = True
                                fonctions.game_over(gameOver, gameOverSound)

                            phase = 1
            
        """EVA: Affichage des éléments(textures) du jeu puis actualisation de l'écran à chaque tour de boucle."""
    
        #D'abord le background
        screen.blit(background, (0,0))
    
        #Puis le plateau
        for case in plateau.listeCase:
            screen.blit(case.texture, (case.x * constantes.tailleCase, case.y * constantes.tailleCase))
    
        #Si on est en phase 1, on affiche les pièces à partir de la droite du plateau (xChoixPiece & yChoixPiece)
        if phase == 1:
            for case in Piece1.piece:
                screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece1 + case.y) * constantes.tailleCase)))
            for case in Piece2.piece:
                screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece2 + case.y) * constantes.tailleCase)))
            for case in Piece3.piece:
                screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece3 + case.y) * constantes.tailleCase)))
    
        #Si on est en phase 2, on affiche la pièce sélectionnée à partir du (0,0), en haut à gauche du plateau, et les autres à droite.
        if phase == 2:
        
            if Piece1.selected == True:
        
                if Piece1.placable == False:
                    for case in Piece1.piece:
                        screen.blit(case.texture, (((0 + case.x) * constantes.tailleCase), ((0 + case.y) * constantes.tailleCase)))
                    
                    for case in Piece2.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece2 + case.y) * constantes.tailleCase)))
                    for case in Piece3.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece3 + case.y) * constantes.tailleCase)))    
                    
                    pygame.display.flip()
                    time.sleep(0.6)
                
                    for case in Piece1.piece:
                        case.texture = case.texture_selected
                        Piece1.placable = True
                
                else:
                    for case in Piece1.piece:
                        screen.blit(case.texture, (((0 + case.x) * constantes.tailleCase), ((0 + case.y) * constantes.tailleCase)))
                
                    for case in Piece2.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece2 + case.y) * constantes.tailleCase)))
                    for case in Piece3.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece3 + case.y) * constantes.tailleCase)))
                    
            elif Piece2.selected == True:
        
                if Piece2.placable == False:
                    for case in Piece2.piece:
                        screen.blit(case.texture, (((0 + case.x) * constantes.tailleCase), ((0 + case.y) * constantes.tailleCase)))
                    
                    for case in Piece1.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece1 + case.y) * constantes.tailleCase)))
                    for case in Piece3.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece3 + case.y) * constantes.tailleCase)))    
                    
                    pygame.display.flip()
                    time.sleep(0.6)
                
                    for case in Piece2.piece:
                        case.texture = case.texture_selected
                        Piece2.placable = True
                    
                else:
                    for case in Piece2.piece:
                        screen.blit(case.texture, (((0 + case.x) * constantes.tailleCase), ((0 + case.y) * constantes.tailleCase)))
                
                    for case in Piece1.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece1 + case.y) * constantes.tailleCase)))
                    for case in Piece3.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece3 + case.y) * constantes.tailleCase)))
                
            elif Piece3.selected == True:
        
                if Piece3.placable == False:
                    for case in Piece3.piece:
                        screen.blit(case.texture, (((0 + case.x) * constantes.tailleCase), ((0 + case.y) * constantes.tailleCase)))
                    
                    for case in Piece2.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece2 + case.y) * constantes.tailleCase)))
                    for case in Piece1.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece1 + case.y) * constantes.tailleCase)))
                    
                    pygame.display.flip()
                    time.sleep(0.6)
                
                    for case in Piece3.piece:
                        case.texture = case.texture_selected
                        Piece3.placable = True
                    
                else:
                    for case in Piece3.piece:
                        screen.blit(case.texture, (((0 + case.x) * constantes.tailleCase), ((0 + case.y) * constantes.tailleCase)))
            
                    for case in Piece2.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece2 + case.y) * constantes.tailleCase)))
                    for case in Piece1.piece:
                        screen.blit(case.texture, (((constantes.xChoixPiece + case.x) * constantes.tailleCase), ((constantes.yChoixPiece1 + case.y) * constantes.tailleCase)))


        #EVA: Affichage d'un nouvel écran lors d'un game over.
        if gameOver == True:
            screen.blit(backgroundGameOver,(0,0))
            screen.blit(gameOverText, (6*constantes.tailleCase, 7*constantes.tailleCase))
    
        pygame.display.flip()

        #EVA: Affichage du score constantes
        screen.blit(score_text, (1*constantes.tailleCase, 15*constantes.tailleCase))
