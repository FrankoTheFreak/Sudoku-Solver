
# Packages
import pygame
import sys
import copy


# initailise font
pygame.font.init()


# Parameters
WIDTH = HEIGHT = 550
BGCLR = (248, 249, 250)
BORDERCLR = (52, 58, 64)
LINECLR = (222, 226, 230)
FONT = pygame.font.SysFont('Bahnschrift', 30)
OGVALUES = (52, 58, 64)
CPVALUES = (173, 181, 189)


# Initial state of sudoku board
grid = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]


# Creating a copy of original grid
grid_original = copy.deepcopy(grid)


def empty(grid):
    """
    desc >>
        : finds an empty slot in the sudoku
    returns >>
        : for an empty slot returns its row, col in grid
        : otherwise for no empty slots it returns False
    """

    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 0:
                return r, c

    return False


def valid(grid, num, row, col):
    """
    desc >>
        : checks for all the conditions (row, col & square)
    returns >>
        : if all conditions are satisfied it returns True
        : if any one condition is unsatisfied it returns False
    """

    # row check
    for c in range(len(grid)):
        if grid[row][c] == num:
            return False

    # col check
    for r in range(len(grid)):
        if grid[r][col] == num:
            return False

    # square check
    x = (row // 3) * 3
    y = (col // 3) * 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if grid[i][j] == num:
                return False

    return True


def solve(grid, win):
    """
    desc >>
        : uses recursion and backtracking to solve sudoku
    returns >>
        : updates values on the sudoku GUI
        : returns True if sudoku is solved
        : returns False if sudoku is unsolved
    """

    if empty(grid) == False:
        return True
    else:
        row, col = empty(grid)

    for num in range(1, 10):
        if valid(grid, num, row, col):
            grid[row][col] = num
            value = FONT.render(str(num), True, CPVALUES)
            win.blit(value, ((50 * col + 55 + 12), (50 * row + 57)))
            pygame.display.update()
            pygame.time.delay(30)

            if solve(grid, win):
                return True

            grid[row][col] = 0
            pygame.draw.rect(
                win, BGCLR, (50 * col + 55, 50 * row + 55, 40, 40))
            pygame.display.update()

    return False


def main():
    """
    desc >>
        : initialises pygame
        : creates sudoku GUI
        : calls necessary functions to solve sudoku
    """

    # initialise pygame
    pygame.init()

    # sudoku board
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    win.fill((BGCLR))

    # draws grids lines on board GUI
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(win, BORDERCLR, (50 + 50 * i, 50),
                             (50 + 50 * i, 500), 3)
            pygame.draw.line(win, BORDERCLR, (50, 50 + 50 * i),
                             (500, 50 + 50 * i), 3)
        else:
            pygame.draw.line(win, LINECLR, (50 + 50 * i, 50),
                             (50 + 50 * i, 500), 2)
            pygame.draw.line(win, LINECLR, (50, 50 + 50 * i),
                             (500, 50 + 50 * i), 2)

    # place initial values on the board GUI
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                value = FONT.render(str(grid[i][j]), True, BGCLR)
                win.blit(value, ((j + 1.15) * 50 + 10, (i + 1.15) * 50))
            else:
                value = FONT.render(str(grid[i][j]), True, OGVALUES)
                win.blit(value, ((j + 1.15) * 50 + 10, (i + 1.15) * 50))

    pygame.display.update()

    while True:

        for event in pygame.event.get():

            # press [SPACE] to solve sudoku
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if solve(grid, win) == True:
                        break

            # click on 'X' at top right or 'Q' on keyboard to quit
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()


main()
