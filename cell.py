class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    '''
    Setter for this cell’s value
    '''
    def set_cell_value(self, value):
        self.value =  value

    '''
    Setter for this cell’s sketched value
    '''
    def set_sketched_value(self, value):
        self.value = value

    '''
    Draws this cell, along with the value inside it.
    If this cell has a nonzero value, that value is displayed.
    Otherwise, no value is displayed in the cell.
    The cell is outlined red if it is currently selected.
    '''
    def draw(self):
        pass
