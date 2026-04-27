# KATA: Find Path
#
# Dada una lista de números del 1 al N desordenados,
# encuentra el primer número que cumple una condición usando backtracking.
# Si no existe, devuelve None.
#
# find_path([3, 1, 4, 2], lambda x: x > 3) == 4
# find_path([3, 1, 4, 2], lambda x: x > 10) == None

def find_path(numbers, condition):
    for n in numbers:
        if condition(n):
            return n
    return None
