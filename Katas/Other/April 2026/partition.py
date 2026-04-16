# KATA: Partition
#
# Dada una lista y una función de condición, divide la lista
# en dos listas: los que cumplen la condición y los que no.
#
# partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0) == ([2, 4], [1, 3, 5])
# partition(["hi", "hello", "hey"], lambda s: len(s) > 2) == (["hello", "hey"], ["hi"])
# partition([], lambda x: x > 0) == ([], [])
# partition([1, 2, 3], lambda x: x > 10) == ([], [1, 2, 3])

def partition(list, condition):
    condition_list = []
    uncondition_list = []
    partition_list = condition_list, uncondition_list
    for i in list:
        if condition(i):
            condition_list.append(i)
        else:
            uncondition_list.append(i)
    return partition_list

#Senior version with filter()

def senior_partition(elements, condition):
    return list(filter(condition, elements)), list(filter(lambda x: not condition(x), elements))
    