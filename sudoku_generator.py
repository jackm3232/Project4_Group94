import math
import random


# Define "SudokuGenerator" class that generates a sudoku (in the form of a 2D list) and its solution
class SudokuGenerator:

    # Define constructor that initializes class variables and creates a 2D board (initially full of 0s)
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        initial_board = []
        for i in range(0, row_length):
            initial_board.append([])
            for j in range(0, row_length):
                initial_board[i].append(0)
        self.board = initial_board
        self.box_length = int(math.sqrt(row_length))

    # Define "get_board" method that returns the 2D board
    def get_board(self):
        return self.board

    # Define "print_board" method that prints the 2D board
    def print_board(self):
        for i in self.board:
            print(*i, sep=" ")

    # Define "valid_in_row" method that returns True if 'num' is not already present in 'row'
    def valid_in_row(self, row, num):
        for i in self.board[row]:
            if i == num:
                return False
        return True

    # Define "valid_in_col" method that returns True if 'num' is not already present in 'col'
    def valid_in_col(self, col, num):
        for i in range(0, self.row_length):
            if self.board[i][col] == num:
                return False
        return True

    # Define "valid_in_box" method that returns True if 'num' is not present in the specified 3x3 box
    # The 3x3 box is specified by 'row_start' and 'column_start'
    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.board[i][j] == num:
                    return False
        return True

    # Define "is_valid" method that returns True if 'num' can be placed in the cell specified by 'row' and 'col'
    # To be able to be placed, 'num' must be valid in the row, column, and 3x3 box
    def is_valid(self, row, col, num):
        good_in_row = self.valid_in_row(row, num)
        good_in_column = self.valid_in_col(col, num)
        good_in_box = self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num)
        if good_in_row and good_in_column and good_in_box is True:
            return True
        else:
            return False

    # Define "fill_box" method that fills specified 3x3 box with integers (range 1-9) randomly and without repeats
    # The 3x3 box is specified by 'row_start' and 'column_start'
    def fill_box(self, row_start, col_start):
        keep_filling = True
        num_to_fill = 0
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                while keep_filling is True:
                    num_to_fill = random.randint(1, 9)
                    if self.valid_in_box(row_start, col_start, num_to_fill) is True:
                        break
                self.board[i][j] = num_to_fill

    # Define "fill_diagonal" method that fills the three 3x3 boxes along diagonal of board (top left to bottom right)
    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

    # Define "fill_remaining" method that fills rest of the cells on the board (after first 3 boxes have been filled)
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    # Define "fill_values" method that completely fills the empty board (this is the solution to the sudoku)
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    # Define "remove_cells" method that removes specified amount of cells from the board by setting the values to 0
    # The locations of the cells removed are generated randomly and no cell can be removed more than once
    def remove_cells(self):
        count = 0
        while count != self.removed_cells:
            row_index = random.randint(0, self.row_length - 1)
            col_index = random.randint(0, self.row_length - 1)
            if self.board[row_index][col_index] != 0:
                self.board[row_index][col_index] = 0
                count += 1


# Define "generate_sudoku" function that creates an instance of a sudoku, fills it, removes cells, and returns the board
# The 2D board returned is the board that will be shown to the player at the beginning of the game (it is not solved)
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
