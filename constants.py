"""Screen"""
SCREENSIZE = [608, 640]
SCREENXMIDDLE = SCREENSIZE[0] // 2

CELLSIZE = 32

BOARDBEGINNINGX = CELLSIZE*5
BOARDBEGINNINGY = CELLSIZE*4

PIECECHOOSEPLACEX = 12
PIECECHOOSEPLACEY1 = 0
PIECECHOOSEPLACEY2 = 6
PIECECHOOSEPLACEY3 = 12

MAINMENUBUTTONPLACEY1 = 150
MAINMENUBUTTONPLACEY2 = 270
MAINMENUBUTTONPLACEY3 = 390

"""Game loop constants"""
FPS = 60

"""Textures"""
BACKGROUNDTEXTURE = "assets/textures/Background.png"
GAMEOVERBACKGROUNDTEXTURE = "assets/textures/Background_game_over.png"
SETTINGSBACKGROUNDTEXTURE = "assets/textures/Settings_background.png"
TITLETEXTURE = "assets/textures/Title.png"
SOUNDSETTINGSTEXTURE = "assets/textures/Sound_settings.png"

#Buttons
BUTTONSTEXTURE = "assets/textures/button.png"
BUTTONSSELECTEDTEXTURE = "assets/textures/button_selected.png"
MUSICONBUTTONTEXTURE = "assets/textures/Music_on.png"
MUSICONBUTTONSELECTEDTEXTURE = "assets/textures/Music_on_selected.png"
MUSICOFFBUTTONTEXTURE = "assets/textures/Music_off.png"
MUSICOFFBUTTONSELECTEDTEXTURE = "assets/textures/Music_off_selected.png"
SOUNDONBUTTONTEXTURE = "assets/textures/Sound_on.png"
SOUNDONBUTTONSELECTEDTEXTURE = "assets/textures/Sound_on_selected.png"
SOUNDOFFBUTTONTEXTURE = "assets/textures/Sound_off.png"
SOUNDOFFBUTTONSELECTEDTEXTURE = "assets/textures/Sound_off_selected.png"
GAMESOUNDSETTINGSBUTTONTEXTURE = "assets/textures/Game_sound_settings_button.png"
GAMESOUNDSETTINGSBUTTONSELECTEDTEXTURE = "assets/textures/Game_sound_settings_button_selected.png"

#Cell's texture
BOARDCELLTEXTURE = "assets/textures/Empty_cell.png"
UNSELECTEDCELLTEXTURE = "assets/textures/Unselected_cell.png"
SELECTEDCELLTEXTURE = "assets/textures/Selected_cell.png"
CANTPLACECELLTEXTURE = "assets/textures/Cant_place_cell.png"

#List of list of cell's argument (pick a random list to generate a piece)
PIECELIST = [
    
    [{"x":0, "y":0}],

    [{"x":0, "y":0}, {"x":0, "y":1}],
    [{"x":0, "y":0}, {"x":1, "y":0}],

    [{"x":0, "y":0}, {"x":0, "y":1}, {"x":0, "y":2}],
    [{"x":0, "y":0}, {"x":1, "y":0}, {"x":2, "y":0}],

    [{"x":0, "y":0}, {"x":0, "y":1}, {"x":0, "y":2}, {"x":0, "y":3}],
    [{"x":0, "y":0}, {"x":1, "y":0}, {"x":2, "y":0}, {"x":3, "y":0}],
    
    [{"x":0, "y":0}, {"x":0, "y":1}, {"x":0, "y":2}, {"x":0, "y":3}, {"x":0, "y":4}],
    [{"x":0, "y":0}, {"x":1, "y":0}, {"x":2, "y":0}, {"x":3, "y":0}, {"x":4, "y":0}],

    [{"x":0, "y":0}, {"x":1, "y":0}, {"x":2, "y":0}, {"x":2, "y":1}],
    [{"x":0, "y":0}, {"x":1, "y":0}, {"x":2, "y":0}, {"x":0, "y":1}],
    [{"x":0, "y":1}, {"x":1, "y":1}, {"x":2, "y":1}, {"x":2, "y":0}],
    [{"x":0, "y":1}, {"x":1, "y":1}, {"x":2, "y":1}, {"x":0, "y":0}],
    [{"x":0, "y":0}, {"x":0, "y":1}, {"x":0, "y":2}, {"x":1, "y":2}],
    [{"x":0, "y":0}, {"x":1, "y":0}, {"x":0, "y":1}, {"x":0, "y":2}],
    [{"x":0, "y":0}, {"x":1, "y":0}, {"x":1, "y":1}, {"x":1, "y":2}],
    [{"x":1, "y":0}, {"x":1, "y":1}, {"x":1, "y":2}, {"x":0, "y":2}],


    [{"x":0, "y":0}, {"x":0, "y":1}, {"x":1, "y":1}],
    [{"x":1, "y":0}, {"x":1, "y":1}, {"x":0, "y":1}],
    [{"x":0, "y":0}, {"x":1, "y":0}, {"x":0, "y":1}],
    [{"x":0, "y":0}, {"x":1, "y":0}, {"x":1, "y":1}],

    [{"x":0, "y":0}, {"x":0, "y":1}, {"x":1, "y":0}, {"x":1, "y":1}],

    [{"x":0, "y":0}, {"x":0, "y":1}, {"x":0, "y":2}, {"x":1, "y":2}, {"x":2, "y":2}],
    [{"x":2, "y":0}, {"x":2, "y":1}, {"x":2, "y":2}, {"x":1, "y":2}, {"x":0, "y":2}],
    [{"x":0, "y":0}, {"x":1, "y":0}, {"x":2, "y":0}, {"x":0, "y":1}, {"x":0, "y":2}],
    [{"x":0, "y":0}, {"x":1, "y":0}, {"x":2, "y":0}, {"x":2, "y":1}, {"x":2, "y":2}],

    [{"x":0, "y":0}, {"x":0, "y":1}, {"x":0, "y":2}, {"x":1, "y":0}, {"x":1, "y":1}, {"x":1, "y":2}, {"x":2, "y":0}, {"x":2, "y":1}, {"x":2, "y":2}],
]