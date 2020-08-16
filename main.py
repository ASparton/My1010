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

"""Initialization of all we need before starting the game."""

#Screen creations
screen = pygame.display.set_mode((constants.screenSize[0], constants.screenSize[1]), RESIZABLE)

#Background importation + display
background = pygame.image.load(constants.backgroundTexture).convert_alpha()
screen.blit(background, (0,0))
#Game over background importation
backgroundGameOver = pygame.image.load(constants.gameOverBackgroundTexture).convert_alpha()

#Font creation
font = pygame.font.SysFont("dearsunshine", 64)

#Board creation + display
board = board_class.Board()
board.build()
for cell in board.cellsList:
    screen.blit(cell.texture, (cell.x * constants.cellSize, cell.y * constants.cellSize))

#Pieces creation
randomCellList = random.choice(constants.pieceList)
piece1 = functions.create_piece(randomCellList)

randomCellList = random.choice(constants.pieceList)
piece2 = functions.create_piece(randomCellList)

randomCellList = random.choice(constants.pieceList)
piece3 = functions.create_piece(randomCellList)

#Pieces display
for cell in piece1.cellsList:
    screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))
for cell in piece2.cellsList:
    screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
for cell in piece3.cellsList:
    screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))

#We select the first piece. Then the player will choose from that start
piece1.select()
#Set the score at the beginning
score = 0

