# Sudoku-Solver

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

  If you want a solution for a sudoku puzzle, it may help you. Give each line of the puzzle as input with zeroes in place of spaces.
  
  This program uses backtracking process to solve. The program finds the zeroes i.e. empty spaces in the line and checks the number in range 9 that it unique in that row , column and square. Like that the code goes on checking each and every space in the puzzle. If any number is repeated inside the row and column, then it is backtrack and changes the number in the respective space. The program uses the recursion to backtrack in the puzzle.
  
  # Input
    7 8 0 4 0 0 1 2 0
    6 0 0 0 7 5 0 0 9
    0 0 0 6 0 1 0 7 8
    0 0 7 0 4 0 2 6 0
    0 0 1 0 5 0 9 3 0
    9 0 4 0 6 0 0 0 5
    0 7 0 3 0 0 0 1 2
    1 2 0 0 0 7 4 0 0
    0 4 9 2 0 6 0 0 7
  
  # Output
    7 8 5  | 4 3 9  | 1 2 6
    6 1 2  | 8 7 5  | 3 4 9
    4 9 3  | 6 2 1  | 5 7 8
    - - - - - - - - - - - - - 
    8 5 7  | 9 4 3  | 2 6 1
    2 6 1  | 7 5 8  | 9 3 4
    9 3 4  | 1 6 2  | 7 8 5
    - - - - - - - - - - - - - 
    5 7 8  | 3 9 4  | 6 1 2
    1 2 6  | 5 8 7  | 4 9 3
    3 4 9  | 2 1 6  | 8 5 7
    Check for more solution?
  Thank you
