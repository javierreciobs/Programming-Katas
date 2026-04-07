# Kata: Decimal to Binary
# Write a function that converts a positive integer to its binary representation as a string.
#
# Examples:
# to_binary(1)   → "1"
# to_binary(2)   → "10"
# to_binary(5)   → "101"
# to_binary(10)  → "1010"
# to_binary(255) → "11111111"

#Without function bin()

def to_binary(number:int):
    binary_number = ""
    while number > 0:
        if number % 2 == 0:
            binary_number = "0" + binary_number
        else: 
            number % 2 == 1
            binary_number = "1" + binary_number
        number = number // 2
    return binary_number






