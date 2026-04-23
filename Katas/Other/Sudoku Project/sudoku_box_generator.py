# KATA: Sudoku Box Generator
#
# Genera una matriz de 3x3 con los números del 1 al 9 
# distribuidos aleatoriamente.
#
# generate_random_box() == [[3, 1, 9], [4, 8, 2], [7, 6, 5]] (por ejemplo)

import random

def sudoku_box_generator():
    sudoku_numbers = random.sample(range(1, 10), 9)
    row1 = sudoku_numbers[0:3]
    row2 = sudoku_numbers[3:6]
    row3 = sudoku_numbers[6:9]
    return [row1, row2, row3]