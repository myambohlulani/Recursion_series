# Flattening an array
# Myambo Hlulani
# 22 May 2025

def flatten(array: list ) -> list:
    # empty list
    if not list:
        return
    if len(array) == 1:
        return [array[0]]
    if isinstance(array[0], list):
        return array[0] + flatten(array[1:])
    return [array[0]] + flatten(array[1:])

test_case = [1, 3, [2, 5, 4], 6, 7, 9, 8, 0]
print(flatten(test_case)) #output = [1, 3, 2, 5, 4, 6, 7, 9, 8, 0]