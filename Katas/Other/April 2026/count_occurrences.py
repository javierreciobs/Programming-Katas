# Kata: Count Occurrences
# Write a function that counts how many times each word appears in a string.
# Ignore case. Return a dictionary.
#
# Examples:
# count_occurrences("hello world hello") → {"hello": 2, "world": 1}
# count_occurrences("the cat sat on the mat") → {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
# count_occurrences("") → {}

def count_occurrences(string):
    words = string.split()
    dic = {}
    for w in words:
        # w is the key and 1 is the value
        if w in dic:
            dic[w] += 1
        else: 
            dic[w] = 1
    return dic

#Senior version

from collections import Counter

#Counter is a dic subclass to count hashables elements (inmutable objets) in a collection

def senior_count_occurences(string):
    return Counter(string.split())

    