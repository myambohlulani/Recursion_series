# This version uses loop for binary search
# 0mniManTheCpu
# 13 May 2025 - Tuesday
# Recursion series 1 , week 1, #1

def binary_search(array: list[int], target: int) -> int:
    """
    This function uses binary search to look for a target using a loop.
    Time complexity => O(logn)
    Args:
        array (list[int]): The ordered list of integers in which the user must search in.
        target (int): The integer that a user is searching for.

    Returns:
        int: This is the index that the function will return if found and return -1 if not found.
            -1 will be returned since we are telling the computer that this is the index the target will be if it were to be added.
    """
    left_pointer: int = 0
    right_pointer: int = len(array) - 1

    while right_pointer >= left_pointer: # loop run until the pointers pass each other and that will tell us that the number is not found
        middle_pointer: int = (left_pointer + right_pointer) // 2 # always looking for middle value in case it is found there
        if array[middle_pointer] == target:
            # if the middle value is equivalent to target then we return that index
            return middle_pointer
        elif array[middle_pointer] > target:
            # if target is lower that the middle value then we discard all values from middle to the end and move our pointer to middle - 1
            right_pointer = middle_pointer - 1
            # moving it -1 since we already checked the middle value and got False
        elif array[middle_pointer] < target:
            # if the target is greater than the middle value then we discard all values less that the middle value and move a pointer to middle + 1
            left_pointer = middle_pointer + 1
    
    # if the value is not in the list, then we return the index it would be if it were to be added
    return -1

print(binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23)) #output = 5
print(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 8)) #output = -1
print(binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 10)) #output = 0
print(binary_search([5, 10, 15, 20, 25, 30, 35, 40, 45, 50], 50)) #output = 9

# This implementation of binary search does not account for duplicates, I will implement those in the near future.
print(binary_search([1, 2, 2, 3, 4, 4, 4, 5, 6, 7], 4)) #output = 4