#! python3
# sudoku_recursion_solver.py - solves the Sudoku 9x9 square with
# recursion method.

# grid variable represents Sudoku cell where zeros stand for emty square.
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 4, 7, 0, 0, 2, 0],
        [0, 1, 9, 5, 0, 8, 6, 4, 7],
        [0, 6, 0, 9, 0, 0, 0, 0, 4],
        [3, 4, 2, 6, 8, 0, 0, 0, 0],
        [0, 9, 0, 0, 5, 0, 8, 3, 0],
        [0, 0, 0, 7, 2, 0, 0, 0, 3],
        [0, 0, 6, 0, 0, 5, 0, 1, 0],
        [0, 0, 3, 8, 9, 0, 0, 0, 0]]



def is_possible(grid, y, x, num):
    '''Checks if a number from 1 to 9 can be inserted. 
       If not return False'''

    # Check row
    for i in range(9):
        if grid[y][i] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][x] == num:
            return False

    # Check 3x3 square
    # But first need to find its row and column indexes 
    # y_pos and x_pos are the first indexes of [0, 1, 2]
    # or [3, 4, 5] or [6, 7, 8] lists.
    y_pos = (y // 3) * 3
    x_pos = (x // 3) * 3
    for i in range(y_pos, y_pos + 3):
        for j in range(x_pos, x_pos + 3):
            if grid [i][j] == num:
                return False

    return True


def print_grid(grid):
    ''' Displays Sudoku on the screen '''
    for y in range(9):
        if y % 3 == 0 and y != 0:
            print("- - - - - - - - - - - - - ")

        for x in range(9):
            if x % 3 == 0 and x != 0:
                print(" | ", end="")

            if x == 8:
                print(grid[y][x])
            else:
                print(str(grid[y][x]) + " ", end="")


def solve(grid):
    # In this algorithm, if a 1x1 square has more than 1 possible value,
    # then the function will iterate over all of them. If, after
    # choosing some value, a collision occurs, then the recursion will
    # return to the place where the wrong value has been inserted and then
    # choose the next possible value for this 1x1 square. If there's more
    # than one solution the program will show them all.

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(grid, y, x, n):
                        grid[y][x] = n
                        solve(grid)
                        grid[y][x] = 0
                return
    print_grid(grid)
    input('More?')
    

solve(grid)