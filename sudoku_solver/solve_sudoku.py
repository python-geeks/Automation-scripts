import random


def is_number_valid(row, col, num):
    # function to find if the number is valid or not in the respective space
    global grid   # making grid as global variable
    for i in range(0, 9):
        # for loop to find if the number is present in the row or not
        if grid[row][i] == num:
            return False
    for i in range(0, 9):
        # for loop to find if the number is present in the column or not
        if grid[i][col] == num:
            return False
    # makes the variables to consider the 3x3 square in the puzzle
    col_subset = (col // 3) * 3
    row_subset = (row // 3) * 3
    for i in range(0, 3):
        # for loop to find if the number is present in square
        for j in range(0, 3):
            if grid[row_subset + i][col_subset + j] == num:
                return False
    return True   # if not preent in the all the possibilities returns True


def print_board():  # function to print the puzzle after solving
    global grid   # global variables
    for i in range(len(grid)):  # for loop to print the board
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def fill(row, col):
    global grid
    if col >= 9 and row < 8:
        row = row + 1
        col = 0
    if row >= 9 and col >= 9:
        return True
    if row < 3:
        if col < 3:
            col = 3
    elif row < 6:
        if col == int(row/3)*3:
            col = col + 3
    else:
        if col == 6:
            row = row + 1
            col = 0

            if row >= 9:
                return True
    for i in range(1, 10):
        if is_number_valid(row, col, i):
            grid[row][col] = i
            if fill(row, col + 1):
                return True
            grid[row][col] = 0
    return False


def generate_sudoku(visible_count):
    # visible_count - count of visible numbers on the grid
    global grid
    grid = []
    for g in range(0, 9):
        grid.append([0]*9)
    # first generate for each 3x3 grid diagnolly

    for i in range(0, 7, 3):
        k = i
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(0, 9):
            rand = random.randint(0, 8 - j)

            if k % 3 == 0:
                k = i

            grid[k][int(j/3) + i] = number_list[rand]
            k = k + 1

            del number_list[rand]

    # fill remaining
    fill(0, 3)

    # remove digits
    # please remember it does not check if sudoku
    # is solvable while removing digits
    hidden_count = 81 - visible_count
    while hidden_count > 0:
        rand_cell = random.randint(1, 81)
        r = int(rand_cell/9) - 1
        c = int(rand_cell % 9) - 1
        if not grid[r][c] == 0:
            grid[r][c] = 0
            hidden_count = hidden_count - 1


def solve_sudoku():
    # function to solve sudoku problem
    global grid
    for row in range(9):
        # for loop to find 0 in the row and column
        for col in range(9):
            if grid[row][col] == 0:
                # gives values to give in the spaces
                for n in range(1, 10):
                    # if the number is valid or not
                    if is_number_valid(row, col, n):
                        # assigns the value
                        grid[row][col] = n
                        # recalls the function
                        solve_sudoku()
                        # if the number is already present then
                        # assign the value 0 to it
                        grid[row][col] = 0
                return
    print("\nSolution is:")
    print_board()    # calls the print_board function
    # if user presses enter then function is called again
    input("Check for more solution?")
# takes each line of the sudoku as input with spaces between two numbers


generate_sudoku(10)
print_board()


solve_sudoku()  # calls the solve function
