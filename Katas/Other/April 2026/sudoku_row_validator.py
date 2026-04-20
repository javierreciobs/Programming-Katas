# KATA: Sudoku Row Validator
#
# Dada una lista de 9 números, determina si es una fila válida de sudoku.
# Una fila válida contiene exactamente los números del 1 al 9 sin repetir.
#
# valid_row([1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
# valid_row([9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
# valid_row([1, 2, 3, 4, 5, 6, 7, 8, 8]) == False
# valid_row([0, 2, 3, 4, 5, 6, 7, 8, 9]) == False
# valid_row([1, 2, 3, 4, 5, 6, 7, 8]) == False

def sudoku_row_validator(row):
    return set(row) == set(range(1, 10)) and len(row) == 9

