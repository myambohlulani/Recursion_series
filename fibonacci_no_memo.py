# Fibonacci without memoization
# 0mniManTheCpu
# 13 May 2025 - Tuesday
# Recursion series 1 , week 1, # 3

def fibonacci(number: input) -> int:
    # base case 1
    if number == 0:
        return 0
    # base case 2
    if number == 1:
        return 1
    # recursive call
    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(10)) #output 55
print(fibonacci(20)) #output 6765
print(fibonacci(30)) #output 832040

# this will take time depending on your processor
print(fibonacci(50))