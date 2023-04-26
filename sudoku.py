import random
class Cell:

    def __int__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.is_editable = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        pass

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = {}
        self.selected_cell = None

    def set_up_cells(self, sudoku):
        i = 0
        while i < self.width:
            j = 0
            while j < self.height:
                self.cells[i,j] = Cell(sudoku[i][j], j, i, self.screen)
                # i do not know why this is an error / warning?
                # i want to get it so that the tuple key for this dictionary is the same as the cell's row and col
                j +=1
            i += 1

    def draw(self):
        for cell in self.cells:
            cell.draw()

    def select(self, row, col):
        previous_cell = self.selected_cell
        previous_cell.is_Selected = False
        self.selected_cell = self.cells[row, col]
        self.selected_cell.is_Selected = True

    def click(self, x, y):
        # col_value = x * ??
        # col_value = y * ??
        # select(row_value, col_value)
        pass


    def clear(self):
        self.selected_cell.set_cell_value(0)


    def sketch(self, value):
        self.selected_cell.set_sketched_value(value)


    def place_number(self, value):
        self.selected_cell.set_cell_value_value(self.selected_cell.sketched_value)


    def reset_to_original(self, sudoku):
        for cell in self.cells:
            cell.set_cell_value = sudoku[cell.row][cell.col]
            # row and col might have to be reversed ^^^^

    def is_full(self):
        num_empty_cells = 0
        for cell in self.cells:
            if cell.value != 0:
                num_empty_cells += 1
        if num_empty_cells == 0:
            return True
        else:
            return False

    def update_board(self):
        # I do not understand what this is or why we need it
        pass

    def find_empty(self):
        empty_cells = []
        for cell in self.cells:
            if cell.value == 0:
                empty_cells.append(cell)
        return empty_cells[random.randint(0, len(empty_cells)-1)]

    def check_board(self):
        # I don't get this either
        pass


def main():
    pass


if __name__ == "__main__":
    main()