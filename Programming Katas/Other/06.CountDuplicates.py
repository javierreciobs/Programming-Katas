# Kata: Count Duplicates
# Write a function that receives a string and returns the number of characters that appear more 
# than once. It should not count each duplicate individually, but rather count how many unique 
# characters are repeated.
# count_duplicates("aabbcc") → 3
# count_duplicates("aabbb") → 2
# count_duplicates("hello") → 1
# count_duplicates("abcd") → 0
# count_duplicates("") → 0

def count_duplicates(string):
    repeated_letters = {}
    for letter in string:
        if letter in repeated_letters:
            repeated_letters [letter] += 1
        else: repeated_letters [letter] = 1
    duplicates = 0
    for letter in repeated_letters:
        if repeated_letters[letter] > 1:
            duplicates +=1
    return duplicates

print(count_duplicates("aabbcc"))
print(count_duplicates("aabbb"))
print(count_duplicates("hello"))
print(count_duplicates("abcd"))
print(count_duplicates(""))
