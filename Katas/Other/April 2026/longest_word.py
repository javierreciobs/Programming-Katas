# Kata: Longest Word
# Write a function that returns the longest word in a string.
# If there are ties, return the first one.
#
# Examples:
# longest_word("hello world") == "hello"
# longest_word("the quick brown fox") == "quick"
# longest_word("I love Python") == "Python"
# longest_word("") == ""

def longest_word(string):
    words = string.split()
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

#Senior version
# max() with len criteron

def senior_longest_word(string):
    return "" if string == "" else max(string.split(), key=len)

