# determining if a number is a power of 3
# Hlulani Myambo
# 23 May 2025

def power_of_three(number: int) -> bool:
    if not number  or (number < 3 and number != 1):
        return False
    if number % 3 == 0 or number == 1:
        return True
    if number % 3 != 0:
        return False
    return power_of_three(number // 3)

print(power_of_three(10)) # False
print(power_of_three(3)) # True
print(power_of_three(27)) # True
print(power_of_three(1)) # True
print(power_of_three(0)) # False