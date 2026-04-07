##This is String Calculator Kata

#Tools:
#
#.to_int    (just a created function for this kata)
#list comprehensions
#.startswith()




def to_int(values):
    try:
        return int(values)
    except:
        return 0


def string_calculator(string):
    if (string == "") or (string == None):
        return 0
    if string.startswith("//"):
        separator = string[2]
        expression = string[4:]
        final_values = [to_int(n) for n in expression.split(separator)]
    else: 
        final_values = [to_int(n) for n in string.split(",")]

    return sum(final_values)

#Cases and tests
print(string_calculator(""))
print(string_calculator(None))
print(string_calculator("4"))
print(string_calculator("1,2,3"))
print(string_calculator("a"))
print(string_calculator("1,a"))
print(string_calculator("1,a,2"))
print(string_calculator("1a,2"))
print(string_calculator("//#/3#2"))
print(string_calculator("//#/3,2"))
print(string_calculator("//%/1%2%3"))


