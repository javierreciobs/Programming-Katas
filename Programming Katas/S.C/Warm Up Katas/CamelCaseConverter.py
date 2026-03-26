##This is CamelCaseConverter Kata

#Tools:
#  
# .replace()
# .join()
# .capitalize()
# .spliy()
# list comprehensions

def camel_case_converter(string):
    if string == "":
        return ""
    words = string.replace("_", " ").replace("-", " ").split()
    capitalized = [w.capitalize() for w in words]
    joined = "".join(capitalized)
    return joined


print(camel_case_converter(""))
print(camel_case_converter("foo"))
print(camel_case_converter("Foo Bar"))
print(camel_case_converter("foo_bar foo-bar"))







#HALL OF SHAME


# text = "Foo bar foo"
# print(text.split())

# text2= "foo_bar foo-bar"

#print(text2.replace("_", "" and "-", "").join())

# print(text2.replace("_", "").replace("-", "").join(text2))

#print("".join(["Foo", "Bar", "Foo"]))

# print(text2.capitalize())