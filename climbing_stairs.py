# climbing the stairs
# Myambo Hlulani
# 27 May 2025

def climbing_stairs(number):
    if number < 1:
        return 0
    if number == 1:
        return 1
    if number == 2:
        return 2
    return climbing_stairs(number - 1) + climbing_stairs(number - 2)

print(climbing_stairs(4)) # 5 ways