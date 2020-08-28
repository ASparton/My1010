"""Screen"""
SCREENSIZE = [640, 544]

CELLSIZE = 32

PIECECHOOSEPLACEX = 12
PIECECHOOSEPLACEY1 = 0
PIECECHOOSEPLACEY2 = 6
PIECECHOOSEPLACEY3 = 12

"""Game loop constants"""
FPS = 60

"""Textures"""
BACKGROUNDTEXTURE = "assets/textures/Background.png"
GAMEOVERBACKGROUNDTEXTURE = "assets/textures/Background_game_over.png"
TITLETEXTURE = "assets/textures/Title.png"
BOARDSETTINGSTEXTURE = "assets/textures/Board_settings.png"

#Buttons
PLAYBUTTONTEXTURE = "assets/textures/Play_button.png"
PLAYBUTTONSELECTEDTEXTURE = "assets/textures/Play_button_selected.png"
EXITBUTTONTEXTURE = "assets/textures/Exit_button.png"
EXITBUTTONSELECTEDTEXTURE = "assets/textures/Exit_button_selected.png"
HOMEBUTTONTEXTURE = "assets/textures/Home_button.png"
HOMEBUTTONSELECTEDTEXTURE = "assets/textures/Home_button_selected.png"
SETTINGSBUTTONTEXTURE = "assets/textures/Settings_button.png"
SETTINGSBUTTONSELECTEDTEXTURE = "assets/textures/Settings_button_selected.png"
MUSICONBUTTONTEXTURE = "assets/textures/Music_on.png"
MUSICONBUTTONSELECTEDTEXTURE = "assets/textures/Music_on_selected.png"
MUSICOFFBUTTONTEXTURE = "assets/textures/Music_off.png"
MUSICOFFBUTTONSELECTEDTEXTURE = "assets/textures/Music_off_selected.png"
SOUNDONBUTTONTEXTURE = "assets/textures/Sound_on.png"
SOUNDONBUTTONSELECTEDTEXTURE = "assets/textures/Sound_on_selected.png"
SOUNDOFFBUTTONTEXTURE = "assets/textures/Sound_off.png"
SOUNDOFFBUTTONSELECTEDTEXTURE = "assets/textures/Sound_off_selected.png"

#Cell's texture
BOARDCELLTEXTURE = "assets/textures/Empty_cell.png"

REDCELLTEXTURE = "assets/textures/Red_cell.png"
LIGHTBLUECELLTEXTURE = "assets/textures/Light_blue_cell.png"
ORANGECELLTEXTURE = "assets/textures/Orange_cell.png"
YELLOWCELLTEXTURE = "assets/textures/Yellow_cell.png"
BLUECELLTEXTURE = "assets/textures/Blue_cell.png"
BLACKCELLTEXTURE = "assets/textures/Black_cell.png"
BROWNCELLTEXTURE = "assets/textures/Brown_cell.png"
GREENCELLTEXTURE = "assets/textures/Green_cell.png"
PINKCELLTEXTURE = "assets/textures/Pink_cell.png"
PURPLECELLTEXTURE = "assets/textures/Purple_cell.png"

#Selected cell's texture
REDCELLSELECTEDTEXTURE = "assets/textures/Red_cell_selected.png"
LIGHTBLUECELLSELECTEDTEXTURE = "assets/textures/Light_blue_cell_selected.png"
ORANGECELLSELECTEDTEXTURE = "assets/textures/Orange_cell_selected.png"
YELLOWCELLSELECTEDTEXTURE = "assets/textures/Yellow_cell_selected.png"
BLUECELLSELECTEDTEXTURE = "assets/textures/Blue_cell_selected.png"
BLACKCELLSELECTEDTEXTURE = "assets/textures/Black_cell_selected.png"
BROWNCELLSELECTEDTEXTURE = "assets/textures/Brown_cell_selected.png"
GREENCELLSELECTEDTEXTURE = "assets/textures/Green_cell_selected.png"
PINKCELLSELECTEDTEXTURE = "assets/textures/Pink_cell_selected.png"
PURPLECELLSELECTEDTEXTURE = "assets/textures/Purple_cell_selected.png"

#Can't be placed cell's texture
REDCANTPLACETEXTURE = "assets/textures/Red_cell_not.png"
LIGHTBLUECANTPLACETEXTURE = "assets/textures/Light_blue_cell_not.png"
ORANGECANTPLACETEXTURE = "assets/textures/Orange_cell_not.png"
YELLOWCANTPLACETEXTURE = "assets/textures/Yellow_cell_not.png"
BLUECANTPLACETEXTURE = "assets/textures/Blue_cell_not.png"
BLACKCANTPLACETEXTURE = "assets/textures/Black_cell_not.png"
BROWNCANTPLACETEXTURE = "assets/textures/Brown_cell_not.png"
GREENCANTPLACETEXTURE = "assets/textures/Green_cell_not.png"
PINKCANTPLACETEXTURE = "assets/textures/Pink_cell_not.png"
PURPLECANTPLACETEXTURE = "assets/textures/Purple_cell_not.png"

