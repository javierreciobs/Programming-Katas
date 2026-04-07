# Kata: Two Sum
# Receives a list of numbers and a target number.
# Returns the indices of the two numbers that add up to the target.
# Examples:
# two_sum([2, 7, 11, 15], 9) → [0, 1]  (2 + 7 = 9)
# two_sum([3, 2, 4], 6) → [1, 2]  (2 + 4 = 6)
# two_sum([3, 3], 6) → [0, 1]  (3 + 3 = 6)

def two_sum(list, target):
    for i in range(len(list)):
        for j in range (i + 1, len(list)):
            if list[i] + list[j] == target:
                return [i, j]

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))



