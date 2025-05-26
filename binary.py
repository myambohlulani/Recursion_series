# converting into decimals into binary number
# Hlulani Myambo
# 26 May 2025

def to_binary(number):
    if number == 0:
        return "0"
    if number == 1:
        return "1"
    return to_binary(number//2) + str(number % 2)

print(to_binary(10)) # output = 1010
print(to_binary(98)) # output = 1100010
print(to_binary(100)) # output = 1100100