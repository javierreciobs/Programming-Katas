# Kata: Anagram Detector
# Write a function that checks if two strings are anagrams of each other.
# An anagram uses the same letters in a different order.
# Ignore case and spaces.
#
# Examples:
# is_anagram("listen", "silent")     → True
# is_anagram("hello", "world")       → False
# is_anagram("Astronomer", "Moon starer") → True
# is_anagram("", "")                 → True

#I promise that my instict told me that I can resolve this in one line with return comparison

def anagram_detector(string1, string2):
    return sorted(string1.lower().replace(" ", "")) == sorted(string2.lower().replace(" ", ""))
