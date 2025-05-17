# number raised to the nth term
# Hlulani Myambo
# 14 May 2025 - Wednesday

def power_function(number: int | float, exponent: int) -> int | float:
    # base case
    if exponent == 0:
        return 1
    # recursive call
    return number * power_function(number, exponent - 1)

print(power_function(2.0000, 10)) # Output = 1024.0
print(power_function(2.10000, 3)) # output = 9.261000000000001