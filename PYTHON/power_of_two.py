# Hlulani Myambo
# 19 May 2025

test_cases = [1, 2, 10, 12, 32, 64, -1, 128, 125, 0, 250, 1024, -2, -4, -97]
"""
True True False False True True True False True False True True True False
"""

def is_power_of_two(number: int) -> bool:
    """
    This function checks if a number is a power of 2 and returns a boolean, it even checks for negative numbers.
    Args:
        number (int): number to be checked if it is a power of two or not

    Returns:
        bool: returns either True or False depending on the input.
    """
    if number == 2 or number == 0:
        return True
    if not number or number % 2 != 0:
        return False
    if number < 0:
        return is_power_of_two(-number // 2)
    return is_power_of_two(number // 2)

def print_out(data: list[int], index=0):
    """
    This function simply print out data
    Args:
        data (list[int]): data - test cases
        index (int, optional): This is the index of any test case within the array Defaults to 0.

    Returns:
        _type_: Returns None
    """
    if index >= len(data):
        return
    print(is_power_of_two(data[index]))
    return print_out(data, index + 1)

print_out(test_cases)
