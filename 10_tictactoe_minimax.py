"""Practical 10: Tic-Tac-Toe game-playing agent using Minimax.

Human plays X; the computer plays O. Minimax tries every possible future
move, assigns +1 to an AI win, -1 to a human win, and 0 to a draw. The AI
chooses the move with the highest score. With this scoring, the AI should not
lose when it plays correctly.

Run: python 10_tictactoe_minimax.py
Enter board positions 1-9 as shown on screen.
"""

HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    """Display the 3x3 board with grid lines."""
    print("\n-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")


def check_winner(board):
    """Return X or O if that player has a line; otherwise return None."""
    # Check horizontal rows.
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    # Check vertical columns.
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    # Check both diagonals.
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def is_moves_left(board):
    """Return True if at least one empty square remains."""
    return any(EMPTY in row for row in board)


def minimax(board, is_maximizing):
    """Evaluate the board assuming both players choose their best moves."""
    winner = check_winner(board)
    if winner == AI:
        return 1
    if winner == HUMAN:
        return -1
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI  # Try an AI move.
                    score = minimax(board, False)
                    board[i][j] = EMPTY  # Undo the trial move.
                    best_score = max(best_score, score)
        return best_score

    best_score = float("inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = HUMAN  # Try the human's best reply.
                score = minimax(board, True)
                board[i][j] = EMPTY  # Undo the trial move.
                best_score = min(best_score, score)
    return best_score


def find_best_move(board):
    """Return the (row, column) of the highest-scoring AI move."""
    best_score = -float("inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def human_move(board):
    """Read a valid, unoccupied board position from the human player."""
    while True:
        try:
            position = int(input("Enter your position (1-9): "))
            if not 1 <= position <= 9:
                print("Please enter a number from 1 to 9.")
                continue
            row, col = divmod(position - 1, 3)
            if board[row][col] != EMPTY:
                print("Position already occupied. Try again.")
                continue
            board[row][col] = HUMAN
            return
        except ValueError:
            print("Please enter a valid number.")


def play_game():
    """Alternate human and AI turns until someone wins or the board is full."""
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("\n===== TIC-TAC-TOE =====")
    print("You are X")
    print("AI is O")
    print("\nBoard positions:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    while True:
        human_move(board)
        print_board(board)
        if check_winner(board) == HUMAN:
            print("Congratulations! You win.")
            break
        if not is_moves_left(board):
            print("Game Draw!")
            break

        print("\nAI is thinking...")
        move = find_best_move(board)
        if move is not None:
            board[move[0]][move[1]] = AI
        print_board(board)
        if check_winner(board) == AI:
            print("AI wins!")
            break
        if not is_moves_left(board):
            print("Game Draw!")
            break


if __name__ == "__main__":
    play_game()
