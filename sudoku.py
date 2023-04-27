import random

class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.is_editable = True
        self.is_Selected = False
        self.sketched_value = 0
        self.has_sketched = False

    def set_cell_value(self, value):
        self.value = value
        self.has_sketched = False
        self.sketched_value = 0

    def set_sketched_value(self, value):
        self.sketched_value = value
        self.has_sketched = True

    def draw(self):
        # for debugging
        pass


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = {}
        self.selected_cell = None
        self.first_Selection = True

    # makes dictionary of cells with coordinates as key
    def set_up_cells(self, generated_sudoku):
        i = 0
        while i < self.width:
            j = 0
            while j < self.height:
                self.cells[i, j] = Cell(generated_sudoku.board[j][i], j, i, self.screen)
                j +=1
            i += 1

    def draw(self):
        for cell in self.cells:
            cell.draw()

    # selects cell, clears past selection so only one selected at a time
    def select(self, row, col):
        if not self.first_Selection:
            previous_cell = self.selected_cell
            previous_cell.is_Selected = False
        self.selected_cell = self.cells[row, col]
        self.selected_cell.is_Selected = True
        self.selected_cell.draw()
        self.first_Selection = False

    # translates clicking in window to selecting cell coordinates
    def click(self, x, y):
        col_value = int((x -209.5) / 45)
        row_value = int((y-28) / 45)
        self.select(row_value, col_value)

    def clear(self):
        self.selected_cell.set_cell_value(0)

    # sets all editable cells back to 0
    def clear_whole_board(self):
        for cell in self.cells:
            if self.cells[cell].is_editable:
                self.cells[cell].set_cell_value(0)

    def sketch(self, value):
        self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        self.selected_cell.set_cell_value(value)

    def reset_to_original(self, sudoku):
        for cell in self.cells:
            cell.set_cell_value = sudoku[cell.row][cell.col]
            # row and col might have to be reversed ^^^^

    # checks if board is full
    def is_full(self):
        num_empty_cells = 0
        for cell in self.cells:
            if cell.value != 0:
                num_empty_cells += 1
        if num_empty_cells == 0:
            return True
        else:
            return False

    # sets sudoku equal to cell values
    def update_board(self, sudoku):
        cell_key_list = self.cells.keys()
        for cell_key in cell_key_list:
            this_cell = self.cells[cell_key]
            sudoku_board = sudoku.get_board()
            sudoku_board[this_cell.row][this_cell.col] = this_cell.value

    # sees if there are any empty cells
    def find_empty(self):
        empty_cells = []
        cell_list = self.cells.values()
        for cell in cell_list:
            if cell.value == 0:
                empty_cells.append(cell)
        if len(empty_cells) == 0:
            return True
        else:
            return False

    # checks if empty, then updates board
    def check_board(self, sudoku):
        if self.find_empty():
            self.update_board(sudoku)
            res = True
        else:
            res = False
        return res


