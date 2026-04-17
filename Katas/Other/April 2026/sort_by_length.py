# KATA: Sort by Length
# 
# Dada una lista de strings, devuélvela ordenada de menor a mayor longitud.
# Si dos strings tienen la misma longitud, mantén el orden original.
# 
# RESTRICCIÓN: Prohibido usar .sort() o sorted(). 
# Implementa tu propio algoritmo de ordenación (ej. Bubble Sort).
#
# EJEMPLOS:
# sort_by_length(["a", "ccc", "dd", "bb"]) == ["a", "dd", "bb", "ccc"]
# sort_by_length(["apple", "pie", "shortcake"]) == ["pie", "apple", "shortcake"]
# sort_by_length([]) == []

def sort_by_length(strings):
    for i in range(len(strings)):
        for j in range(len(strings) -1):
            if len(strings[j]) > len(strings[j+1]):
               strings[j], strings[j+1] = strings[j+1], strings[j]
    return strings

#Senior version
#With sorted and keys

def senior_sort_by_length(strings):
    return sorted(strings, key = len)
            


