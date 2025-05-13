def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
def solve_n_queens(n, row=0, board=[], solutions=[]):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_n_queens(n, row + 1, board, solutions)
            board.pop()
    return solutions
solutions = solve_n_queens(8)
print(f"Total solutions: {len(solutions)}")
for i in range(8):
    row = ['.']*8
    row[solutions[0][i]] = 'Q'
    print(' '.join(row))