#Game music
pygame.mixer.music.load("Sons/Music.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

#Game sound initialization
winingLineSound = pygame.mixer.Sound("Sons/Ouh_nice_!.wav")
cantPlaceSound = pygame.mixer.Sound("Sons/Nope.wav")
gameOverSound = pygame.mixer.Sound("Sons/Game_over.wav")

#Game over variable initialization
gameOver = False
gameOverText = font.render("Game Over", False, (255, 255, 255))

"""Variable that cut the two phase of the game:
         - When phase == 1, we are in the first phase, the selection of the piece
         - When phase == 2, we are in the second phase, the player put down the piece on the board"""
phase = 1

#Load the screen
pygame.display.flip()

loop = 1
while loop:
    
    for event in pygame.event.get(): #Exit event
        if event.type == QUIT:
            loop = 0
        
        #We wait for game event and update the score only if we're not in game over
        if gameOver == False:
            score_conversion_text = str(score)
            score_text = font.render(score_conversion_text, False, (255,255,255))
    
            if phase == 1:
                """When we are in phase 1, the player need to choose a piece with the directional keys,
                and need to press "c" to choose the one he wants. That's the events we are wainting for"""
                if event.type == KEYDOWN:
                
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
                                
                    if event.key == K_c:
                    
                        if piece1.selected == True:
                            for cell in piece1.cellsList:
                                cell.x = 0 + cell.x
                                cell.y = 0 + cell.y
                        
                        elif piece2.selected == True:
                            for cell in piece1.cellsList:
                                cell.x = 0 + cell.x
                                cell.y = 0 + cell.y
                    
                        elif piece3.selected == True:
                            for cell in piece1.cellsList:
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
                
                        if piece1.selected == True:
                            piece1.moove("down")
                
                        elif piece2.selected == True:
                            piece2.moove("down")
                   
                        elif piece3.selected == True:
                            piece3.moove("down")
                
                    if event.key == K_UP:
                
                        if piece1.selected == True:
                            piece1.moove("up")
                    
                        elif piece2.selected == True:
                            piece2.moove("up")
                   
                        elif piece3.selected == True:
                            piece3.moove("up")
                    
                    if event.key == K_RIGHT:
                
                        if piece1.selected == True:
                            piece1.moove("right")
                    
                        elif piece2.selected == True:
                            piece2.moove("right")
                   
                        elif piece3.selected == True:
                            piece3.moove("right")
           
                    if event.key == K_LEFT:
                
                        if piece1.selected == True:
                            piece1.moove("left")
                    
                        elif piece2.selected == True:
                            piece2.moove("left")
                   
                        elif piece3.selected == True:
                            piece3.moove("left")
            
                    if event.key == K_RETURN:
                    
                        if piece1.selected == True:
                            canBePlaced = board.player_place_verification(piece1)
                            if canBePlaced:
                                piece1.place_piece(board)
                                score += piece1.cellNumber
                            elif canBePlaced == False:
                            
                                for cell in piece1.cellsList:
                                    cell.texture = cell.cantPlaceTexture
                            
                                piece1.canBePlaced = False
                                cantPlaceSound.play()
                            
                        elif piece2.selected == True:
                            canBePlaced = board.player_place_verification(piece2)
                            if canBePlaced:
                                piece2.place_piece(board)
                                score += piece2.cellNumber
                            elif canBePlaced == False:
                        
                                for cell in piece2.cellsList:
                                    cell.texture = cell.cantPlaceTexture
                                
                                piece2.canBePlaced = False
                                cantPlaceSound.play()
                            
                        elif piece3.selected == True:
                            canBePlaced = board.player_place_verification(piece3)
                            if canBePlaced:
                                piece3.place_piece(board)
                                score += piece3.cellNumber
                            elif canBePlaced == False:
                            
                                for cell in piece3.cellsList:
                                    cell.texture = cell.cantPlaceTexture
                                
                                piece3.canBePlaced = False
                                cantPlaceSound.play()
                                        
                        if canBePlaced == True:
                            #Check for lines who has been made and add to the score
                    
                            lineCellNumber = board.line_verification_suppression()
                        
                            if lineCellNumber > 0:
                                score += lineCellNumber
                                winingLineSound.play()
                        
                            #Check for a possible game over
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
                                
                                        #Generate 3 other pieces if all has been placed
                                    
                                        randomCellList = random.choice(constants.pieceList)
                                        piece1 = functions.create_piece(randomCellList)

                                        randomCellList = random.choice(constants.pieceList)
                                        piece2 = functions.create_piece(randomCellList)

                                        randomCellList = random.choice(constants.pieceList)
                                        piece3 = functions.create_piece(randomCellList)
                                    
                                        testList.append(board.place_verification(piece1))
                                        testList.append(board.place_verification(piece2))
                                        testList.append(board.place_verification(piece3))
                                    
                                        piece1.select()
                        
                            #Create the game over or not
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
            
        """Display every textures of the game at every loop in the right order."""
    
        screen.blit(background, (0,0))

        for cell in board.cellsList:
            screen.blit(cell.texture, (cell.x * constants.cellSize, cell.y * constants.cellSize))
    
        if phase == 1:
            for cell in piece1.cellsList:
                screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))
            for cell in piece2.cellsList:
                screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
            for cell in piece3.cellsList:
                screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))
    
        if phase == 2:
        
            if piece1.selected == True:
        
                if piece1.canBePlaced == False:
                    for cell in piece1.cellsList:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
                    
                    for cell in piece2.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
                    for cell in piece3.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))    
                    
                    pygame.display.flip()
                    time.sleep(0.6)
                
                    for cell in piece1.cellsList:
                        cell.texture = cell.selectedTexture
                        piece1.canBePlaced = True
                
                else:
                    for cell in piece1.cellsList:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
                
                    for cell in piece2.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
                    for cell in piece3.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))
                    
            elif piece2.selected == True:
        
                if piece2.canBePlaced == False:
                    for cell in piece2.cellsList:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
                    
                    for cell in piece1.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))
                    for cell in piece3.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))    
                    
                    pygame.display.flip()
                    time.sleep(0.6)
                
                    for cell in piece2.cellsList:
                        cell.texture = cell.selectedTexture
                        piece2.canBePlaced = True
                    
                else:
                    for cell in piece2.cellsList:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
                
                    for cell in piece1.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))
                    for cell in piece3.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY3 + cell.y) * constants.cellSize)))
                
            elif piece3.selected == True:
        
                if piece3.canBePlaced == False:
                    for cell in piece3.cellsList:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
                    
                    for cell in piece2.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
                    for cell in piece1.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))
                    
                    pygame.display.flip()
                    time.sleep(0.6)
                
                    for cell in piece3.cellsList:
                        cell.texture = cell.selectedTexture
                        piece3.canBePlaced = True
                    
                else:
                    for cell in piece3.cellsList:
                        screen.blit(cell.texture, (((0 + cell.x) * constants.cellSize), ((0 + cell.y) * constants.cellSize)))
            
                    for cell in piece2.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY2 + cell.y) * constants.cellSize)))
                    for cell in piece1.cellsList:
                        screen.blit(cell.texture, (((constants.pieceChoosePlaceX + cell.x) * constants.cellSize), ((constants.pieceChoosePlaceY1 + cell.y) * constants.cellSize)))

        if gameOver == True:
            screen.blit(backgroundGameOver,(0,0))
            screen.blit(gameOverText, (6*constants.cellSize, 7*constants.cellSize))
    
        screen.blit(score_text, (1*constants.cellSize, 15*constants.cellSize))

        pygame.display.flip()
