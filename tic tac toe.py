def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_win(board, player):
    # Rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or \
           board[0][2] == board[1][1] == board[2][0] == player
def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    while moves < 9:
        print_board(board)
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter col (0-2): "))
        except:
            print("Invalid input!")
            continue
        if board[row][col] != " ":
            print("Cell already taken!")
            continue
        board[row][col] = player
        moves += 1
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
        player = "O" if player == "X" else "X"
    print_board(board)
    print("It's a draw!")
tic_tac_toe()
