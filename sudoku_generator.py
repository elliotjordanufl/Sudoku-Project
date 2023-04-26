import math, random
import sys, pygame
from sudoku import Board


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = math.sqrt(row_length)
        self.board = self.initialize_board()

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board

    def initialize_board(self):
        # this is a placeholder list of lists
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        return board

    def print_board(self):
        for i in range(0, len(self.board)):
            print(self.board[i])

    def valid_in_row(self, row, num):
        if num in self.board[row]:
            return False
        else:
            return True

    def valid_in_col(self, col, num):
        for i in range(0, 9):
            if num == self.board[i][int(col)]:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        i = row_start
        while i <= row_start + 2:
            j = col_start
            while j <= col_start + 2:
                if self.board[i][int(j)] == num:
                    return False
                j += 1
            i += 1
        return True

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3, col - col % 3, num):
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        unused_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        i = row_start
        while i <= row_start + 2:
            j = col_start
            while j <= col_start + 2:
                num_to_add = unused_numbers.pop(random.randint(0, len(unused_numbers) - 1))
                self.board[i][j] = num_to_add
                j += 1
            i += 1

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):

        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
            #finishes the row and moves on to the next one below it
        if row >= self.row_length and col >= self.row_length:
            return True
            #finished checking board
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
            #checks if in first box and shifts to upper middle box
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
                self.board[row][int(col)] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][int(col)] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, int(self.box_length))

    def remove_cells(self):
        while self.removed_cells > 0:
            rand_col = random.randint(0, self.row_length-1)
            rand_row = random.randint(0, self.row_length-1)
            cell_to_remove = self.board[rand_col][rand_row]
            if cell_to_remove != 0:
                self.board[rand_col][rand_row] = 0
                self.removed_cells -= 1

    def print_numbers(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board[i][j] != 0:
                    this_cell = this_board.cells[j, i]
                    this_cell.value = self.board[i][j]
                    this_cell.is_editable = False
                    screen.blit(myfont2.render(f'{self.board[i][j]}', True, black), (45*i + 209.5, 45*j + 28))
    def print_numbers_2(self):
        for i in range(0, 9):
            for j in range(0, 9):
                this_cell = this_board.cells[j,i]
                if not this_cell.is_editable:
                    screen.blit(myfont2.render(f'{self.board[i][j]}', True, black), (45 * i + 209.5, 45 * j + 28))
                elif not this_cell.value == 0:
                    screen.blit(myfont2.render(f'{this_cell.value}', True, black), (45*i + 209.5, 45*j + 28))

def generate_sudoku(size, removed):
    global sudoku
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

pygame.init()

def intro_screen():
    text = myfont.render('Welcome to Sudoku', True, black)
    text1 = myfont1.render('Select Game Mode:', True, black)
    text_option1 = myfont2.render('Easy', True, black)
    text_option2 = myfont2.render('Medium', True, black)
    text_option3 = myfont2.render('Hard', True, black)


    screen.fill(black)
    screen.blit(background, (0, 0))
    screen.blit(text, (123.5, 60))
    screen.blit(text1, (197.5, 200))
    pygame.draw.rect(screen, yellow, (195, 400, 53, 35))
    screen.blit(text_option1, (200, 400))
    pygame.draw.rect(screen, yellow, (358.5, 400, 83, 35))
    screen.blit(text_option2, (363.5, 400))
    pygame.draw.rect(screen, yellow, (545, 400, 60, 35))
    screen.blit(text_option3, (550, 400))


def puzzle_screen():
    screen.fill(black)
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, yellow, (197.5, 28, 405, 405))
    pygame.draw.rect(screen, black, (197.5, 28, 405, 405), 5)
    pygame.draw.rect(screen, black, (332.5, 28, 5, 405))
    pygame.draw.rect(screen, black, (467.5, 28, 5, 405))
    pygame.draw.rect(screen, black, (197.5, 163, 405, 5))
    pygame.draw.rect(screen, black, (197.5, 298, 405, 5))
    #smaller boundaries
    for i in range(0, 9):
        pygame.draw.rect(screen, black, (197.5, 73 + 45*i, 405, 2.5))

    for i in range(0, 9):
        pygame.draw.rect(screen, black, (242.5 + 45*i, 28, 2.5, 405))

    button_text1 = myfont2.render('Reset', True, black)
    button_text2 = myfont2.render('Restart', True, black)
    button_text3 = myfont2.render('Exit', True, black)

    pygame.draw.rect(screen, yellow, (195, 450, 65, 35))
    screen.blit(button_text1, (200, 450))
    pygame.draw.rect(screen, yellow, (358.5, 450, 83, 35))
    screen.blit(button_text2, (363.5, 450))
    pygame.draw.rect(screen, yellow, (545, 450, 65, 35))
    screen.blit(button_text3, (550, 450))


