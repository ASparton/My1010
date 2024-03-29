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

"""Pygame + mixer initialization to delete the sound delay in the pygame.mixer"""
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(44100, -16, 2, 1024)

"""Program setup"""

#Screen setup
screen = pygame.display.set_mode((constants.SCREENSIZE[0], constants.SCREENSIZE[1]))
pygame.display.set_caption("Retro 1010!")

#Game music and sound setup
pygame.mixer.music.load("assets/sounds/Retro Samurai.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1) #Play the music indefinitely
soundDict = {"winingLine":pygame.mixer.Sound("assets/sounds/Line.wav"), "cantPlace":pygame.mixer.Sound("assets/sounds/Cant_place.wav"),
"gameOver":pygame.mixer.Sound("assets/sounds/Game_over.wav"), "select":pygame.mixer.Sound("assets/sounds/Select.wav"),
"piecePlaced":pygame.mixer.Sound("assets/sounds/Placed.wav"), "moove":pygame.mixer.Sound("assets/sounds/Moove.wav"),
"beginGame":pygame.mixer.Sound("assets/sounds/Begin.wav"), "enter":pygame.mixer.Sound("assets/sounds/Enter.wav")}
for sound in soundDict.keys():
    soundDict[sound].set_volume(0.5)    #Set the volume on each sound at 0.5

#Font setup
titleFont = pygame.font.Font("assets/fonts/karma future.ttf", 72)
gameOverFont = titleFont = pygame.font.Font("assets/fonts/karma future.ttf", 60)
font = pygame.font.Font("assets/fonts/karma future.ttf", 26)

#Texture loading
background = pygame.image.load(constants.BACKGROUNDTEXTURE).convert_alpha()
settingsBackground = pygame.image.load(constants.SETTINGSBACKGROUNDTEXTURE).convert_alpha()
buttonsTexture = pygame.image.load(constants.BUTTONSTEXTURE).convert_alpha()    #Just to get the size

#Game buttons
gameSoundSettingsButton = button_class.Button("settings", constants.SCREENSIZE[0]-100, constants.BOARDBEGINNINGY*constants.CELLSIZE, "", False, constants.GAMESOUNDSETTINGSBUTTONTEXTURE, constants.GAMESOUNDSETTINGSBUTTONSELECTEDTEXTURE)
playButton = button_class.Button("play", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY1, "PLAY", True)
soundSettingsButton = button_class.Button("settings", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY2, "SETTINGS")
exitButton = button_class.Button("exit", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY3, "EXIT")

#Settings board setup
soundSettings = soundSettings_class.SoundSettings(constants.SCREENSIZE[0]/2 - 125, constants.SCREENSIZE[1]/2 - 75)
def draw_sound_settings():
    """Display all the elements when the player enter the sound settings."""
    if not soundSettings.close:
        screen.blit(settingsBackground, (0,0))
        screen.blit(soundSettings.texture, (soundSettings.x, soundSettings.y))
        soundSettings.texture.blit(soundSettings.exitButton.texture, (soundSettings.exitButton.x, soundSettings.exitButton.y))
        soundSettings.exitButton.texture.blit(soundSettings.exitButton.title, (soundSettings.exitButton.titlePosition[0], soundSettings.exitButton.titlePosition[1]))
        if soundSettings.soundOn:
            soundSettings.texture.blit(soundSettings.soundOnButton.texture, (soundSettings.soundOnButton.x, soundSettings.soundOnButton.y))
        elif not soundSettings.soundOn:
            soundSettings.texture.blit(soundSettings.soundOffButton.texture, (soundSettings.soundOffButton.x, soundSettings.soundOffButton.y))
        if soundSettings.musicOn:
            soundSettings.texture.blit(soundSettings.musicOnButton.texture, (soundSettings.musicOnButton.x, soundSettings.musicOnButton.y))
        elif not soundSettings.musicOn:
            soundSettings.texture.blit(soundSettings.musicOffButton.texture, (soundSettings.musicOffButton.x, soundSettings.musicOffButton.y))
    #IMPORTANT: Refresh the screen even if the sound setting is closed
    # because this draw function is called after the draw function of the future game parts        
    pygame.display.flip()

def sound_settings_function():
    """Function called when the player enter the sound settings.
    It allows the player to navigate trough the music and the sounds to mute them or play them.
    We have to repeat this instructions in diferent parts of the game."""
    if event.key == K_LEFT:
        if soundSettings.selectedButton == soundSettings.soundOffButton or soundSettings.selectedButton == soundSettings.soundOnButton:
            soundDict["select"].play()
        soundSettings.selectNextButton("left")
    elif event.key == K_RIGHT:
        if soundSettings.selectedButton == soundSettings.musicOffButton or soundSettings.selectedButton == soundSettings.musicOnButton:
            soundDict["select"].play()
        soundSettings.selectNextButton("right")
    elif event.key == K_UP:
        if soundSettings.selectedButton != soundSettings.exitButton:
            soundDict["select"].play()
        soundSettings.selectNextButton("up")
    elif event.key == K_DOWN:
        if soundSettings.selectedButton == soundSettings.exitButton:
            soundDict["select"].play()
        soundSettings.selectNextButton("down")

    elif event.key == K_RETURN:

        if soundSettings.soundOnButton.selected:
            soundSettings.set_sound(False)
            for sound in soundDict.keys():
                soundDict[sound].set_volume(0)

        elif soundSettings.soundOffButton.selected:
            soundDict["enter"].play()
            soundSettings.set_sound(True)
            for sound in soundDict.keys():
                soundDict[sound].set_volume(0.5)

        elif soundSettings.musicOnButton.selected:
            soundDict["enter"].play()
            soundSettings.set_music(False)
            pygame.mixer.music.pause()

        elif soundSettings.musicOffButton.selected:
            soundDict["enter"].play()
            soundSettings.set_music(True)
            pygame.mixer.music.unpause()

        elif soundSettings.exitButton.selected:
            soundSettings.close = True

#game variables setup
phase = "main_menu" #3 phases in the program (1: main_menu / 2: game / 3: game_over)
gamePhase = "choose" #2 phases in the game phase (1: choose(the player pick a piece) / 2: board(the player cross the board to place the piece in it))
gameOver = False
createDrawFunction = False  #We have to create the draw function of the program phase only once
GAMEOVERTEXT = gameOverFont.render("Game Over", False, (139,172,15))
TITLE = titleFont.render("RETRO 1010!", False, (132,187,132))

#game loop setup
clock = pygame.time.Clock() #Create a clock to control FPS (How many times per second the main loop will run)
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
                screen.blit(TITLE, ((constants.SCREENXMIDDLE-TITLE.get_size()[0]//2), 0))
                screen.blit(playButton.texture, (playButton.x, playButton.y))
                playButton.texture.blit(playButton.title, (playButton.titlePosition[0], playButton.titlePosition[1]))
                screen.blit(exitButton.texture, (exitButton.x, exitButton.y))
                exitButton.texture.blit(exitButton.title, (exitButton.titlePosition[0], exitButton.titlePosition[1]))
                screen.blit(soundSettingsButton.texture, (soundSettingsButton.x, soundSettingsButton.y))
                soundSettingsButton.texture.blit(soundSettingsButton.title, (soundSettingsButton.titlePosition[0], soundSettingsButton.titlePosition[1]))

        for event in pygame.event.get(): #Exit event
            if event.type == QUIT:
                runGame = False

            if event.type == KEYDOWN:
                if soundSettings.close:

                    if event.key == K_DOWN: #Select the next button
                        soundDict["select"].play()
                        if playButton.selected:
                            playButton.selected = False
                            soundSettingsButton.selected = True
                        elif soundSettingsButton.selected:
                            soundSettingsButton.selected = False
                            exitButton.selected = True
                        else:
                            exitButton.selected = False
                            playButton.selected = True

                    elif event.key == K_UP:   #Select the next button
                        soundDict["select"].play()
                        if playButton.selected:
                            playButton.selected = False
                            exitButton.selected = True
                        elif soundSettingsButton.selected:
                            soundSettingsButton.selected = False
                            playButton.selected = True
                        else:
                            exitButton.selected = False
                            soundSettingsButton.selected = True

                    elif event.key == K_RETURN:   #Call the function of the selected button

                        if playButton.selected:
                            soundDict["beginGame"].play()
                            phase = playButton.do_function()
                            createDrawFunction = False
                            gamePhase = "choose"
                            board = board_class.Board() #Board creation
                            board.build()
                            piece1, piece2, piece3 = functions.generate_pieces()    #Pieces generation
                            #Use of arrays to imitate a pointer which is here chosenPiece 
                            chosenPiece = piece1    #For now it points on piece1
                            piece1[0].selected = True   #We select the first piece. Then the player will choose from that start
                            score = 0   #Set the score at the beginning
                            bestScore = functions.get_best_score()
                            
                        elif exitButton.selected:
                            runGame = exitButton.do_function()
                            soundDict["enter"].play()
                        else:
                            soundSettings.close = soundSettingsButton.do_function()
                            soundDict["enter"].play()

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
                screen.blit(TITLE, ((constants.SCREENSIZE[0]//2-TITLE.get_size()[0]//2), 0))

                for cell in board.cellsList:
                    screen.blit(cell.texture, ((constants.BOARDBEGINNINGX + cell.x) * constants.CELLSIZE, (constants.BOARDBEGINNINGY + cell.y) * constants.CELLSIZE))
                    
                if gamePhase == "choose":
                    for cell in piece1[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX1 + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY + cell.y) * constants.CELLSIZE)))
                    for cell in piece2[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX2 + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY + cell.y)* constants.CELLSIZE)))
                    for cell in piece3[0].cellsList:
                        screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX3 + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY + cell.y)* constants.CELLSIZE)))
                    
                elif gamePhase == "board":
                        
                    if chosenPiece[0].canBePlaced == False:
                        for cell in chosenPiece[0].cellsList:
                            screen.blit(cell.texture, ((cell.x * constants.CELLSIZE), (cell.y * constants.CELLSIZE)))
                                    
                        if piece1[0].selected == False:
                            for cell in piece1[0].cellsList:
                                screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX1 + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY + cell.y) * constants.CELLSIZE)))
                        if piece2[0].selected == False:
                            for cell in piece2[0].cellsList:
                                screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX2 + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY + cell.y) * constants.CELLSIZE)))
                        if piece3[0].selected == False:
                            for cell in piece3[0].cellsList:
                                screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX3 + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY + cell.y) * constants.CELLSIZE)))

                        screen.blit(gameSoundSettingsButton.texture, (gameSoundSettingsButton.x, gameSoundSettingsButton.y))    
                        screen.blit(scoreText, (1*constants.CELLSIZE, 6*constants.CELLSIZE))
                        screen.blit(scorePoint, (2*constants.CELLSIZE, 7*constants.CELLSIZE))
                        screen.blit(bestScoreText, (0, 10*constants.CELLSIZE))
                        screen.blit(bestScorePoint, (2*constants.CELLSIZE, 11*constants.CELLSIZE))

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
                                screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX1 + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY + cell.y) * constants.CELLSIZE)))
                        if piece2[0].selected == False:
                            for cell in piece2[0].cellsList:
                                screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX2 + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY + cell.y) * constants.CELLSIZE)))
                        if piece3[0].selected == False:
                            for cell in piece3[0].cellsList:
                                screen.blit(cell.texture, (((constants.PIECECHOOSEPLACEX3 + cell.x) * constants.CELLSIZE), ((constants.PIECECHOOSEPLACEY + cell.y) * constants.CELLSIZE)))

                screen.blit(gameSoundSettingsButton.texture, (gameSoundSettingsButton.x, gameSoundSettingsButton.y))
                screen.blit(scoreText, (1*constants.CELLSIZE, 6*constants.CELLSIZE))
                screen.blit(scorePoint, (2*constants.CELLSIZE, 7*constants.CELLSIZE))
                screen.blit(bestScoreText, (0, 10*constants.CELLSIZE))
                screen.blit(bestScorePoint, (2*constants.CELLSIZE, 11*constants.CELLSIZE))

        #Creation of the scores texts
        strScore = " SCORE: " 
        scoreText = font.render(strScore, False, (159,196,159))
        strScorePoint = str(score)
        scorePoint = font.render(strScorePoint, False, (159, 196,159))
        strBestScore = " BEST SCORE: "
        bestScoreText = font.render(strBestScore, False, (159,196,159))
        bestScorePoint = font.render(bestScore, False, (159,196,159))

        for event in pygame.event.get(): #Exit event
            if event.type == QUIT:
                runGame = False

            if gamePhase == "choose":
                """When we are in choose game phase, the player need to choose a piece with the directional keys,
                and need to press "Return" to choose the one he wants. That's the events we are wainting for"""
                if event.type == KEYDOWN:
                    if soundSettings.close:

                        if event.key == K_RIGHT:    #Select the next piece in function of how many pieces left in the selection
                            if piece1[0].selected == True:
                                piece1[0].selected = False
                                
                                if piece2[0].placed == False:
                                    piece2[0].selected = True
                                    chosenPiece = piece2
                                    soundDict["select"].play()
                                    
                                elif piece2[0].placed == True:
                                    if piece3[0].placed == False:
                                        piece3[0].selected = True
                                        chosenPiece = piece3
                                        soundDict["select"].play()
                                        
                                    elif piece3[0].placed == True:
                                        piece1[0].selected = True
                                        chosenPiece = piece1
                                
                            elif piece2[0].selected == True:
                                piece2[0].selected = False
                                
                                if piece3[0].placed == False:
                                    piece3[0].selected = True
                                    chosenPiece = piece3
                                    soundDict["select"].play()
                                    
                                elif piece3[0].placed == True:
                                    if piece1[0].placed == False:
                                        piece1[0].selected = True
                                        chosenPiece = piece1
                                        soundDict["select"].play()
                                        
                                    elif piece1[0].placed == True:
                                        piece2[0].selected = True
                                        chosenPiece = piece2
                                
                            elif piece3[0].selected == True:
                                piece3[0].selected = False
                                
                                if piece1[0].placed == False:
                                    piece1[0].selected = True
                                    chosenPiece = piece1
                                    soundDict["select"].play()
                                    
                                elif piece1[0].placed == True:
                                    if piece2[0].placed == False:
                                        piece2[0].selected = True
                                        chosenPiece = piece2
                                        soundDict["select"].play()
                                        
                                    elif piece2[0].placed == True:
                                        piece3[0].selected = True
                                        chosenPiece = piece3
                                    
                        elif event.key == K_LEFT:   #Select the next piece in function of how many pieces left in the selection
                            if piece1[0].selected == True:
                                piece1[0].selected = False
                            
                                if piece3[0].placed == False:
                                    piece3[0].selected = True
                                    chosenPiece = piece3
                                    soundDict["select"].play()
                                
                                elif piece3[0].placed == True:
                                    if piece2[0].placed == False:
                                        piece2[0].selected = True
                                        chosenPiece = piece2
                                        soundDict["select"].play()
                                    
                                    elif piece2[0].placed == True:
                                        piece1[0].selected = True
                                        chosenPiece = piece1
                            
                            elif piece2[0].selected == True:
                                piece2[0].selected = False
                            
                                if piece1[0].placed == False:
                                    piece1[0].selected = True
                                    chosenPiece = piece1
                                    soundDict["select"].play()
                                
                                elif piece1[0].placed == True:
                                    if piece3[0].placed == False:
                                        piece3[0].selected = True
                                        chosenPiece = piece3
                                        soundDict["select"].play()
                                    
                                    elif piece3[0].placed == True:
                                        piece2[0].selected = True
                                        chosenPiece = piece2
                            
                            elif piece3[0].selected == True:
                                piece3[0].selected = False
                            
                                if piece2[0].placed == False:
                                    piece2[0].selected = True
                                    chosenPiece = piece2
                                    soundDict["select"].play()
                                
                                elif piece2[0].placed == True:
                                    if piece1[0].placed == False:
                                        piece1[0].selected = True
                                        chosenPiece = piece1
                                        soundDict["select"].play()
                                    
                                    elif piece1[0].placed == True:
                                        piece3[0].selected = True
                                        chosenPiece = piece3
                        
                        elif event.key == K_UP: #Select the settings button
                            soundDict["select"].play()
                            gameSoundSettingsButton.selected = True
                            if piece1[0].selected == True:
                                piece1[0].selected = False
                            elif piece2[0].selected == True:
                                piece2[0].selected = False
                            elif piece3[0].selected == True:
                                piece3[0].selected = False
                        
                        elif event.key == K_DOWN:   #Return from the settings button to the pieces to pick one
                            soundDict["select"].play()
                            gameSoundSettingsButton.selected = False
                            chosenPiece[0].selected = True

                        elif event.key == K_RETURN:
                            
                            if gameSoundSettingsButton.selected:
                                soundSettings.close = gameSoundSettingsButton.do_function() #Open the sound settings
                                soundDict["enter"].play()
                            else:
                                for cell in chosenPiece[0].cellsList:   #Place the chosen piece on the board
                                    cell.x = constants.BOARDBEGINNINGX + cell.x
                                    cell.y = constants.BOARDBEGINNINGY + cell.y
                                gamePhase = "board"

                    elif not soundSettings.close:
                        sound_settings_function()
                
            elif gamePhase == "board":
                """During the board phase :
                - We wait for the player to moove the piece on the board with the directional keys.
                - Then we wait for him to put down the piece on the board with enter. if he is allowed to.
                - Then we check for a possible game over and generate other pieces if there is no more and return to phase 1"""
                if event.type == KEYDOWN:
                    
                    #Save the position of the piece before the events to check if it has mooved after (to play the moove sound or not)
                    cellsPiecePositionBeforeAction = []
                    for cells in chosenPiece[0].cellsList:
                        cellsPiecePositionBeforeAction.append([cells.x, cells.y])

                    if event.key == K_DOWN:
                        chosenPiece[0].moove("down")

                    if event.key == K_UP:
                        chosenPiece[0].moove("up")

                    if event.key == K_RIGHT:
                        chosenPiece[0].moove("right")

                    if event.key == K_LEFT:
                        chosenPiece[0].moove("left")
                    
                    didNotMoove = functions.check_moove(chosenPiece, cellsPiecePositionBeforeAction)
                    if not didNotMoove:
                        soundDict["moove"].play()
            
                    if event.key == K_BACKSPACE:    #If the player press backspace he can return to choose phase to pick an other piece
                        for cell in chosenPiece[0].cellsList:   #So we have to replace the place at her start point
                            cell.x = cell.initialX
                            cell.y = cell.initialY
                        gamePhase = "choose"

                    if event.key == K_RETURN:  
                        #If the player press return, check if he can place the piece where he wants to then act in function of this test.
                    
                        canBePlaced = board.player_place_verification(chosenPiece[0])
                        #If it can't be placed, then we change the texture and play a sound to show that he can't place the piece here.
                        if not canBePlaced:
                            soundDict["cantPlace"].play()
                            for cell in chosenPiece[0].cellsList:
                                cell.texture = cell.cantPlaceTexture
                            chosenPiece[0].canBePlaced = False

                        elif canBePlaced:
                            #Place the piece on the board and update the score
                            chosenPiece[0].place_piece(board)
                            score += chosenPiece[0].cellNumber
                    
                            #Check if line has been done
                            lineCellNumber = board.line_verification_suppression()
                            if lineCellNumber > 0:
                                soundDict["winingLine"].play()
                                score += lineCellNumber
                            else:
                                soundDict["piecePlaced"].play()
                        
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
                                pygame.mixer.music.pause()
                                soundDict["gameOver"].play()
                                functions.set_new_best_score_or_not(score, int(bestScore))
                                #Game over menu's buttons creation
                                homeButton = button_class.Button("home", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, 320, "MAIN MENU", True)
                                exitButton.x = constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2
                                exitButton.y = 480
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
                screen.blit(TITLE, (constants.SCREENSIZE[0]//2 - TITLE.get_size()[0]//2, 0))
                screen.blit(GAMEOVERTEXT, (constants.SCREENSIZE[0]//2 - GAMEOVERTEXT.get_size()[0]//2, 3*constants.CELLSIZE))
                screen.blit(homeButton.texture, (homeButton.x, homeButton.y))
                homeButton.texture.blit(homeButton.title, (homeButton.titlePosition[0], homeButton.titlePosition[1]))
                screen.blit(exitButton.texture, (exitButton.x, exitButton.y))
                exitButton.texture.blit(exitButton.title, (exitButton.titlePosition[0], exitButton.titlePosition[1]))
                screen.blit(scoreText, (4*constants.CELLSIZE, 7*constants.CELLSIZE))
                screen.blit(bestScoreText, (10*constants.CELLSIZE, 7*constants.CELLSIZE))
                pygame.display.flip()

        #Redef of the score's texts
        strScoreText = "SCORE: " + str(score)
        scoreText = font.render(strScoreText, False, (159, 196,159))
        strBestScoreText = "BEST SCORE: " + bestScore
        bestScoreText = font.render(strBestScoreText, False, (159, 196,159))

        for event in pygame.event.get(): #Exit event
            if event.type == QUIT:
                runGame = False

            if event.type == KEYDOWN:

                if event.key == K_DOWN: #Select the next button
                    soundDict["select"].play()
                    if homeButton.selected:
                        homeButton.selected = False
                        exitButton.selected = True
                    elif exitButton.selected:
                        exitButton.selected = False
                        homeButton.selected = True

                if event.key == K_UP:   #Select the next button
                    soundDict["select"].play()
                    if homeButton.selected:
                        homeButton.selected = False
                        exitButton.selected = True
                    elif exitButton.selected:
                        exitButton.selected = False
                        homeButton.selected = True

                if event.key == K_RETURN:   #Call the function of the selected button
                    soundDict["enter"].play()

                    if homeButton.selected:
                        phase = homeButton.do_function()
                        createDrawFunction = False
                        #Main menu's buttons creation
                        playButton = button_class.Button("play", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY1, "PLAY", True)
                        soundSettingsButton = button_class.Button("settings", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY2, "SETTINGS")
                        exitButton = button_class.Button("exit", constants.SCREENXMIDDLE-buttonsTexture.get_size()[0]//2, constants.MAINMENUBUTTONPLACEY3, "EXIT")
                        pygame.mixer.music.unpause()

                    elif exitButton.selected:
                        runGame = exitButton.do_function()
        
        draw_game_over_screen()

pygame.quit()   #If the main loop is break it's because a "QUIT" event has been done. So we quit pygame