import constants
import cell_class

"""Board class of the game.
   It is a list of cells (cell_class)."""
class Board:
        
    def __init__(self, x=10, y=10):
        
        self.x_size = x
        self.y_size = y
        self._cellsList = []
           
    #CellsList property
    def _get_cellsList(self):
        return self._cellsList
    cellsList = property(_get_cellsList)

    def build(self):
        """Build the board based on the size given."""
        
        x_counter = 0
        y_counter = 0
        
        while(y_counter < self.y_size):
            while(x_counter < self.x_size):
                self.cellsList.append(cell_class.Cell(x_counter, y_counter))
                x_counter += 1
            
            y_counter += 1
            x_counter = 0
            
    def place_verification(self, piece):
        """Test if a piece can be placed on the board: 
           - Take the piece that we wanna test in parameter
           - Return the true if the piece can be placed and false if it can't."""
        
        test = False
        currentTest = False
        cellToTest = [0,0]
        
        for boardCell in self.cellsList:
            
                for pieceCell in piece.cellsList:

                    cellToTest[0] = boardCell.x + pieceCell.x
                    cellToTest[1] = boardCell.y + pieceCell.y

                    if cellToTest[0] <= 9 and cellToTest[1] <= 9:
                    
                        for boardCellToTest in self.cellsList:
                            if boardCellToTest.x == cellToTest[0] and boardCellToTest.y == cellToTest[1]:
                                if boardCellToTest.empty == False:
                                    currentTest = False
                                    break
                                elif boardCellToTest.empty == True:
                                    currentTest = True
                                    break
                                
                        if currentTest == False:
                            break
                    else:
                        currentTest = False
                        break
                        
                if currentTest == True:
                    test = True
                    break
                    
                elif currentTest == False:
                    test = False
        
        return test
        
    def player_place_verification(self, piece):
        """Test if the piece can be placed where the player decide to place:
           - Take the piece that we wanna test in parameter
           - Return the true if the piece can be placed and false if it can't."""
        
        test = True
        
        for pieceCell in piece.cellsList:
            for boardCell in self.cellsList:
                
                if boardCell.x == pieceCell.x and boardCell.y == pieceCell.y:
                    if boardCell.empty == False:
                        test = False
                    break
            
            if test == False:
                return test
                
        return test
        
    def line_verification_suppression(self):
        """Test if one or more lines of the board are complete.
        If it is, remove the lines and return the number of lines removed."""
        
        LineCellNumber = 0
        
        cellToTest = [0,0]
        test = 0
        
        for cell in self.cellsList:
            
            cellToTest[0] = cell.x
            cellToTest[1] = cell.y

            #Test the "empty" attribute of each cell of the horizontal lines
            if cell.x == 0:
            
                while cellToTest[0] < 10:
                    for boardCellToTest in self.cellsList:
                        if boardCellToTest.x == cellToTest[0] and boardCellToTest.y == cellToTest[1]:
                            if boardCellToTest.empty == True:
                                test = False
                                break
                            elif boardCellToTest.empty == False:
                                test = True
                                break
                    if test == False:
                        break
                    cellToTest[0] += 1
                cellToTest[0] -= 1
                
                #Remove the horizontal line if all the cell are not empty (empty == False)
                if test == True:
                    while cellToTest[0] >= 0:
                        for cell in self.cellsList:
                            if cell.x == cellToTest[0] and cell.y == cellToTest[1]:
                                cell.empty = True
                                cell.texture = cell.unselectedTexture
                                LineCellNumber += 1
                                break
                        cellToTest[0] -= 1

                if cell.y == 0:

                    cellToTest[0] = 0
                    cellToTest[1] = 0

                    while cellToTest[1] < 10:
                        for boardCellToTest in self.cellsList:
                            if boardCellToTest.x == cellToTest[0] and boardCellToTest.y == cellToTest[1]:
                                if boardCellToTest.empty == True:
                                    test = False
                                    break
                                elif boardCellToTest.empty == False:
                                    test = True
                                    break
                        if test == False:
                            break
                        cellToTest[1] += 1
                    cellToTest[1] -= 1    

                    #Remove the line if the cells are not empty. (empty == False)
                    if test == True:
                        while cellToTest[1] >= 0:
                            for cell in self.cellsList:
                                if cell.x == cellToTest[0] and cell.y == cellToTest[1]:
                                    cell.empty = True
                                    cell.texture = cell.unselectedTexture
                                    LineCellNumber += 1
                                    break
                            cellToTest[1] -= 1
            
            #Test the "empty" attribute of each cells of the vertical lines
            elif cell.y == 0:
                
                while cellToTest[1] < 10:
                    for boardCellToTest in self.cellsList:
                        if boardCellToTest.x == cellToTest[0] and boardCellToTest.y == cellToTest[1]:
                            if boardCellToTest.empty == True:
                                test = False
                                break
                            elif boardCellToTest.empty == False:
                                test = True
                                break
                    if test == False:
                        break
                    cellToTest[1] += 1
                cellToTest[1] -= 1
                
                #Remove the line if the cells are not empty. (empty == False)
                if test == True:
                    while cellToTest[1] >= 0:
                        for cell in self.cellsList:
                            if cell.x == cellToTest[0] and cell.y == cellToTest[1]:
                                cell.empty = True
                                cell.texture = cell.unselectedTexture
                                LineCellNumber += 1
                                break
                        cellToTest[1] -= 1
                            
        return LineCellNumber
                            
    def put_down_piece(self, piece):
        """Place the piece on the board.
           Modify the properties of the board's cells at the position where we put down the piece"""
        
        counter = piece.cellNumber
        
        for boardCell in self.cellsList:
        
            """If each cells of the piece are placed (counter == 0), then we stop crossing the board cells list."""
            if counter == 0:
                break
            
            for pieceCell in piece.cellsList:
                
                if boardCell.x == pieceCell.x and boardCell.y == pieceCell.y:
                
                    """Modification of the cell's board properties.
                    (empty == False) and take the texture of the piece."""
                    boardCell.empty = False
                    boardCell.texture = pieceCell.texture
                    counter -= 1
                    
                    break
