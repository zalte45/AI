"""Practical 8: 8-Queens problem using backtracking.

Place 8 queens on an 8x8 chessboard so that no two queens share a column or
diagonal. The algorithm places one queen per row, tests whether a position is
safe, and backtracks if a later row has no safe position.

Run: python 08_eight_queens_backtracking.py
"""

N = 8


def print_board(board):
    """Display queens as Q and empty squares as dots."""
    print("\nSolution:")
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))


def is_safe(board, row, col):
    """Check the column and both upward diagonals before placing a queen."""
    # Only earlier rows need checking because queens are placed top to bottom.
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal.
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper-right diagonal.
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row):
    """Return True when a valid placement for all rows has been found."""
    if row == N:  # All eight queens have been placed safely.
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Try putting a queen in this square.
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0  # Undo the move and try the next column.

    return False


if __name__ == "__main__":
    board = [[0 for _ in range(N)] for _ in range(N)]
    if solve_n_queens(board, 0):
        print_board(board)
    else:
        print("No solution exists.")
