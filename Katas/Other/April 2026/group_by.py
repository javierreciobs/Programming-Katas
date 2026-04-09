# KATA: Group By
#
# Dada una lista de elementos, agrúpalos en un diccionario
# según el resultado de aplicar una función de agrupación.
#
# La función recibe:
#   - una lista de elementos
#   - una función que devuelve la "clave" de agrupación
#
# Devuelve un diccionario donde cada clave tiene
# una lista de elementos que comparten esa clave.
#
# Ejemplos:
#
# group_by([1, 2, 3, 4, 5], lambda x: x % 2) == {0: [2, 4], 1: [1, 3, 5]}
# group_by(["hi", "hello", "hey"], lambda s: len(s)) == {2: ["hi"], 5: ["hello"], 3: ["hey"]}
# group_by([], lambda x: x) == {}
# group_by([1, 2, 3], lambda x: "par" if x % 2 == 0 else "impar") == {"impar": [1, 3], "par": [2]}

def group_by(elements, key_fn):
    grouped = {}
    if elements == []:
        return {}
    for e in elements:
        if key_fn(e) not in grouped:
            grouped[key_fn(e)] = []
        grouped[key_fn(e)].append(e)
    return grouped

#Senior version

def senior_group_by(elements, key_fn):
    grouped = {}
    for e in elements:
        grouped.setdefault(key_fn(e), []).append(e)
    return grouped

print(senior_group_by([1, 2, 3, 4, 5], lambda x: x % 2))