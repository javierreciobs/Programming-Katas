# Kata: Is Perfect Number
# A perfect number is a number that equals the sum of its divisors
# (excluding itself).
# Example: 6 → divisors are 1, 2, 3 → 1+2+3 = 6 → True
# Example: 28 → divisors are 1, 2, 4, 7, 14 → 1+2+4+7+14 = 28 → True
# Example: 12 → divisors are 1, 2, 3, 4, 6 → 1+2+3+4+6 = 16 → False
#
# is_perfect(6) → True
# is_perfect(28) → True
# is_perfect(12) → False
# is_perfect(1) → False

# Tools:
#

def is_perfect_numbers(number):
    div_array_sum = ""
    divisors_array = []
    divisors = 1
    while divisors < number:
        if number % divisors == 0:
            divisors_array.append(divisors)
        divisors = divisors + 1
    div_array_sum = sum(divisors_array)
    return number == div_array_sum

print(is_perfect_numbers(6))
print(is_perfect_numbers(28))
print(is_perfect_numbers(12))
print(is_perfect_numbers(1))








# #other way
#     for i in number:
#         if number % initial_divisor == 

