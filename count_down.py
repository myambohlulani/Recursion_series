# Myambo Hlulani
# 18 May 2025

def count_down(number):
    if number == 0:
        return 0
    print(number, end=' ')
    return count_down(number - 1)

print(count_down(10))
print(count_down(9))
print(count_down(8))
print(count_down(7))
print(count_down(6))
print(count_down(5))
print(count_down(4))
print(count_down(3))
print(count_down(2))
print(count_down(1))
print(count_down(0))