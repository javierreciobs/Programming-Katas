# KATA: Sudoku Box Validator
#
# Dada una caja 3x3 del sudoku (lista de 3 listas de 3 elementos),
# determina si es válida. Una caja válida contiene exactamente
# los números del 1 al 9 sin repetir.
#
# is_valid_box([[1,2,3],[4,5,6],[7,8,9]]) == True
# is_valid_box([[1,1,3],[4,5,6],[7,8,9]]) == False
# is_valid_box([[1,2,3],[4,5,6],[7,8,0]]) == False
# is_valid_box([[1,2,3],[4,5,6],[7,8,9]]) == True
# is_valid_box([[3,1,2],[6,4,5],[9,7,8]]) == True
# is_valid_box([[9,8,7],[6,5,4],[3,2,1]]) == True

def sudoku_box_validator(box):
    result = []
    for n in box:
        result.extend(n)
    return set(result) == set(range(1, 10)) and len(result) == 9

#Senior version

def senior_sudoku_box_validator(senior_box):
    return set([n for row in senior_box for n in row]) == set(range(1, 10))
