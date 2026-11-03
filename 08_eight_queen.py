# Size of the chessboard (8 x 8)
N = 8


# Function to print the chessboard
def print_board(board):

    # Print heading
    print("\nSolution:")

    # Traverse each row of the board
    for row in board:

        # Print Q for queen and . for empty cell
        print(" ".join("Q" if cell == 1 else "." for cell in row))


# Function to check whether placing a queen is safe
def is_safe(board, row, col):

    # Check the same column in previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False  # Queen already exists in this column

    # Check the upper-left diagonal
    i, j = row - 1, col - 1

    # Continue until the boundary of the board
    while i >= 0 and j >= 0:

        # If another queen is found, position is unsafe
        if board[i][j] == 1:
            return False

        # Move diagonally upward-left
        i -= 1
        j -= 1

    # Check the upper-right diagonal
    i, j = row - 1, col + 1

    # Continue until the boundary of the board
    while i >= 0 and j < N:

        # If another queen is found, position is unsafe
        if board[i][j] == 1:
            return False

        # Move diagonally upward-right
        i -= 1
        j += 1

    # If no queen attacks this position, it is safe
    return True


# Function to solve the 8 Queens problem using backtracking
def solve_n_queens(board, row):

    # Base condition: all 8 queens are placed
    if row == N:
        return True

    # Try placing a queen in every column of the current row
    for col in range(N):

        # Check whether the current position is safe
        if is_safe(board, row, col):

            # Place the queen in the current position
            board[row][col] = 1

            # Recursively solve the next row
            if solve_n_queens(board, row + 1):
                return True

            # Backtrack: remove the queen if solution fails
            board[row][col] = 0

    # No valid position found in this row
    return False


# Main program
if __name__ == "__main__":

    # Create an 8 x 8 chessboard filled with zeros
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Start solving from the first row (row 0)
    if solve_n_queens(board, 0):

        # If solution is found, print the board
        print_board(board)

    else:

        # If no solution is found
        print("No solution exists.")
