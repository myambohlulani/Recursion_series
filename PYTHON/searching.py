# Searching for a number within an array using recursion
# Myambo Hlulani
# 22 May 2025

def search(array: list[int], target: int) -> bool:
    # empty array
    if not array:
        return False
    if len(array) == 1:
        return array[0] == target
    if array[0] == target:
        return True
    return search(array[1:], target)

if __name__ == '__main__':
    test_case = [-11, -8, -5, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 34, 37, 40, 43, 49, 52, 97, 100, 103, 106, 109, 112, 115, 118]
    print(search(test_case, -11)) # True
    print(search(test_case, 0)) # False
    print(search(test_case, 118)) # True
    print(search(test_case, 1000)) # False