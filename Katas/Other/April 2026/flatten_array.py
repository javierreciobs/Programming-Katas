# Kata: Flatten Array (con TDD)
# Write a function that receives a nested list and returns a flat list.
# Examples:
# flatten([1, [2, 3], [4, [5, 6]]]) → [1, 2, 3, 4, 5, 6]
# flatten([1, 2, 3]) → [1, 2, 3]
# flatten([]) → []

def flatten_array(array):
    flat_list = []
    for element in array:
        if isinstance(element, int):
            flat_list.append(element)
        else: 
            flat_list.extend(flatten_array(element))
    return flat_list
        
