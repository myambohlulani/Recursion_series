# Finding the minimum within the array using the for loop for the first function and recursion only for the second function
# 0mniManTheCpu
# 14 May 2025 - Wednesday
# Recursion series 1 , week 1, # 6

def find_minimum(array: list[int]) -> int:
    """
    This function looks for the minimum value in the array using both the for loop and recursion
    Args:
        array (list[int]): array of integers

    Returns:
        int: it will return the minimum number
    """
    # base case for when an array is empty
    if not array:
        return 
    # base case for when the number is the only on in the array
    if len(array) == 1:
        return array[0]
    minimum: int = array[0]
    # looping through the list of all the numbers from index 1
    for number in array[1:]:
        if minimum > number:
            minimum = number

    return minimum

test = find_minimum([1, 2, 10, -2, 10, 11, -231, 90, 112, 67]) #ouput = -231
print(test)

def find_min(array: list[int]) -> int:
    if not array:
        return 
    if len(array) == 1:
        return array[0]
    return array[0] if array[0] < find_min(array[1:])  else find_min(array[1:])

test_2 = [1, 10, -11, -22, 102, -2, 90, 13]
print(find_min(test_2))#ouput = -22
