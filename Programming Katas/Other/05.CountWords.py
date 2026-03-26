# Kata: Count Words
# Write a function that takes a string and returns the number of words it contains.

# Examples:
# count_words("hello world") → 2
# count_words("python is great") → 3
# count_words("") → 0
# count_words("one") → 1

#Tools:
# .split()
# .len()

def count_words(string):
    words = len(string.split())
    return words

print(count_words("hello world"))
print(count_words("python is great"))
print(count_words(""))
print(count_words("one"))

print(len(["fasf", "afasff", "fasaf"]))