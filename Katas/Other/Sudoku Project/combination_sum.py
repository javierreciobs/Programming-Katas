# KATA: Combination Sum
#
# Dada una lista de números y un objetivo,
# devuelve la primera combinación que sume exactamente el objetivo.
# Ojo sin repetir el mismo elemento de la lista de números.
# Si no existe, devuelve None.
#
# combination_sum([2, 3, 5], 8) == [3, 5]
# combination_sum([2, 3, 5], 11) == None

def combination_sum(numbers, target, current = []):
    if target == 0:
        return current
    if target < 0:
        return None
    for n in numbers:
        result = combination_sum(numbers[n+1:], target - n, current + [n])
        if result is not None:
            return result
        