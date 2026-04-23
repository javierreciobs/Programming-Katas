# KATA: Sudoku Board Validator
#
# Recibe una matriz 9x9 y devuelve True si el tablero es válido.
# Un tablero válido tiene todas las filas, columnas y cajas 3x3 correctas.
# Cada una debe contener los números del 1 al 9 sin repetir.
#
# is_valid_board(valid_matrix) == True
# is_valid_board(invalid_matrix) == False

from sudoku_box_validator import sudoku_box_validator
from sudoku_column_validator import sudoku_column_validator
from sudoku_row_validator import sudoku_row_validator

def sudoku_board_validator(matrix):
    return (
        all(sudoku_row_validator(row) for row in matrix) and
        all(sudoku_column_validator(matrix, c) for c in range(9)) and
        all(sudoku_box_validator([row[c:c+3] for row in matrix[r:r+3]])
            for r in range(0, 9, 3) for c in range(0, 9, 3))
    )