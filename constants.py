"""Screen"""
screenSize = [640, 544]

cellSize = 32

pieceChoosePlaceX = 12
pieceChoosePlaceY1 = 0
pieceChoosePlaceY2 = 6
pieceChoosePlaceY3 = 12

"""Textures"""
backgroundTexture = "assets/textures/Background.png"
gameOverBackgroundTexture = "assets/textures/Background_game_over.png"

#Main menu
titleTexture = "assets/textures/Title.png"

#Buttons
playButtonTexture = "assets/textures/Play_button.png"
playButtonSelectedTexture = "assets/textures/Play_button_selected.png"
exitButtonTexture = "assets/textures/Exit_button.png"
exitButtonSelectedTexture = "assets/textures/Exit_button_selected.png"
homeButtonTexture = "assets/textures/Home_button.png"
homeButtonSelectedTexture = "assets/textures/Home_button_selected.png"
    
#Cell's texture
boardCellTexture = "assets/textures/Empty_cell.png"

redCellTexture = "assets/textures/Red_cell.png"
lightBlueCellTexture = "assets/textures/Light_blue_cell.png"
orangeCellTexture = "assets/textures/Orange_cell.png"
yellowCellTexture = "assets/textures/Yellow_cell.png"
blueCellTexture = "assets/textures/Blue_cell.png"
blackCellTexture = "assets/textures/Black_cell.png"
brownCellTexture = "assets/textures/Brown_cell.png"
greenCellTexture = "assets/textures/Green_cell.png"
pinkCellTexture = "assets/textures/Pink_cell.png"
purpleCellTexture = "assets/textures/Purple_cell.png"

#Selected cell's texture
redCellSelectedTexture = "assets/textures/Red_cell_selected.png"
lightBlueCellSelectedTexture = "assets/textures/Light_blue_cell_selected.png"
orangeCellSelectedTexture = "assets/textures/Orange_cell_selected.png"
yellowCellSelectedTexture = "assets/textures/Yellow_cell_selected.png"
blueCellSelectedTexture = "assets/textures/Blue_cell_selected.png"
blackCellSelectedTexture = "assets/textures/Black_cell_selected.png"
brownCellSelectedTexture = "assets/textures/Brown_cell_selected.png"
greenCellSelectedTexture = "assets/textures/Green_cell_selected.png"
pinkCellSelectedTexture = "assets/textures/Pink_cell_selected.png"
purpleCellSelectedTexture = "assets/textures/Purple_cell_selected.png"

#Can't be placed cell's texture
redCantPlaceTexture = "assets/textures/Red_cell_not.png"
lightBlueCantPlaceTexture = "assets/textures/Light_blue_cell_not.png"
orangeCantPlaceTexture = "assets/textures/Orange_cell_not.png"
yellowCantPlaceTexture = "assets/textures/Yellow_cell_not.png"
blueCantPlaceTexture = "assets/textures/Blue_cell_not.png"
blackCantPlaceTexture = "assets/textures/Black_cell_not.png"
brownCantPlaceTexture = "assets/textures/Brown_cell_not.png"
greenCantPlaceTexture = "assets/textures/Green_cell_not.png"
pinkCantPlaceTexture = "assets/textures/Pink_cell_not.png"
purpleCantPlaceTexture = "assets/textures/Purple_cell_not.png"

#List of list of cell's argument (pick a random list to generate a piece)
pieceList = [
    
    [{"x":0, "y":0,"textureUnselected": redCellTexture, "textureSelected": redCellSelectedTexture, "textureNot": redCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": blueCellTexture, "textureSelected": blueCellSelectedTexture, "textureNot": blueCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": blueCellTexture, "textureSelected": blueCellSelectedTexture, "textureNot": blueCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": blueCellTexture, "textureSelected": blueCellSelectedTexture, "textureNot": blueCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": blueCellTexture, "textureSelected": blueCellSelectedTexture, "textureNot": blueCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": lightBlueCellTexture, "textureSelected": lightBlueCellSelectedTexture, "textureNot": lightBlueCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":0, "y":3,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}, {"x":3, "y":0,"textureUnselected": purpleCellTexture, "textureSelected": purpleCellSelectedTexture, "textureNot": purpleCantPlaceTexture}],
    
    [{"x":0, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":0, "y":3,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":0, "y":4,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":3, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}, {"x":4, "y":0,"textureUnselected": brownCellTexture, "textureSelected": brownCellSelectedTexture, "textureNot": brownCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],
    [{"x":1, "y":0,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": greenCellTexture, "textureSelected": greenCellSelectedTexture, "textureNot": greenCantPlaceTexture}],


    [{"x":0, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}],
    [{"x":1, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": yellowCellTexture, "textureSelected": yellowCellSelectedTexture, "textureNot": yellowCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": blackCellTexture, "textureSelected": blackCellSelectedTexture, "textureNot": blackCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": blackCellTexture, "textureSelected": blackCellSelectedTexture, "textureNot": blackCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": blackCellTexture, "textureSelected": blackCellSelectedTexture, "textureNot": blackCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": blackCellTexture, "textureSelected": blackCellSelectedTexture, "textureNot": blackCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}],
    [{"x":2, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}],
    [{"x":0, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}, {"x":2, "y":2,"textureUnselected": pinkCellTexture, "textureSelected": pinkCellSelectedTexture, "textureNot": pinkCantPlaceTexture}],

    [{"x":0, "y":0,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":0, "y":1,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":0, "y":2,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":1, "y":0,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":1, "y":1,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":1, "y":2,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":2, "y":0,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":2, "y":1,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}, {"x":2, "y":2,"textureUnselected": orangeCellTexture, "textureSelected": orangeCellSelectedTexture, "textureNot": orangeCantPlaceTexture}],
]