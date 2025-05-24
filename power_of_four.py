# checking if a number is a power of four or not.
# Hlulani Myambo
# 24 May 2025

def power_of_four(number: int) -> bool:
    if not number or (number % 4 != 0 and number != 1) or number < 0:
        return False
    if number % 4 == 0 or number == 1:
        return True
    return power_of_four(number // 4)

print(power_of_four(4)) # True
print(power_of_four(1)) # True
print(power_of_four(16)) # True
print(power_of_four(10)) # False
print(power_of_four(-4)) # False