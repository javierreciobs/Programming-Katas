# Kata: Palindrome
# Write a function that takes a string and returns True if it is a palindrome and False if it is not.
# A palindrome is a word that reads the same forwards and backwards.

# Examples:
# is_palindrome("racecar") → True
# is_palindrome("hello") → False
# is_palindrome("madam") → True
# is_palindrome("") → True

#Tools:
# Slicing and comparison, no if/else needed

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("sasas"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("madam"))
print(is_palindrome(""))