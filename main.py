import pygame
from pygame.locals import *

import time

import constants
import functions
import cell_class
import board_class
import piece_class
import button_class

pygame.init()

"""Initialization of all we need before starting the game."""

#Screen creations
screen = pygame.display.set_mode((constants.SCREENSIZE[0], constants.SCREENSIZE[1]), RESIZABLE)
pygame.display.set_caption("Retro 1010!")

#Background importation + display
background = pygame.image.load(constants.BACKGROUNDTEXTURE).convert_alpha()
screen.blit(background, (0,0))
#Game over background importation
backgroundGameOver = pygame.image.load(constants.GAMEOVERBACKGROUNDTEXTURE).convert_alpha()

#Font creation
font = pygame.font.Font("assets/pixel_font.ttf", 40)

#Game music
pygame.mixer.music.load("assets/sounds/The Grand Affair.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

#Game sound initialization
winingLineSound = pygame.mixer.Sound("assets/sounds/Ouh_nice_!.wav")
cantPlaceSound = pygame.mixer.Sound("assets/sounds/Nope.wav")
gameOverSound = pygame.mixer.Sound("assets/sounds/Game_over.wav")

#Game over variable initialization
gameOver = False
gameOverText = font.render("Game Over", False, (255, 255, 255))

#Menu initialization
title = pygame.image.load(constants.TITLETEXTURE).convert_alpha()
#Buttons creation
playButton = button_class.Button("play", constants.SCREENSIZE[0]/2-96, 200, constants.PLAYBUTTONTEXTURE, constants.PLAYBUTTONSELECTEDTEXTURE, True)
mainMenuExitButton = button_class.Button("exit", constants.SCREENSIZE[0]/2-96, 400, constants.EXITBUTTONTEXTURE, constants.exitButtonSelectedTexture)

"""Variable that cut the two phase of the game:
         - When phase == 1, we are in the first phase, the selection of the piece
         - When phase == 2, we are in the second phase, the player put down the piece on the board
         - When phase == 3, we are in game over, the player can watch the scores, then exit or go to the main menu"""
phase = 0

#Load the screen
pygame.display.flip()

#game loop setup
clock = pygame.time.Clock()
runGame = True

while runGame:
     #Set the max FPS of the game to "constants.FPS" (60), so we have the same loop time on every system
    clock.tick(constants.FPS)

    while (phase == 0):
        clock.tick(constants.FPS)

        """Main menu"""
        if not runGame: #If the player exit the game. Break the while loop to end up the program
            break

        for event in pygame.event.get(): #Exit event
            if event.type == QUIT:
                runGame = False

            if event.type == KEYDOWN:
                if event.key == K_DOWN: #Select the next button
                    if playButton.selected:
                        playButton.selected = False
                        mainMenuExitButton.selected = True
                    elif mainMenuExitButton.selected:
                        mainMenuExitButton.selected = False
                        playButton.selected = True

                if event.key == K_UP:   #Select the next button
                    if playButton.selected:
                        playButton.selected = False
                        mainMenuExitButton.selected = True
                    elif mainMenuExitButton.selected:
                        mainMenuExitButton.selected = False
                        playButton.selected = True

                if event.key == K_RETURN:   #Call the function of the selected button
                    if playButton.selected:
                        phase = playButton.do_function()
                        if phase == 1:  #Creation of the game elements
                            #Board creation
                            board = board_class.Board()
                            board.build()
                            #Pieces generation
                            piece1, piece2, piece3 = functions.generate_pieces()
                            #Pointer (list) of the piece the player is going to choose
                            chosenPiece = piece1    #For now it points on piece1
                            #We select the first piece. Then the player will choose from that start
                            piece1[0].selected = True
                            #Set the score at the beginning
                            score = 0
                            bestScore = functions.get_best_score()

                    elif mainMenuExitButton.selected:
                        runGame = mainMenuExitButton.do_function()

        """Display of the main menu's elements"""
        screen.blit(background, (0,0))
        screen.blit(title, ((constants.SCREENSIZE[0]/2-160), 0))
        screen.blit(playButton.texture, (playButton.x, playButton.y))
        screen.blit(mainMenuExitButton.texture, (mainMenuExitButton.x, mainMenuExitButton.y))

        pygame.display.flip()

    while (phase == 1 or phase == 2):
        clock.tick(constants.FPS)

        if not runGame: #If the player exit the game. Break the while loop to end up the program
            break
        
        #We wait for game event and update the score
        strScore = "SCORE: " + str(score)
        scoreText = font.render(strScore, False, (10,10,10))
        strBestScore = "BEST SCORE: " + bestScore
        bestScoreText = font.render(strBestScore, False, (10,10,10))

        for event in pygame.event.get(): #Exit event
            if event.type == QUIT:
                runGame = False
    
            if phase == 1:
                """When we are in phase 1, the player need to choose a piece with the directional keys,
                and need to press "c" to choose the one he wants. That's the events we are wainting for"""
                if event.type == KEYDOWN:
                
                    if event.key == K_DOWN:
                        
                        if piece1[0].selected == True:
                            piece1[0].selected = False
                            
                            if piece2[0].placed == False:
                                piece2[0].selected = True
                                chosenPiece = piece2
                                
                            elif piece2[0].placed == True:
                                if piece3[0].placed == False:
                                    piece3[0].selected = True
                                    chosenPiece = piece3
                                    
                                elif piece3[0].placed == True:
                                    piece1[0].selected = True
                                    chosenPiece = piece1
                            
                        elif piece2[0].selected == True:
                            piece2[0].selected = False
                            
                            if piece3[0].placed == False:
                                piece3[0].selected = True
                                chosenPiece = piece3
                                
                            elif piece3[0].placed == True:
                                if piece1[0].placed == False:
                                    piece1[0].selected = True
                                    chosenPiece = piece1
                                    
                                elif piece1[0].placed == True:
                                    piece2[0].selected = True
                                    chosenPiece = piece2
                            
                        elif piece3[0].selected == True:
                            piece3[0].selected = False
                            
                            if piece1[0].placed == False:
                                piece1[0].selected = True
                                chosenPiece = piece1
                                
                            elif piece1[0].placed == True:
                                if piece2[0].placed == False:
                                    piece2[0].selected = True
                                    chosenPiece = piece2
                                    
                                elif piece2[0].placed == True:
                                    piece3[0].selected = True
                                    chosenPiece = piece3
                                
                    if event.key == K_UP:
                    
                        if piece1[0].selected == True:
                            piece1[0].selected = False
                        
                            if piece3[0].placed == False:
                                piece3[0].selected = True
                                chosenPiece = piece3
                            
                            elif piece3[0].placed == True:
                                if piece2[0].placed == False:
                                    piece2[0].selected = True
                                    chosenPiece = piece2
                                
                                elif piece2[0].placed == True:
                                    piece1[0].selected = True
                                    chosenPiece = piece1
                        
                        elif piece2[0].selected == True:
                            piece2[0].selected = False
                        
                            if piece1[0].placed == False:
                                piece1[0].selected = True
                                chosenPiece = piece1
                            
                            elif piece1[0].placed == True:
                                if piece3[0].placed == False:
                                    piece3[0].selected = True
                                    chosenPiece = piece3
                                
                                elif piece3[0].placed == True:
                                    piece2[0].selected = True
                                    chosenPiece = piece2
                        
                        elif piece3[0].selected == True:
                            piece3[0].selected = False
                        
                            if piece2[0].placed == False:
                                piece2[0].selected = True
                                chosenPiece = piece2
                            
                            elif piece2[0].placed == True:
                                if piece1[0].placed == False:
                                    piece1[0].selected = True
                                    chosenPiece = piece1
                                
                                elif piece1[0].placed == True:
                                    piece3[0].selected = True
                                    chosenPiece = piece3
 
                    if event.key == K_c:

                        for cell in chosenPiece[0].cellsList:
                            cell.x = 0 + cell.x
                            cell.y = 0 + cell.y
                            
                        phase = 2
                
            if phase == 2:
                """During phase 2 :
                - We wait for the player to moove the piece on the board with the directional keys.
                - Then we wait for him to put down the piece on the board with enter.
                - Then we check for a possible game over, generate other pieces if there is no more and return to phase 1"""
                if event.type == KEYDOWN:
                
                    if event.key == K_DOWN:
                        chosenPiece[0].moove("down")
                
                    if event.key == K_UP:
                        chosenPiece[0].moove("up")
                    
                    if event.key == K_RIGHT:
                        chosenPiece[0].moove("right")
           
                    if event.key == K_LEFT:
                        chosenPiece[0].moove("left")
            
                    if event.key == K_r:
                        for cell in chosenPiece[0].cellsList:
                            cell.x = cell.initialX
                            cell.y = cell.initialY
                        phase = 1

                    if event.key == K_RETURN:
                    
                        canBePlaced = board.player_place_verification(chosenPiece[0])
                        if canBePlaced:
                            chosenPiece[0].place_piece(board)
                            score += chosenPiece[0].cellNumber
                        elif canBePlaced == False:
                            for cell in chosenPiece[0].cellsList:
                                cell.texture = cell.cantPlaceTexture
                            
                            chosenPiece[0].canBePlaced = False
                            cantPlaceSound.play()
                                        
                        if canBePlaced == True:
                            #Check for lines who has been made and add to the score
                    
                            lineCellNumber = board.line_verification_suppression()
                        
                            if lineCellNumber > 0:
                                score += lineCellNumber
                                winingLineSound.play()
                        
                            #Check for a possible game over
                            boardPlaceTestList = []
                            
                            if piece1[0].placed == False:
                            
                                boardPlaceTestList.append(board.place_verification(piece1[0]))
                                if piece2[0].placed == False:
                                    boardPlaceTestList.append(board.place_verification(piece2[0]))
                                if piece3[0].placed == False:
                                    boardPlaceTestList.append(board.place_verification(piece3[0]))
                            
                                piece1[0].selected = True
                                chosenPiece = piece1
                                
                            elif piece1[0].placed == True:
                                if piece2[0].placed == False:
                            
                                    boardPlaceTestList.append(board.place_verification(piece2[0]))
                                    if piece3[0].placed == False:
                                        boardPlaceTestList.append(board.place_verification(piece3[0]))
                                
                                    piece2[0].selected = True
                                    chosenPiece = piece2
                                    
                                elif piece2[0].placed == True:
                                    if piece3[0].placed == False:
                                
                                        boardPlaceTestList.append(board.place_verification(piece3[0]))
                                    
                                        piece3[0].selected = True
                                        chosenPiece = piece3
                                        
                                    elif piece3[0].placed == True:
                                
                                        #Generate 3 other pieces if all has been placed
                                        piece1, piece2, piece3 = functions.generate_pieces()
                                        piece1[0].selected = True
                                        chosenPiece = piece1

                                        boardPlaceTestList.append(board.place_verification(piece1[0]))
                                        boardPlaceTestList.append(board.place_verification(piece2[0]))
                                        boardPlaceTestList.append(board.place_verification(piece3[0]))
                        
                            #Test if we are game over or not
                            gameOverTest = functions.check_game_over(boardPlaceTestList)
                            if gameOverTest == True:
                                gameOverSound.play()
                                functions.set_new_best_score_or_not(score, int(bestScore))
                                #Game over menu's buttons creation
                                homeButton = button_class.Button("home", constants.SCREENSIZE[0]/2-96, 200, constants.HOMEBUTTONTEXTURE, constants.HOMEBUTTONSELECTEDTEXTURE, True)
                                gameOverExitButton = button_class.Button("exit", constants.SCREENSIZE[0]/2-96, 400, constants.EXITBUTTONTEXTURE, constants.exitButtonSelectedTexture)
                                phase = 3
                            else:
                                phase = 1

        """Display every textures of the game at every loop in the right order."""
    
        screen.blit(background, (0,0))

        for cell in board.cellsList:
            screen.blit(cell.texture, (cell.x * constants.CELLSIZE, cell.y * constants.CELLSIZE))
    
        if phase == 1:
            for cell in piece1[0].cellsList:
                screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY1 + cell.y) * constants.CELLSIZE)))
            for cell in piece2[0].cellsList:
                screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY2 + cell.y) * constants.CELLSIZE)))
            for cell in piece3[0].cellsList:
                screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY3 + cell.y) * constants.CELLSIZE)))
    
        if phase == 2:
        
            if chosenPiece[0].canBePlaced == False:
                for cell in chosenPiece[0].cellsList:
                    screen.blit(cell.texture, (((0 + cell.x) * constants.CELLSIZE), ((0 + cell.y) * constants.CELLSIZE)))
                    
                if piece1[0].selected == False:
                    for cell in piece1[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY1 + cell.y) * constants.CELLSIZE)))
                if piece2[0].selected == False:
                    for cell in piece2[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY2 + cell.y) * constants.CELLSIZE)))
                if piece3[0].selected == False:
                    for cell in piece3[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY3 + cell.y) * constants.CELLSIZE)))
                    
                screen.blit(scoreText, (0.3*constants.CELLSIZE, 13.8*constants.CELLSIZE))
                screen.blit(bestScoreText, (0.3*constants.CELLSIZE, 15.8*constants.CELLSIZE))

                pygame.display.flip()
                time.sleep(0.6)
                
                for cell in chosenPiece[0].cellsList:
                    cell.texture = cell.selectedTexture
                    chosenPiece[0].canBePlaced = True
                
            else:
                for cell in chosenPiece[0].cellsList:
                    screen.blit(cell.texture, (((0 + cell.x) * constants.CELLSIZE), ((0 + cell.y) * constants.CELLSIZE)))
                
                if piece1[0].selected == False:
                    for cell in piece1[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY1 + cell.y) * constants.CELLSIZE)))
                if piece2[0].selected == False:
                    for cell in piece2[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY2 + cell.y) * constants.CELLSIZE)))
                if piece3[0].selected == False:
                    for cell in piece3[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY3 + cell.y) * constants.CELLSIZE)))
                    
        screen.blit(scoreText, (0.3*constants.CELLSIZE, 13.8*constants.CELLSIZE))
        screen.blit(bestScoreText, (0.3*constants.CELLSIZE, 15.8*constants.CELLSIZE))

        pygame.display.flip()

    while (phase == 3):
        clock.tick(constants.FPS)

        if not runGame: #If the player exit the game. Break the while loop to end up the program
            break

        for event in pygame.event.get(): #Exit event
            if event.type == QUIT:
                runGame = False

            if event.type == KEYDOWN:
                if event.key == K_DOWN: #Select the next button
                    if homeButton.selected:
                        homeButton.selected = False
                        gameOverExitButton.selected = True
                    elif gameOverExitButton.selected:
                        gameOverExitButton.selected = False
                        homeButton.selected = True

                if event.key == K_UP:   #Select the next button
                    if homeButton.selected:
                        homeButton.selected = False
                        gameOverExitButton.selected = True
                    elif gameOverExitButton.selected:
                        gameOverExitButton.selected = False
                        homeButton.selected = True

                if event.key == K_RETURN:   #Call the function of the selected button
                    if homeButton.selected:
                        phase = homeButton.do_function()
                        if phase == 0:
                            #Main menu's buttons creation
                            playButton = button_class.Button("play", constants.SCREENSIZE[0]/2-96, 200, constants.PLAYBUTTONTEXTURE, constants.PLAYBUTTONSELECTEDTEXTURE, True)
                            mainMenuExitButton = button_class.Button("exit", constants.SCREENSIZE[0]/2-96, 400, constants.EXITBUTTONTEXTURE, constants.exitButtonSelectedTexture)
                    elif gameOverExitButton.selected:
                        runGame = gameOverExitButton.do_function()

        """Display of the game over menu's objects"""
        screen.blit(backgroundGameOver,(0,0))
        screen.blit(gameOverText, (300, 50))
        screen.blit(homeButton.texture, (homeButton.x, homeButton.y))
        screen.blit(gameOverExitButton.texture, (gameOverExitButton.x, gameOverExitButton.y))

        pygame.display.flip()

pygame.quit()   #If the main loop is break it's because a "QUIT" event has been done. So we quit pygame