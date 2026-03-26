#This is fibonacci kata

#Tools:

#Here we have a recursive function (a function that calls itself)

def fibonacci(value):
    if value == 0: 
        return 0
    elif value == 1:
        return 1
    return fibonacci(value-1) + fibonacci(value-2)
        


#Tests 
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))


#Other way 
#With variables loop


def fibonacci2(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    first_value = 0
    second_value = 1
    for i in range(i-1):
        fibonacci_value = first_value + second_value
        first_value = second_value
        second_value = fibonacci_value
    return fibonacci_value

#Tests
print(fibonacci2(0))
print(fibonacci2(1))
print(fibonacci2(2))
print(fibonacci2(3))
print(fibonacci2(4))
print(fibonacci2(5))
print(fibonacci2(6))
print(fibonacci2(7))

