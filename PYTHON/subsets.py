# finding the subsets on an array
# Hlulani Myambo
# 26 May 2025

# dynamic programming
def subsets(array: list[int]) -> list:
    if not array:
        return [[]]
    return subsets(array[1:]) + [ [array[0]] + subset for subset in subsets(array[1:])]

print(subsets([1, 2, 3]))