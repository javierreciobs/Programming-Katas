# Kata: Flatten Array
# Write a function that receives a nested list and returns a flat list.
# Examples:
# flatten([1, [2, 3], [4, [5, 6]]]) → [1, 2, 3, 4, 5, 6]
# flatten([1, 2, 3]) → [1, 2, 3]
# flatten([]) → []

def flatten_array(nested_list):
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(flatten_array(i))
        else:
            flat_list.append(i)
    return flat_list



print(flatten_array([1, [2, 3], [4, [5, 6]]]))
print(flatten_array([1, 2, 3]))
print(flatten_array([]))


