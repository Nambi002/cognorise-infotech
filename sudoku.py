# Function to check if a number can be placed in the given position
def is_valid(board, row, col, num):
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False
    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

# Backtracking function to solve the Sudoku
def solve_sudoku(board):
    # Find the first empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                # Try numbers 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        # Recursively attempt to solve the rest of the board
                        if solve_sudoku(board):
                            return True
                        # Backtrack if the number didn't lead to a solution
                        board[row][col] = 0
                return False  # No valid number found, trigger backtracking
    return True  # All cells are filled, puzzle solved

# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Sudoku Puzzle:")
print_board(sudoku_board)

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Puzzle:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists.")
