# KATA: Zip Lists
#
# Dadas dos listas, combínalas en una lista de pares (tuplas).
# Si las listas tienen distinto tamaño, ignora los elementos sobrantes.
#
# zip_lists([1, 2, 3], ["a", "b", "c"]) == [(1, "a"), (2, "b"), (3, "c")]
# zip_lists([1, 2], ["a", "b", "c"]) == [(1, "a"), (2, "b")]
# zip_lists([], ["a", "b"]) == []
# zip_lists([1, 2, 3], []) == []

#Without using built-in function zip()

def zip_list(first_list, second_list):
    zip = []
    for i in range(min(len(first_list), len(second_list))):
        zip.append((first_list[i], second_list[i]))
    return zip

#Senior

def senior_zip_list(senior_first_list, senior_second_list):
    return list(zip(senior_first_list, senior_second_list))

    