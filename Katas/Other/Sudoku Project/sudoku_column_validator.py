# KATA: Sudoku Column Validator
#
# Recibe una matriz 9x9 y un índice de columna.
# Devuelve True si la columna contiene los números del 1 al 9 sin repetir.
#
# is_valid_column(matrix, 0) == True
# is_valid_column(matrix, 0) == False  (si hay duplicados o falta algún número)

matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 9],
]

def sudoku_column_validator(matrix, column_index):
    return set(range(1, 10)) ==  set([row[column_index] for row in matrix])
    
   
