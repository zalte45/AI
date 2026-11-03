# Define the symbols used in the game
EMPTY = " "
HUMAN = "X"
AI = "O"


# Function to print the game board
def print_board(board):

    # Print the top grid line
    print("\n-------------")

    # Print each row
    for row in board:

        # Display each cell with grid lines
        print("| " + " | ".join(row) + " |")

        # Print separator line
        print("-------------")


# Function to check whether a player has won
def check_winner(board):

    # Check horizontal rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]  # Return the winning player

    # Check vertical columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    # Check the top-left to bottom-right diagonal
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    # Check the top-right to bottom-left diagonal
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    # Return None if there is no winner
    return None


# Function to check whether empty cells are available
def is_moves_left(board):

    # Return True if any empty cell exists
    return any(EMPTY in row for row in board)


# Minimax algorithm to find the best possible move
def minimax(board, is_maximizing):

    # Check whether the game has a winner
    winner = check_winner(board)

    # AI winning condition
    if winner == AI:
        return 1

    # Human winning condition
    if winner == HUMAN:
        return -1

    # If the board is full, the game is a draw
    if not is_moves_left(board):
        return 0

    # AI tries to get the maximum score
    if is_maximizing:

        # Initialize the best score to negative infinity
        best_score = -float("inf")

        # Traverse all rows
        for i in range(3):

            # Traverse all columns
            for j in range(3):

                # Check whether the cell is empty
                if board[i][j] == EMPTY:

                    # Try placing AI symbol
                    board[i][j] = AI

                    # Recursively evaluate the next move
                    score = minimax(board, False)

                    # Undo the trial move
                    board[i][j] = EMPTY

                    # Update the maximum score
                    best_score = max(best_score, score)

        # Return the best score for AI
        return best_score

    # Human tries to get the minimum score
    best_score = float("inf")

    # Traverse all rows
    for i in range(3):

        # Traverse all columns
        for j in range(3):

            # Check whether the cell is empty
            if board[i][j] == EMPTY:

                # Try placing the human symbol
                board[i][j] = HUMAN

                # Recursively evaluate AI's next move
                score = minimax(board, True)

                # Undo the trial move
                board[i][j] = EMPTY

                # Update the minimum score
                best_score = min(best_score, score)

    # Return the best score for the human
    return best_score


# Function to find the best move for AI
def find_best_move(board):

    # Initialize the best score
    best_score = -float("inf")

    # Store the best position
    best_move = None

    # Traverse all rows
    for i in range(3):

        # Traverse all columns
        for j in range(3):

            # Check for empty cell
            if board[i][j] == EMPTY:

                # Place AI symbol temporarily
                board[i][j] = AI

                # Calculate the score using Minimax
                score = minimax(board, False)

                # Remove the temporary move
                board[i][j] = EMPTY

                # Check if this move gives a better score
                if score > best_score:

                    # Update the best score
                    best_score = score

                    # Store the row and column
                    best_move = (i, j)

    # Return the best position
    return best_move


# Function to take input from the human player
def human_move(board):

    # Repeat until a valid move is entered
    while True:
        try:

            # Get position from the user
            position = int(input("Enter your position (1-9): "))

            # Check whether the position is between 1 and 9
            if not 1 <= position <= 9:
                print("Please enter a number from 1 to 9.")
                continue

            # Convert position into row and column
            row, col = divmod(position - 1, 3)

            # Check whether the position is already occupied
            if board[row][col] != EMPTY:
                print("Position already occupied. Try again.")
                continue

            # Place the human symbol
            board[row][col] = HUMAN

            # End the input function
            return

        # Handle invalid input
        except ValueError:
            print("Please enter a valid number.")


# Function to run the complete game
def play_game():

    # Create an empty 3x3 board
    board = [[EMPTY for _ in range(3)] for _ in range(3)]

    # Display the game title
    print("\n===== TIC-TAC-TOE =====")

    # Display player symbols
    print("You are X")
    print("AI is O")

    # Display position mapping
    print("\nBoard positions:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    # Continue the game until it ends
    while True:

        # Take the human player's move
        human_move(board)

        # Display the board
        print_board(board)

        # Check whether the human wins
        if check_winner(board) == HUMAN:
            print("Congratulations! You win.")
            break

        # Check whether the game is a draw
        if not is_moves_left(board):
            print("Game Draw!")
            break

        # Display AI thinking message
        print("\nAI is thinking...")

        # Find the best move for AI
        move = find_best_move(board)

        # Place AI symbol at the best position
        if move is not None:
            board[move[0]][move[1]] = AI

        # Display the updated board
        print_board(board)

        # Check whether AI wins
        if check_winner(board) == AI:
            print("AI wins!")
            break

        # Check whether the game is a draw
        if not is_moves_left(board):
            print("Game Draw!")
            break


# Main program execution
if __name__ == "__main__":

    # Start the game
    play_game()

