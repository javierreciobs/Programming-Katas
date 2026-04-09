# Kata: Capitalize Words
# Write a function that capitalizes the first letter of each word in a string.
#
# Examples:
# capitalize_words("hello world")        → "Hello World"
# capitalize_words("the quick brown fox") → "The Quick Brown Fox"
# capitalize_words("python is fun")      → "Python Is Fun"
# capitalize_words("")                   → ""

def capitalize_word(string):
    capitalize = ""
    words = string.split()
    for w in words: 
        capitalize += w.capitalize() + " "
    return capitalize.strip()

#Senior Version
#Claude knows

def senior_capitalize_word(string):
    return " ".join(w.capitalize() for w in string.split())
