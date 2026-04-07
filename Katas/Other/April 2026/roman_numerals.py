# Kata: Roman Numerals
# Write a function that converts an integer to a Roman numeral.
#
# Rules:
# I = 1, V = 5, X = 10, L = 50
# C = 100, D = 500, M = 1000
#
# Examples:
# to_roman(1)    → "I"
# to_roman(4)    → "IV"
# to_roman(9)    → "IX"
# to_roman(14)   → "XIV"
# to_roman(40)   → "XL"
# to_roman(90)   → "XC"
# to_roman(400)  → "CD"
# to_roman(900)  → "CM"
# to_roman(1994) → "MCMXCIV"

def to_roman(number):
    roman_dic = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M",
                 4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM" }
    roman_number = ""
    while number > 0:
        for k in sorted(roman_dic.keys(), reverse = True ):
            if number >= k:
                roman_number += roman_dic[k]
                number -= k
                break
    return roman_number