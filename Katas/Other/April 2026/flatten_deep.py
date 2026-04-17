# KATA: Flatten Deep
#
# Dada una lista anidada a cualquier nivel de profundidad,
# devuelve una lista completamente plana.
#
# flatten_deep([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
# flatten_deep([[1, [2]], [3, [4, [5]]]]) == [1, 2, 3, 4, 5]
# flatten_deep([]) == []
# flatten_deep([1, 2, 3]) == [1, 2, 3]

def flatten_deep(nested_lists):
    result = []
    for i in nested_lists:
        if isinstance(i, list):
            result.extend(flatten_deep(i))
        else:
            result.append(i)
    return result

#Senior version
#Warning
#This can provoke a recursionError, python has a limit of around 1000 turns

def senior_flatten_deep(senior_nested_lists):
    return sum([senior_flatten_deep(i) if isinstance(i, list) else [i] for i in senior_nested_lists], [])
    


