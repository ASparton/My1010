import pygame
from pygame.locals import *

import time

import constants
import functions
import cell_class
import board_class
import piece_class
import button_class
import soundSettings_class

pygame.init()

"""Program setup"""

#Screen setup
screen = pygame.display.set_mode((constants.SCREENSIZE[0], constants.SCREENSIZE[1]), RESIZABLE)
pygame.display.set_caption("Retro 1010!")

#Game music and sound setup
pygame.mixer.music.load("assets/sounds/The Grand Affair.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
soundDict = {"winingLineSound":pygame.mixer.Sound("assets/sounds/Ouh_nice_!.wav"), "cantPlaceSound":pygame.mixer.Sound("assets/sounds/Nope.wav"), "gameOverSound":pygame.mixer.Sound("assets/sounds/Game_over.wav")}
for sound in soundDict.keys():
    soundDict[sound].set_volume(0.5)

#Font setup
titleFont = pygame.font.Font("assets/fonts/karma future.ttf", 72)
mainFont = pygame.font.Font("assets/fonts/karma suture.ttf", 24)

#Texture loading
background = pygame.image.load(constants.BACKGROUNDTEXTURE).convert_alpha()
settingsBackground = pygame.image.load(constants.SETTINGSBACKGROUNDTEXTURE).convert_alpha()
buttonsTexture = pygame.image.load(constants.BUTTONSTEXTURE).convert_alpha()    #Just to get the size

#Game sound settings button
gameSoundSettingsButton = button_class.Button("settings", constants.SCREENSIZE[0]-100, 0, "", False, constants.GAMESOUNDSETTINGSBUTTONTEXTURE, constants.GAMESOUNDSETTINGSBUTTONSELECTEDTEXTURE)

#Main menu setup
title = titleFont.render("RETRO 1010!", False, (132,187,132))
playButton = button_class.Button("play", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY1, "PLAY", True)
soundSettingsButton = button_class.Button("settings", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY2, "SETTINGS")
mainMenuExitButton = button_class.Button("exit", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY3, "EXIT")

#Settings board setup
soundSettings = soundSettings_class.SoundSettings(constants.SCREENSIZE[0]/2 - 125, constants.SCREENSIZE[1]/2 - 75)
def draw_sound_settings():
    if not soundSettings.close:
        screen.blit(settingsBackground, (0,0))
        screen.blit(soundSettings.texture, (soundSettings.x, soundSettings.y))
        soundSettings.texture.blit(soundSettings.exitButton.texture, (soundSettings.exitButton.x, soundSettings.exitButton.y))
        if soundSettings.soundOn:
            soundSettings.texture.blit(soundSettings.soundOnButton.texture, (soundSettings.soundOnButton.x, soundSettings.soundOnButton.y))
        elif not soundSettings.soundOn:
            soundSettings.texture.blit(soundSettings.soundOffButton.texture, (soundSettings.soundOffButton.x, soundSettings.soundOffButton.y))
        if soundSettings.musicOn:
            soundSettings.texture.blit(soundSettings.musicOnButton.texture, (soundSettings.musicOnButton.x, soundSettings.musicOnButton.y))
        elif not soundSettings.musicOn:
            soundSettings.texture.blit(soundSettings.musicOffButton.texture, (soundSettings.musicOffButton.x, soundSettings.musicOffButton.y))
    pygame.display.flip()
def sound_settings_function():
    if event.key == K_LEFT:
        soundSettings.selectNextButton("left")
    elif event.key == K_RIGHT:
        soundSettings.selectNextButton("right")
    elif event.key == K_UP:
        soundSettings.selectNextButton("up")
    elif event.key == K_DOWN:
        soundSettings.selectNextButton("down")

    elif event.key == K_RETURN:
        if soundSettings.soundOnButton.selected:
            soundSettings.set_sound(False)
            for sound in soundDict.keys():
                soundDict[sound].set_volume(0)

        elif soundSettings.soundOffButton.selected:
            soundSettings.set_sound(True)
            for sound in soundDict.keys():
                soundDict[sound].set_volume(0.5)

        elif soundSettings.musicOnButton.selected:
            soundSettings.set_music(False)
            pygame.mixer.music.pause()

        elif soundSettings.musicOffButton.selected:
            soundSettings.set_music(True)
            pygame.mixer.music.unpause()

        elif soundSettings.exitButton.selected:
            soundSettings.close = True

#game variables setup
phase = "main_menu"
gamePhase = "choose"
gameOver = False
createDrawFunction = False
GAMEOVERTEXT = titleFont.render("Game Over", False, (139,172,15))

#game loop setup
clock = pygame.time.Clock()
runGame = True

while runGame:
     #Set the max FPS of the game to "constants.FPS" (60), so we have the same loop time on every system
    clock.tick(constants.FPS)

    while (phase == "main_menu"):
        clock.tick(constants.FPS)
        if not runGame: #If the player exit the game. Break the while loop to end up the program
            break

        if not createDrawFunction:  #To create the function only once
            createDrawFunction = True
            def draw_main_menu_screen():    #draw function: draw/display the main menu screen
                screen.blit(background, (0,0))
                screen.blit(title, ((constants.SCREENSIZE[0]//2-title.get_size()[0]//2), 0))
                screen.blit(playButton.texture, (playButton.x, playButton.y))
                playButton.texture.blit(playButton.title, (playButton.titlePosition[0], playButton.titlePosition[1]))
                screen.blit(mainMenuExitButton.texture, (mainMenuExitButton.x, mainMenuExitButton.y))
                mainMenuExitButton.texture.blit(mainMenuExitButton.title, (mainMenuExitButton.titlePosition[0], mainMenuExitButton.titlePosition[1]))
                screen.blit(soundSettingsButton.texture, (soundSettingsButton.x, soundSettingsButton.y))
                soundSettingsButton.texture.blit(soundSettingsButton.title, (soundSettingsButton.titlePosition[0], soundSettingsButton.titlePosition[1]))

        for event in pygame.event.get(): #Exit event
            if event.type == QUIT:
                runGame = False

            if event.type == KEYDOWN:
                if soundSettings.close:

                    if event.key == K_DOWN: #Select the next button
                        if playButton.selected:
                            playButton.selected = False
                            soundSettingsButton.selected = True
                        elif soundSettingsButton.selected:
                            soundSettingsButton.selected = False
                            mainMenuExitButton.selected = True
                        else:
                            mainMenuExitButton.selected = False
                            playButton.selected = True

                    elif event.key == K_UP:   #Select the next button
                        if playButton.selected:
                            playButton.selected = False
                            mainMenuExitButton.selected = True
                        elif soundSettingsButton.selected:
                            soundSettingsButton.selected = False
                            playButton.selected = True
                        else:
                            mainMenuExitButton.selected = False
                            soundSettingsButton.selected = True

                    elif event.key == K_RETURN:   #Call the function of the selected button
                        if playButton.selected:
                            phase = playButton.do_function()
                            createDrawFunction = False
                            gamePhase = "choose"
                            board = board_class.Board() #Board creation
                            board.build()
                            piece1, piece2, piece3 = functions.generate_pieces()    #Pieces generation
                            #Pointer (list) of the piece the player is going to choose
                            chosenPiece = piece1    #For now it points on piece1
                            piece1[0].selected = True   #We select the first piece. Then the player will choose from that start
                            score = 0   #Set the score at the beginning
                            bestScore = functions.get_best_score()
                            
                        elif mainMenuExitButton.selected:
                            runGame = mainMenuExitButton.do_function()
                        else:
                            soundSettings.close = soundSettingsButton.do_function()

                elif not soundSettings.close:
                    sound_settings_function()

        draw_main_menu_screen()
        draw_sound_settings()

    while (phase == "game"):
        clock.tick(constants.FPS)
        if not runGame: #If the player exit the game. Break the while loop to end up the program
            break

        if not createDrawFunction:  #To create the function only once
            createDrawFunction = True
            def draw_game_screen(gamePhase):    #Draw the game screen
                screen.blit(background, (0,0))

                for cell in board.cellsList:
                    screen.blit(cell.texture, (cell.x * constants.CELLSIZE, cell.y * constants.CELLSIZE))
                    
                if gamePhase == "choose":
                    for cell in piece1[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY1 + cell.y) * constants.CELLSIZE)))
                    for cell in piece2[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY2 + cell.y) * constants.CELLSIZE)))
                    for cell in piece3[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY3 + cell.y) * constants.CELLSIZE)))
                    
                elif gamePhase == "board":
                        
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

                        screen.blit(gameSoundSettingsButton.texture, (gameSoundSettingsButton.x, gameSoundSettingsButton.y))    
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

                screen.blit(gameSoundSettingsButton.texture, (gameSoundSettingsButton.x, gameSoundSettingsButton.y))
                screen.blit(scoreText, (constants.CELLSIZE, 14*constants.CELLSIZE))
                screen.blit(bestScoreText, (constants.CELLSIZE, 16*constants.CELLSIZE))

        #We wait for game event and update the score
        strScore = "SCORE: " + str(score)
        scoreText = mainFont.render(strScore, False, (255,255,255))
        strBestScore = "BEST SCORE: " + bestScore
        bestScoreText = mainFont.render(strBestScore, False, (255,255,255))

        for event in pygame.event.get(): #Exit event
            if event.type == QUIT:
                runGame = False

            if gamePhase == "choose":
                """When we are in choose game phase, the player need to choose a piece with the directional keys,
                and need to press "c" to choose the one he wants. That's the events we are wainting for"""
                if event.type == KEYDOWN:
                    if soundSettings.close:

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
                                    
                        elif event.key == K_UP:
                        
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
                        
                        elif event.key == K_RIGHT:
                            gameSoundSettingsButton.selected = True
                            if piece1[0].selected == True:
                                piece1[0].selected = False
                            elif piece2[0].selected == True:
                                piece2[0].selected = False
                            elif piece3[0].selected == True:
                                piece3[0].selected = False
                        
                        elif event.key == K_LEFT:
                            gameSoundSettingsButton.selected = False
                            chosenPiece[0].selected = True

                        elif event.key == K_RETURN:
                            
                            if gameSoundSettingsButton.selected:
                                soundSettings.close = gameSoundSettingsButton.do_function()
                            else:
                                for cell in chosenPiece[0].cellsList:
                                    cell.x = 0 + cell.x
                                    cell.y = 0 + cell.y
                                    
                                gamePhase = "board"

                    elif not soundSettings.close:
                        sound_settings_function()
                
            elif gamePhase == "board":
                """During the board phase :
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
                        gamePhase = "choose"

                    if event.key == K_RETURN:
                    
                        canBePlaced = board.player_place_verification(chosenPiece[0])
                        if canBePlaced:
                            chosenPiece[0].place_piece(board)
                            score += chosenPiece[0].cellNumber
                        elif canBePlaced == False:
                            for cell in chosenPiece[0].cellsList:
                                cell.texture = cell.cantPlaceTexture
                            
                            chosenPiece[0].canBePlaced = False
                            soundDict["cantPlaceSound"].play()
                                        
                        if canBePlaced == True:
                            #Check for lines who has been made and add to the score
                    
                            lineCellNumber = board.line_verification_suppression()
                        
                            if lineCellNumber > 0:
                                score += lineCellNumber
                                soundDict["winingLineSound"].play()
                        
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
                                soundDict["gameOverSound"].play()
                                functions.set_new_best_score_or_not(score, int(bestScore))
                                #Game over menu's buttons creation
                                homeButton = button_class.Button("home", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, 250, "MAIN MENU", True)
                                gameOverExitButton = button_class.Button("exit", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, 370, "EXIT")
                                phase = "game_over"
                                createDrawFunction = False
                            else:
                                gamePhase = "choose"

        draw_game_screen(gamePhase)
        draw_sound_settings()

    while (phase == "game_over"):
        clock.tick(constants.FPS)
        if not runGame: #If the player exit the game. Break the while loop to end up the program
            break

        if not createDrawFunction:
            createDrawFunction = True
            def draw_game_over_screen():
                screen.blit(background,(0,0))
                screen.blit(GAMEOVERTEXT, (constants.SCREENSIZE[0]//2 - GAMEOVERTEXT.get_size()[0]//2, 0))
                screen.blit(homeButton.texture, (homeButton.x, homeButton.y))
                homeButton.texture.blit(homeButton.title, (homeButton.titlePosition[0], homeButton.titlePosition[1]))
                screen.blit(gameOverExitButton.texture, (gameOverExitButton.x, gameOverExitButton.y))
                gameOverExitButton.texture.blit(gameOverExitButton.title, (gameOverExitButton.titlePosition[0], gameOverExitButton.titlePosition[1]))
                screen.blit(scoreText, (2*constants.CELLSIZE, 4*constants.CELLSIZE))
                screen.blit(bestScoreText, (12*constants.CELLSIZE, 4*constants.CELLSIZE))
                pygame.display.flip()

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
                        createDrawFunction = False
                        #Main menu's buttons creation
                        playButton = button_class.Button("play", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY1, "PLAY", True)
                        soundSettingsButton = button_class.Button("settings", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY2, "SETTINGS")
                        mainMenuExitButton = button_class.Button("exit", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY3, "EXIT")

                    elif gameOverExitButton.selected:
                        runGame = gameOverExitButton.do_function()
        
        draw_game_over_screen()

pygame.quit()   #If the main loop is break it's because a "QUIT" event has been done. So we quit pygame