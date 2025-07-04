# Looking for the sum of elements within an array recursively
# Hlulani Myambo
# 14 May 2025 - Wednesday

def finding_sum(array: list[int]) -> int:
    """This function calculates for the sum of elements within an array"""
    # base case in case the list is empty
    if not array:
        return 0
    # base case of when the list has only one value
    if len(array) == 1:
        return array[0]
    # recursive call
    return array[0] + finding_sum(array[1:])

print(finding_sum([1, 2, 3, 4, 5])) #output = 15
print(finding_sum([-1, 10, 11, -32, 10, -245])) # output = -247

def finding_sum_of_odd_index(array: list[int], index=1) -> int:
    """
    This function finds the sum of odd indexes recursively
    Args:
        array (list[int]): This is the list which it will be searching from
        index (int, optional): index starts at 1 since that is the beginning of odd index hence Defaults to 1.

    Returns:
        int: The sum of the array or 0 if it is empty
    """
    # base case for empty list
    if not array:
        return 0
    # base case
    if len(array) == 1:
        return array[0]
    # recursive call
    return array[1] +finding_sum_of_odd_index(array[2:], index + 2)

print(finding_sum_of_odd_index([10, 20, 30, 40, 50, 60])) #output = 120
print(finding_sum_of_odd_index([1, 2, 3, 4, 5, 6, 7, 8])) #output = 20
print(finding_sum_of_odd_index([10, 35])) #output = 35
print(finding_sum_of_odd_index([])) #ouput = 0