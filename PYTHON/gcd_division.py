# Euclid's Algorithm on finding the greates common denominator recursively
# Myambo Hlulani
# 22 May 2025

# Not sure about implementation for this one though
# using division
def greatest_common_divisor(number: int, divisor: int) -> int:
    if number % divisor == 0:
        return divisor
    return greatest_common_divisor(divisor, number % divisor)

print(greatest_common_divisor(20, 18)) # output = 2

# using substitution
def gcd(number: int, divisor: int) -> int:
    if number == divisor:
        return divisor
    if number > divisor:
        return gcd(number - divisor, divisor)
    if divisor > number:
        return gcd(divisor, divisor - number)

print(gcd(20, 18)) # output = 2
print(gcd(120, 25)) # output = 5
