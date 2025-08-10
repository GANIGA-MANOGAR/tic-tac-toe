import math

# Board positions
board = [" " for _ in range(9)]  # 3x3 board as 1D list

# Print the board
def print_board():
    print("\n")
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print("\n")

# Check for empty spots
def empty_indices(board):
    return [i for i, x in enumerate(board) if x == " "]

# Check for win
def check_winner(b, player):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diagonals
    ]
    for state in win_states:
        if b[state[0]] == b[state[1]] == b[state[2]] == player:
            return True
    return False

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif " " not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in empty_indices(board):
            board[i] = "O"
            score = minimax(board, depth + 1, False)
            board[i] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in empty_indices(board):
            board[i] = "X"
            score = minimax(board, depth + 1, True)
            board[i] = " "
            best_score = min(score, best_score)
        return best_score

# Get the best move for AI
def best_move():
    best_score = -math.inf
    move = 0
    for i in empty_indices(board):
        board[i] = "O"
        score = minimax(board, 0, False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    return move

# Main game loop
def play():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', AI is 'O'. Position numbers: 1 to 9")
    print_board()

    while True:
        # Human move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != " ":
                print("Spot already taken!")
                continue
            board[move] = "X"
        except (ValueError, IndexError):
            print("Invalid input! Try again.")
            continue

        print_board()

        if check_winner(board, "X"):
            print("You win! 🎉")
            break
        elif " " not in board:
            print("It's a tie!")
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = "O"
        print("AI has moved:")
        print_board()

        if check_winner(board, "O"):
            print("AI wins! 🤖")
            break
        elif " " not in board:
            print("It's a tie!")
            break

# Run the game
play()
