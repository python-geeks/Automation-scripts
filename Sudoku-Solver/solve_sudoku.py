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
    print("\nSoltion is:")
    print_board()    # calls the print_board function
    # if user presses enter then function is called again
    input("Check for more solution?")
# takes each line of the sudoku as input with spaces between two numbers


grid = [list(map(int, input().split()))[:9] for _ in range(9)]


solve_sudoku()  # calls the solve function
