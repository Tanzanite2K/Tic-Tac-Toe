def print_board(board):
    for row in board:
        print("|".join(cell or " " for cell in row))
        print("-" * 5)

def check_winner(board):
    lines = board + list(map(list, zip(*board))) + [
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)]
    ]
    for line in lines:
        if all(cell == "X" for cell in line):
            return "X"
        elif all(cell == "O" for cell in line):
            return "O"
    if all(cell != "" for row in board for cell in row):
        return "draw"
    return None

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]

def best_move(board, ai_symbol, player_symbol):
    def minimax(board, is_max):
        result = check_winner(board)
        if result == ai_symbol:
            return 1
        elif result == player_symbol:
            return -1
        elif result == "draw":
            return 0

        if is_max:
            best = -float("inf")
            for i, j in get_available_moves(board):
                board[i][j] = ai_symbol
                score = minimax(board, False)
                board[i][j] = ""
                best = max(score, best)
            return best
        else:
            best = float("inf")
            for i, j in get_available_moves(board):
                board[i][j] = player_symbol
                score = minimax(board, True)
                board[i][j] = ""
                best = min(score, best)
            return best

    best_score = -float("inf")
    move = None
    for i, j in get_available_moves(board):
        board[i][j] = ai_symbol
        score = minimax(board, False)
        board[i][j] = ""
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def main():
    board = [["" for _ in range(3)] for _ in range(3)]
    ai_symbol = "X"
    player_symbol = "O"

    print("Welcome to Tic-Tac-Toe!")
    print("You are O, AI is X.")
    print_board(board)

    while True:
        # Player move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if (0 <= row <= 2) and (0 <= col <= 2) and board[row][col] == "":
                    board[row][col] = player_symbol
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter numbers only.")

        print("\nAfter your move:")
        print_board(board)
        winner = check_winner(board)
        if winner:
            break

        # AI move
        move = best_move(board, ai_symbol, player_symbol)
        if move:
            i, j = move
            board[i][j] = ai_symbol

        print("\nAfter AI move:")
        print_board(board)
        winner = check_winner(board)
        if winner:
            break

    if winner == "draw":
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

if __name__ == "__main__":
    main()
