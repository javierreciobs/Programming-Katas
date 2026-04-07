# Kata: Count Vowels
# Write a function that takes a string and returns the number of vowels it contains.

# Examples:
# count_vowels("hello") → 2
# count_vowels("python") → 1
# count_vowels("aeiou") → 5
# count_vowels("") → 0

#Tools:
#Just a loop for 

def count_vowels(string):
    vocals = 0
    for letter in string:
        if letter in "aeiou":
            vocals +=1
    return vocals


print(count_vowels("hello"))
print(count_vowels("python"))
print(count_vowels("aeiou"))
print(count_vowels(""))
