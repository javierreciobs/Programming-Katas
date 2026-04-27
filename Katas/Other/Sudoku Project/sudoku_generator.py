from sudoku_box_validator import sudoku_box_validator
from sudoku_row_validator import sudoku_row_validator
from sudoku_column_validator import sudoku_column_validator

def solve(board, row, col):
    if row == 9:
        return True  
    if col == 9:
        return solve(board, row + 1, 0)
    for n in range(1, 10):
        if is_valid_move(board, row, col, n):
            board[row][col] = n
            if solve(board, row, col + 1):
                return True
            board[row][col] = 0
    return False

def is_valid_move(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    r = (row // 3) * 3
    c = (col // 3) * 3
    box = [board[br][bc] for br in range(r, r+3) for bc in range(c, c+3)]
    if num in box:
        return False
    return True

def sudoku_generator():
    board = [[0] * 9 for _ in range(9)]
    solve(board, 0, 0)
    return board

print(sudoku_generator())