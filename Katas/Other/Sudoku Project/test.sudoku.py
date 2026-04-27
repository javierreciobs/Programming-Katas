from sudoku_board_validator import sudoku_board_validator
from sudoku_generator import sudoku_generator

def test_generates_valid_board():
    board = sudoku_generator()
    assert sudoku_board_validator(board) == True

