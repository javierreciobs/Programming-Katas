# Kata: Sum Nested
# Write a function that receives a list that can contain integers
# or nested lists of integers, and returns the sum of all integers.
#
# Examples:
# sum_nested([1, [2, 3], [4, [5, 6]]]) → 21
# sum_nested([1, 2, 3]) → 6
# sum_nested([]) → 0
# sum_nested([[[[5]]]]) → 5

def sum_nested(array):
    result = 0
    for i in array:
        if isinstance(i, int):
            result += i
        else:
            result += sum_nested(i)
    return result