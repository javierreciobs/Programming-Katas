# KATA: Unique in Order
#
# Dada una lista de elementos, devuelve una nueva lista donde
# se eliminen los duplicados pero se mantenga el orden original.
#
# unique_ordered([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
# unique_ordered(["a", "b", "a", "c"]) == ["a", "b", "c"]
# unique_ordered([]) == []

def unique_ordered(elements):
    unique_list = []
    for i in elements:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

#Senior

def senior_unique_ordered(senior_elements):
    return list(dict.fromkeys(senior_elements))