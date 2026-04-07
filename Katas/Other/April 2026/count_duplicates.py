# Kata: Count Duplicates (con TDD)
# Write a function that receives a string and returns the number 
# of characters that appear more than once.
# Examples:
# count_duplicates("aabbcc") → 3
# count_duplicates("aabbb") → 2
# count_duplicates("hello") → 1
# count_duplicates("abcd") → 0
# count_duplicates("") → 0

def count_duplicates(string):
    count = 0
    dic = {}
    for i in string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        if dic[i] > 1:
            count += 1
    return count