# KATA: Chunk Array
#
# Divide a list into groups (fragments) of size n.
# The last group can have fewer elements if there are not enough.
#
# chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]
# chunk([], 3) == []
# chunk([1, 2, 3], 1) == [[1], [2], [3]]

def chunk_array(list, n):
    result = []
    for e in range(0, len(list), n):
        result.append(list[e:e+n])
    return result

#Senior version
#Without variables

def senior_chunk_array(list, n):
    return [list[e:e+n] for e in range(0, len(list), n)]

