import math


def print_board(board):
    """Display the current game board."""
  
    for row in board:
        print(" | ".join(row))
        print("---------")


def is_moves_left(board):
    """Check if there are moves left on the board."""
  
    return any(cell == ' ' for row in board for cell in row)


def evaluate(board):
    """Evaluate board state:
       +10 for AI win, -10 for human win, 0 otherwise."""
  
    # Check rows and columns
    for i in range(3):
        # Rows
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return 10 if board[i][0] == 'O' else -10
        # Columns
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return 10 if board[0][i] == 'O' else -10

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return 10 if board[0][0] == 'O' else -10
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return 10 if board[0][2] == 'O' else -10

    # No winner
    return 0


def minimax(board, depth, is_maximizing):
    """Minimax recursive algorithm."""
  
    score = evaluate(board)

    # If AI has won
    if score == 10:
        return score - depth  # Prefer faster wins
    # If human has won
    if score == -10:
        return score + depth  # Prefer slower losses
    # If no moves and no winner
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    value = minimax(board, depth + 1, False)
                    best = max(best, value)
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    value = minimax(board, depth + 1, True)
                    best = min(best, value)
                    board[i][j] = ' '
        return best


def find_best_move(board):
    """Find the best move for the AI ('O')."""
  
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move


def check_winner(board):
    """Return the winner ('X' or 'O') or None if no winner yet."""
  
    # Reuse evaluation logic
    score = evaluate(board)
    if score == 10:
        return 'O'
    elif score == -10:
        return 'X'
    return None


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Human starts

    print("Welcome to Tic-Tac-Toe! You are 'X'. AI is 'O'.")
    print_board(board)

    while is_moves_left(board) and not check_winner(board):
        if current_player == 'X':
            print("Your turn. Enter row and column (0, 1, or 2) separated by space:")
            try:
                row, col = map(int, input().split())
                if board[row][col] != ' ':
                    print("Cell already taken! Try again.")
                    continue
                board[row][col] = 'X'
            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers between 0 and 2.")
                continue
        else:
            print("AI is thinking...")
            row, col = find_best_move(board)
            board[row][col] = 'O'
            print(f"AI placed 'O' at ({row}, {col})")

        print_board(board)
        current_player = 'O' if current_player == 'X' else 'X'

    winner = check_winner(board)
    if winner:
        print(f"Game over! {winner} wins!")
    else:
        print("Game over! It's a draw.")

if __name__ == '__main__':
    main()
