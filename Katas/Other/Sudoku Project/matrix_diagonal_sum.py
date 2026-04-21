# KATA: Matrix Diagonal Sum
#
# Dada una matriz cuadrada (NxN), devuelve la suma de los elementos
# de la diagonal principal (de arriba izquierda a abajo derecha).
#
# diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15
# diagonal_sum([[1, 0], [0, 1]]) == 2
# diagonal_sum([[5]]) == 5
# diagonal_sum([]) == 0

def matrix_diagonal_sum(matrix):
    result = 0
    for n in range(len(matrix)):
        result += matrix[n][n]
    return result

#Senior version

def senior_matrix_diagonal_sum(senior_matrix):
    return sum(senior_matrix[n][n] for n in range(len(senior_matrix)))
