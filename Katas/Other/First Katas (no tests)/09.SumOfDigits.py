# Kata: Sum of Digits
# Write a function that receives a number and returns the sum of its digits.
# Examples:
# sum_of_digits(123) → 6
# sum_of_digits(456) → 15
# sum_of_digits(0) → 0
# sum_of_digits(99) → 18

#Tools:


#My solution (with claude little help)

def sum_of_digits(digits):
    str_digits = str(digits)
    str_digits.split
    final_sum = sum([int(d) for d in str_digits])
    return final_sum 


print(sum_of_digits(123))
print(sum_of_digits(456))
print(sum_of_digits(0))
print(sum_of_digits(99))

#With claude help

def sum_of_digits2(digits2):
    digits2 = sum([int(d) for d in str(digits2)])
    return digits2


print(sum_of_digits2(123))
print(sum_of_digits2(456))
print(sum_of_digits2(0))
print(sum_of_digits2(99))