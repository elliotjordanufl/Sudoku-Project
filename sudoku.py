class Cell:
    def __int__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.is_selected = False


    def set_cell_value(self, value):
        self.value = value


    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        if self.value == 0:
            draw_value = False
        else:
            draw_value = True


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # thought this should be called in updateBoard
        # but updateBoard is phrased to update the underlying list instead of the board??
        self.cells = []
        i = 0
        while i < width:
            j = 0
            new_col = []
            while j < height:
                new_cell = Cell(0, j, i, self.screen)
                new_col.append(new_cell)
                j += 1
            self.cells.append(new_col)
            i += 1

    def draw(self):
        pass

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()