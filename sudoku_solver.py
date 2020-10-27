#! python3
# sudoku_solver.py - solves the Sudoku 9x9 square like a real human 
# would, checking for possible value in a 3x3 square, row or column 
# where 1x1 cell belongs.

# grid variable represents Sudoku cell where zeros stand for emty square.
grid = [[0, 0, 0, 0, 0, 0, 0, 8, 0],
        [6, 8, 0, 4, 7, 0, 0, 2, 0],
        [0, 1, 9, 5, 0, 8, 6, 4, 7],
        [0, 6, 0, 9, 0, 0, 0, 0, 4],
        [3, 4, 2, 6, 8, 0, 0, 0, 0],
        [1, 9, 0, 0, 5, 0, 8, 3, 0],
        [0, 0, 0, 7, 2, 0, 4, 0, 3],
        [0, 0, 0, 0, 0, 5, 0, 1, 0],
        [0, 0, 3, 8, 9, 1, 5, 0, 0]]

# Set, which subtracting the values from we will 
# get the set of possible values for each square
subtract_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def print_grid(grid):
    ''' Displays Sudoku on the screen '''
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + ' ', end='')


# check_ functions finds possible values for each 1x1 square 
# (i and j its indexes) in a row, column and 3x3 square.
def check_horizontal(i, j):
    '''Searching for possible values horizontally'''
    return subtract_set - set(grid[i])


def check_vertical(i, j):
    '''Searching for possible values vertically checking each row.'''
    return_set = []
    for n in range(9):
        return_set.append(grid[n][j])
    return subtract_set - set(return_set)


def check_square(i, j):
    '''Searching for possible valuws in the 3x3 square.'''
    
    # Finds the 3x3 square of the selected value and its indexes 
    # ([0, 1, 2] or [3, 4, 5] or [6, 7, 8]).
    first = [0, 1, 2]
    second = [3, 4, 5]
    third = [6, 7, 8]
    find_square = [first, second, third]
    for p in find_square:
        if i in p:
            row = p
        if j in p:
            col = p
    
    # Checks the possible values in the found 3x3 square .
    return_set = []
    for x in row:
        for y in col:
            return_set.append(grid[x][y])
    return subtract_set - set(return_set)


def get_poss_vals(i, j):
    '''Finds the common possible values for 1x1 square, combining founded 
       sets of possible values in a row, column and square'''
    poss_vals = list(check_square(i, j).intersection(check_horizontal(i, j)) \
                                       .intersection(check_vertical(i, j)))
    return poss_vals


def solver(grid):
    '''Main function which will go through each empty 1x1 square and
       finding the only possible value for it until there is more 
       than one empty square'''
    while True:
        zeros = 0
        # i iterates through columns, j through rows
        # zeros - is a number of empty 1x1 squares
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    poss_vals = get_poss_vals(i, j)
                    if len(poss_vals) == 1:
                        grid[i][j] = poss_vals[0]
                    
                if grid[i][j] == 0:
                    zeros += 1
        if zeros == 0:
            return grid


 
grid = solver(grid)
print_grid(grid)
