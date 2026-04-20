# KATA: Matrix Transpose
#
# Dada una matriz (lista de listas), devuelve su transpuesta.
# La transpuesta convierte filas en columnas y columnas en filas.
#
# transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
# transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
# transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
# transpose([]) == []

def matrix_transpose(matrix):
    if not matrix:
        return []
    result = []
    for i in range(len(matrix[0])):  #Iterate colummns
        row = []                     #Create a new list per column                          
        for j in range(len(matrix)): #Iterate rows
            row.append(matrix[j][i])
        result.append(row)
    return result

def senior_matrix_transpose(senior_matrix):
    return [list(row) for row in zip(*senior_matrix)]


