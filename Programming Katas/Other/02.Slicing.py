#Here some more exercises of slicing in python [::]

#First
#Given "hello", obtain only the letters in even positions. That is, "hlo"

def pairs_letters(string):
    return (string [::2])

print(pairs_letters("hello"))

#Second
#Given "abcdefgh", obtain the last 3 characters. Do not count the letters by hand, using slicing.

def last_three_characters(string):
    return (string [-3::])

print(last_three_characters("abcdefg"))

#Third
#Given "Python is great", get only the word "great" using slicing.

def return_great(string):
    return (string [-5::])

print(return_great("Python is great"))

def return_great_with_other_way(string):
    return string.split()[-1]

print(return_great_with_other_way("Python is great"))