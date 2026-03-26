# Kata: Reverse a String
# Write a function that takes a string and returns that string in reverse
#Examples:
# reverse("hello") → "olleh"
# reverse("kata") → "atak"
# reverse("") → ""

#Tools
# ::-1
# start:end:step
# start default = 0
# end default string end
# step default = 1



def reverse_string(string):
    return (string [::-1])


print(reverse_string("Hello"))
print("Hello"[::2])