# Kata: Find Maximum
# Write a function that receives a list of numbers and returns the largest one.
# You cannot use the built-in max() function.
# Examples:
# find_maximum([1, 3, 2]) → 3
# find_maximum([5, 5, 5]) → 5
# find_maximum([-1, -3, -2]) → -1
# find_maximum([7]) → 7

# Tools:
# Just a loop that runs the array of numbers, compares and reassigns

def find_maximun(numbers):
    maximum = numbers[0]
    for i in numbers:
        if maximum < i:
             maximum = i
    return maximum

print(find_maximun([1, 3, 2]))
print(find_maximun([5, 5, 5,]))
print(find_maximun([-1, -3, -2]))
print(find_maximun([7]))