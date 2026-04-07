# This is Prime Factors Kata

#Tools:

# .append()
# while loop
# also variables



def prime_factors(value):
    factors = []
    divisors = 2
    while divisors <= value:
        if value % divisors == 0:
            factors.append(divisors)
            value = value // divisors
        else: 
            divisors = divisors + 1
    return factors



#Tests

print(prime_factors(3))
print(prime_factors(36))
print(prime_factors(54))
print(prime_factors(76))
print(prime_factors(109))
print(prime_factors(2))
print(prime_factors(4))
print(prime_factors(8))
print(prime_factors(9))
print(prime_factors(6))
print(prime_factors(25))
print(prime_factors(1155))