#List of list of cell's argument (pick a random list to generate a piece)
PIECELIST = [
    
    [{"x":0, "y":0,"textureUnselected": REDCELLTEXTURE, "textureSelected": REDCELLSELECTEDTEXTURE, "textureNot": REDCANTPLACETEXTURE}],

    [{"x":0, "y":0,"textureUnselected": BLUECELLTEXTURE, "textureSelected": BLUECELLSELECTEDTEXTURE, "textureNot": BLUECANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": BLUECELLTEXTURE, "textureSelected": BLUECELLSELECTEDTEXTURE, "textureNot": BLUECANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": BLUECELLTEXTURE, "textureSelected": BLUECELLSELECTEDTEXTURE, "textureNot": BLUECANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": BLUECELLTEXTURE, "textureSelected": BLUECELLSELECTEDTEXTURE, "textureNot": BLUECANTPLACETEXTURE}],

    [{"x":0, "y":0,"textureUnselected": LIGHTBLUECELLTEXTURE, "textureSelected": LIGHTBLUECELLSELECTEDTEXTURE, "textureNot": LIGHTBLUECANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": LIGHTBLUECELLTEXTURE, "textureSelected": LIGHTBLUECELLSELECTEDTEXTURE, "textureNot": LIGHTBLUECANTPLACETEXTURE}, {"x":0, "y":2,"textureUnselected": LIGHTBLUECELLTEXTURE, "textureSelected": LIGHTBLUECELLSELECTEDTEXTURE, "textureNot": LIGHTBLUECANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": LIGHTBLUECELLTEXTURE, "textureSelected": LIGHTBLUECELLSELECTEDTEXTURE, "textureNot": LIGHTBLUECANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": LIGHTBLUECELLTEXTURE, "textureSelected": LIGHTBLUECELLSELECTEDTEXTURE, "textureNot": LIGHTBLUECANTPLACETEXTURE}, {"x":2, "y":0,"textureUnselected": LIGHTBLUECELLTEXTURE, "textureSelected": LIGHTBLUECELLSELECTEDTEXTURE, "textureNot": LIGHTBLUECANTPLACETEXTURE}],

    [{"x":0, "y":0,"textureUnselected": PURPLECELLTEXTURE, "textureSelected": PURPLECELLSELECTEDTEXTURE, "textureNot": PURPLECANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": PURPLECELLTEXTURE, "textureSelected": PURPLECELLSELECTEDTEXTURE, "textureNot": PURPLECANTPLACETEXTURE}, {"x":0, "y":2,"textureUnselected": PURPLECELLTEXTURE, "textureSelected": PURPLECELLSELECTEDTEXTURE, "textureNot": PURPLECANTPLACETEXTURE}, {"x":0, "y":3,"textureUnselected": PURPLECELLTEXTURE, "textureSelected": PURPLECELLSELECTEDTEXTURE, "textureNot": PURPLECANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": PURPLECELLTEXTURE, "textureSelected": PURPLECELLSELECTEDTEXTURE, "textureNot": PURPLECANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": PURPLECELLTEXTURE, "textureSelected": PURPLECELLSELECTEDTEXTURE, "textureNot": PURPLECANTPLACETEXTURE}, {"x":2, "y":0,"textureUnselected": PURPLECELLTEXTURE, "textureSelected": PURPLECELLSELECTEDTEXTURE, "textureNot": PURPLECANTPLACETEXTURE}, {"x":3, "y":0,"textureUnselected": PURPLECELLTEXTURE, "textureSelected": PURPLECELLSELECTEDTEXTURE, "textureNot": PURPLECANTPLACETEXTURE}],
    
    [{"x":0, "y":0,"textureUnselected": BROWNCELLTEXTURE, "textureSelected": BROWNCELLSELECTEDTEXTURE, "textureNot": BROWNCANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": BROWNCELLTEXTURE, "textureSelected": BROWNCELLSELECTEDTEXTURE, "textureNot": BROWNCANTPLACETEXTURE}, {"x":0, "y":2,"textureUnselected": BROWNCELLTEXTURE, "textureSelected": BROWNCELLSELECTEDTEXTURE, "textureNot": BROWNCANTPLACETEXTURE}, {"x":0, "y":3,"textureUnselected": BROWNCELLTEXTURE, "textureSelected": BROWNCELLSELECTEDTEXTURE, "textureNot": BROWNCANTPLACETEXTURE}, {"x":0, "y":4,"textureUnselected": BROWNCELLTEXTURE, "textureSelected": BROWNCELLSELECTEDTEXTURE, "textureNot": BROWNCANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": BROWNCELLTEXTURE, "textureSelected": BROWNCELLSELECTEDTEXTURE, "textureNot": BROWNCANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": BROWNCELLTEXTURE, "textureSelected": BROWNCELLSELECTEDTEXTURE, "textureNot": BROWNCANTPLACETEXTURE}, {"x":2, "y":0,"textureUnselected": BROWNCELLTEXTURE, "textureSelected": BROWNCELLSELECTEDTEXTURE, "textureNot": BROWNCANTPLACETEXTURE}, {"x":3, "y":0,"textureUnselected": BROWNCELLTEXTURE, "textureSelected": BROWNCELLSELECTEDTEXTURE, "textureNot": BROWNCANTPLACETEXTURE}, {"x":4, "y":0,"textureUnselected": BROWNCELLTEXTURE, "textureSelected": BROWNCELLSELECTEDTEXTURE, "textureNot": BROWNCANTPLACETEXTURE}],

    [{"x":0, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":2, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":2, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":2, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}],
    [{"x":0, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":1, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":2, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":2, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}],
    [{"x":0, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":1, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":2, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":0, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":0, "y":2,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":1, "y":2,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":0, "y":2,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":1, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":1, "y":2,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}],
    [{"x":1, "y":0,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":1, "y":1,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":1, "y":2,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}, {"x":0, "y":2,"textureUnselected": GREENCELLTEXTURE, "textureSelected": GREENCELLSELECTEDTEXTURE, "textureNot": GREENCANTPLACETEXTURE}],


    [{"x":0, "y":0,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}, {"x":1, "y":1,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}],
    [{"x":1, "y":0,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}, {"x":1, "y":1,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}, {"x":1, "y":1,"textureUnselected": YELLOWCELLTEXTURE, "textureSelected": YELLOWCELLSELECTEDTEXTURE, "textureNot": YELLOWCANTPLACETEXTURE}],

    [{"x":0, "y":0,"textureUnselected": BLACKCELLTEXTURE, "textureSelected": BLACKCELLSELECTEDTEXTURE, "textureNot": BLACKCANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": BLACKCELLTEXTURE, "textureSelected": BLACKCELLSELECTEDTEXTURE, "textureNot": BLACKCANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": BLACKCELLTEXTURE, "textureSelected": BLACKCELLSELECTEDTEXTURE, "textureNot": BLACKCANTPLACETEXTURE}, {"x":1, "y":1,"textureUnselected": BLACKCELLTEXTURE, "textureSelected": BLACKCELLSELECTEDTEXTURE, "textureNot": BLACKCANTPLACETEXTURE}],

    [{"x":0, "y":0,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":0, "y":2,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":1, "y":2,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":2, "y":2,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}],
    [{"x":2, "y":0,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":2, "y":1,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":2, "y":2,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":1, "y":2,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":0, "y":2,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":2, "y":0,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":0, "y":2,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}],
    [{"x":0, "y":0,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":2, "y":0,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":2, "y":1,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}, {"x":2, "y":2,"textureUnselected": PINKCELLTEXTURE, "textureSelected": PINKCELLSELECTEDTEXTURE, "textureNot": PINKCANTPLACETEXTURE}],

    [{"x":0, "y":0,"textureUnselected": ORANGECELLTEXTURE, "textureSelected": ORANGECELLSELECTEDTEXTURE, "textureNot": ORANGECANTPLACETEXTURE}, {"x":0, "y":1,"textureUnselected": ORANGECELLTEXTURE, "textureSelected": ORANGECELLSELECTEDTEXTURE, "textureNot": ORANGECANTPLACETEXTURE}, {"x":0, "y":2,"textureUnselected": ORANGECELLTEXTURE, "textureSelected": ORANGECELLSELECTEDTEXTURE, "textureNot": ORANGECANTPLACETEXTURE}, {"x":1, "y":0,"textureUnselected": ORANGECELLTEXTURE, "textureSelected": ORANGECELLSELECTEDTEXTURE, "textureNot": ORANGECANTPLACETEXTURE}, {"x":1, "y":1,"textureUnselected": ORANGECELLTEXTURE, "textureSelected": ORANGECELLSELECTEDTEXTURE, "textureNot": ORANGECANTPLACETEXTURE}, {"x":1, "y":2,"textureUnselected": ORANGECELLTEXTURE, "textureSelected": ORANGECELLSELECTEDTEXTURE, "textureNot": ORANGECANTPLACETEXTURE}, {"x":2, "y":0,"textureUnselected": ORANGECELLTEXTURE, "textureSelected": ORANGECELLSELECTEDTEXTURE, "textureNot": ORANGECANTPLACETEXTURE}, {"x":2, "y":1,"textureUnselected": ORANGECELLTEXTURE, "textureSelected": ORANGECELLSELECTEDTEXTURE, "textureNot": ORANGECANTPLACETEXTURE}, {"x":2, "y":2,"textureUnselected": ORANGECELLTEXTURE, "textureSelected": ORANGECELLSELECTEDTEXTURE, "textureNot": ORANGECANTPLACETEXTURE}],
]