size = width, height = 800, 533
black = 0, 0, 0
white = 255, 255, 255
yellow = 250, 221, 2
red = 255, 0, 0
gray = 112, 115, 113


screen = pygame.display.set_mode(size)

background = pygame.image.load("sudoku-background.jpg")

myfont = pygame.font.SysFont('Comic Sans', 60)
myfont1 = pygame.font.SysFont('Comic Sans', 45)
myfont2 = pygame.font.SysFont('Comic Sans', 20)


intro_screen()
intro = True


def selection_check():
    puzzle_screen()
    sudoku.print_numbers_2()
    if selection:
        pygame.draw.rect(screen, red, pygame.Rect(45 * col + 197.5, 45 * row + 28, 45, 45), 5)


# defining this variable outside to make sure is accessible
selection = False
# this as a placeholder
this_board = Board(9, 9, screen, "easy")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and intro:
            x, y = event.pos
            if 400 <= y <= 435:
                if 195 <= x <= 248:
                    difficulty = "easy"
                    this_board = Board(9, 9, screen, difficulty)
                    generate_sudoku(9, 30)
                    this_board.set_up_cells(sudoku)
                    puzzle_screen()
                    sudoku.print_numbers()
                    intro = False
                elif 358.5 <= x <= 441.5:
                    difficulty = "medium"
                    this_board = Board(9, 9, screen, difficulty)
                    generate_sudoku(9, 40)
                    this_board.set_up_cells(sudoku)
                    puzzle_screen()
                    sudoku.print_numbers()
                    intro = False
                elif 545 <= x <= 605:
                    difficulty = "hard"
                    this_board = Board(9, 9, screen, difficulty)
                    generate_sudoku(9, 50)
                    this_board.set_up_cells(sudoku)
                    puzzle_screen()
                    sudoku.print_numbers()
                    intro = False
        if event.type == pygame.MOUSEBUTTONDOWN and not intro:
            x, y = event.pos
            selection = False
            if 209.5 <= x <= 614.5 and 28 <= y <= 433:
                for i in range(0, 9):
                    for j in range(0, 9):
                        if (45*i + 209.5) <= x <= (45*(i+1) + 209.5):
                            col = i
                        if (45*j + 28) <= y <= (45*(j+1) + 28):
                            row = j
                this_board.click(x,y)
                if sudoku.get_board()[col][row] == 0:
                    selection = True
            elif 450 <= y <= 485:
                if 195 <= x <= 260:
                    print("Reset")
                    selection = False
                    this_board.clear_whole_board()
                    selection_check()
                elif 358 <= x <= 441:
                    print("Restart")
                    selection = False
                    this_board.clear_whole_board()
                    selection_check()
                    this_board = Board(9, 9, screen, difficulty)
                    generate_sudoku(9, 30)
                    this_board.set_up_cells(sudoku)
                    puzzle_screen()
                    sudoku.print_numbers()
                elif 545 <= x <= 610:
                    quit()

        if selection:
            selection_check()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    screen.blit(myfont2.render('1', True, gray), (45 * col + 197.5, 45 * row + 28))
                    print('1')
                    #sudoku.get_board()[col][row] = 1
                    this_board.place_number(1)
                elif event.key == pygame.K_2:
                    screen.blit(myfont2.render('2', True, gray), (45 * col + 197.5, 45 * row + 28))
                    print('2')
                    this_board.selected_cell.set_cell_value = 2
                elif event.key == pygame.K_3:
                    screen.blit(myfont2.render('3', True, gray), (45 * col + 197.5, 45 * row + 28))
                    this_board.selected_cell.set_cell_value = 3
                elif event.key == pygame.K_4:
                    screen.blit(myfont2.render('4', True, gray), (45 * col + 197.5, 45 * row + 28))
                    this_board.selected_cell.set_cell_value = 4
                elif event.key == pygame.K_5:
                    screen.blit(myfont2.render('5', True, gray), (45 * col + 197.5, 45 * row + 28))
                    this_board.selected_cell.set_cell_value = 5
                elif event.key == pygame.K_6:
                    screen.blit(myfont2.render('6', True, gray), (45 * col + 197.5, 45 * row + 28))
                    this_board.selected_cell.set_cell_value = 6
                elif event.key == pygame.K_7:
                    screen.blit(myfont2.render('7', True, gray), (45 * col + 197.5, 45 * row + 28))
                    this_board.selected_cell.set_cell_value = 7
                elif event.key == pygame.K_8:
                    screen.blit(myfont2.render('8', True, gray), (45 * col + 197.5, 45 * row + 28))
                    this_board.selected_cell.set_cell_value = 8
                elif event.key == pygame.K_9:
                    screen.blit(myfont2.render('9', True, gray), (45 * col + 197.5, 45 * row + 28))
                    this_board.selected_cell.set_cell_value = 9
                selection_check()
                print(selection)


    pygame.display.flip()



