# binary search using recursion
# 0mniManTheCpu 
# 13 May 2025 - Tuesday

def binary_search(array: list[int], target: int, left_pointer: int, right_pointer: int) -> int:
    """
    This function uses recursion to search a list and find a target.
    Args:
        array (list[int]): The list to search from
        target (int): The target which is numeric
        left_pointer (int): This is the left pointer which starts at index 0
        right_pointer (int): This is the right pointer which starts at the last index

    Returns:
        int: The function will return either index of where the value is or -1 since that is where the value will be if it were to be added
    """
    # always target the middle value
    middle_pointer = (right_pointer + left_pointer) // 2

    # base case 1, returns -1 when left pointer passes the right pointer
    if left_pointer > right_pointer:
        return -1
    # if the middle value in the array is equivalent too target then i return index of it
    if array[middle_pointer] == target:
        return middle_pointer
    # if the middle value if greater than target then move the right pointer into middle_pointer - 1 since the middle value has been checked already
    if array[middle_pointer] > target:
        # recursive call
        return binary_search(array, target, left_pointer, middle_pointer - 1)
    # if the middle value is less than target then move the left pointer into middle_pointer + 1 since the middle avlue has been checked already.
    if array[middle_pointer] < target:
        return binary_search(array, target, middle_pointer + 1, right_pointer)

# test cases and their outputs
test_case: list[int] = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search(test_case, 23, 0, len(test_case) - 1)) #output = 5

test_case2: list[int] = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(test_case2, 8, 0, len(test_case2) - 1)) #output = -1

test_case3: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(binary_search(test_case3, 10, 0, len(test_case3) - 1)) #output = 0

test_case4: list[int] = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(binary_search(test_case4, 50, 0, len(test_case4) - 1)) #output = 9