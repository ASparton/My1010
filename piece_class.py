import constants

"""Class that will be the pieces of the game.
 A piece is a cell (cell_class) list.
This class control the pieces in the game (moove, place...).
"""
class Piece:
        
    def __init__(self, cellsList, selected=False):
        
        self._cellsList = cellsList
        
        self._selected = selected
        self._placed = False
        self._canBePlaced = True
        
        self._cellNumber = 0
        self._cellNumberX = 0
        self._cellNumberY = 0

        self.def_cell_number()

    """Properties"""
    #cellsList property
    def _get_cellsList(self):
        return self._cellsList
    def _set_cellsList(self, cellsList):
        self._cellsList = cellsList
    cellsList = property(_get_cellsList, _set_cellsList)

    #selected property
    def _get_selected(self):
        return self._selected
    def _set_selected(self, selected):
        self._selected = selected
    selected = property(_get_selected, _set_selected)
    #placed property
    def _get_placed(self):
        return self._placed
    def _set_placed(self, placed):
        self._placed = placed
    placed = property(_get_placed, _set_placed)
    #canBePlaced property
    def _get_canBePlaced(self):
        return self._canBePlaced
    def _set_canBePlaced(self, canBePlaced):
        self._canBePlaced = canBePlaced
    canBePlaced = property(_get_canBePlaced, _set_canBePlaced)

    #cellNumber property
    def _get_cellNumber(self):
        return self._cellNumber
    def _set_cellNumber(self, cellNumber):
        self._cellNumber = cellNumber
    cellNumber = property(_get_cellNumber, _set_cellNumber)
    #cellNumberX property
    def _get_cellNumberX(self):
        return self._cellNumberX
    def _set_cellNumberX(self, cellNumberX):
        self._cellNumberX = cellNumberX
    cellNumberX = property(_get_cellNumberX, _set_cellNumberX)
    #cellNumberY property
    def _get_cellNumberY(self):
        return self._cellNumberY
    def _set_cellNumberY(self, cellNumberY):
        self._cellNumberY = cellNumberY
    cellNumberY = property(_get_cellNumber, _set_cellNumberY)

    def def_cell_number(self):
        """Give the number of cells in the piece + number in X and Y specific axis"""
        
        xmax = 0
        ymax = 0
        
        for cell in self.cellsList:
            self.cellNumber = self.cellNumber + 1
            
            if xmax < cell.x:
                xmax = cell.x
                
            if ymax < cell.y:
                ymax = cell.y
                
        self.cellNumberX = xmax
        self.cellNumberY = ymax
          
    def select(self):
        """Select each cell of the piece and the piece itself"""
        
        for cell in self.cellsList:
            cell.select = True
            cell.texture = cell.selectedTexture
            
        self.selected = True
        
    def unselect(self):
        """Unselect each cell of the piece and the piece itself"""
        
        for cell in self.cellsList:
            cell.texture = cell.unselectedTexture
            cell.select = False
            
        self.selected = False
        
    def moove(self, direction):
        """Method to moove the piece to one of the 4 directions"""
        
         #Variable that allow or not a piece to moove after testing if each cell of that piece will still be in the board
        outside = False

        if direction == "right":
            for cell in self.cellsList: #If we moove right the piece, test if it will be outside of the board or not
                if (cell.x + 1) > 9:
                    outside = True
            
            if outside == False: #If it's not outside, then moove each in cell (= the entire piece)
                for cell in self.cellsList:
                    cell.x += 1
                
        if direction == "left":
            for cell in self.cellsList:
                if (cell.x - 1) < 0:
                    outside = True

            if outside == False:
                for cell in self.cellsList:        
                    cell.x -=1
                
        if direction == "up":
            for cell in self.cellsList:
                if (cell.y - 1) < 0:
                    outside = True

            if outside == False:
                for cell in self.cellsList:
                    cell.y -=1
                
        if direction == "down":
            for cell in self.cellsList:
                if (cell.y + 1) > 9:
                    outside = True

            if outside == False:
                for cell in self.cellsList:
                    cell.y +=1
            
    def place_piece(self, board):
        """Put down the piece on the board :
        - Unselect the piece
        - Use "put_down_piece" method of the board to change the properties of the board
        - Change the placed attribute to true
        - Place the actual piece outside of the screen (it will be removed when the 3 next pieces will be generated)."""
        
        self.unselect()
        board.put_down_piece(self)
        
        self.placed = True
        for cell in self.cellsList:
            cell.x = 20
            cell.y = 20
