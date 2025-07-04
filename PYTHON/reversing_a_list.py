# Reversing a list within a list and reversing just a list
# 0mniManTheCpu
# 15 May 2025 - Thursday
# Recursion series 1 , week 1, # 9

def reversing_list(array: list[int | str | None]) -> list:
    # base case
    if not array:
        return []
    # base case 2
    if len(array) == 1:
        return [array[0]]
    # recursive call
    return reversing_list(array[1:]) + [array[0]]

print(reversing_list([1, 2, 3, 4])) #ouput = [4, 3, 2, 1]
print(reversing_list([])) #ouput = []
print(reversing_list([""])) #ouput = ['']
print(reversing_list(["Hello, World!", "Sucks does not it?"])) #output = ['Sucks does not it?', 'Hello, World!']

def reversing_array_within_and_elements(array: list[list[int | str | list | None]]) -> list:
    # base case for empty array
    if not array:
        return []
    # base case incase the array contains 1 element
    if len(array) == 1:
        # base case incase the first element is an array/list
        if type(array[0]) == list:
            return [reversing_array_within_and_elements(array[0])]
        else:
            # if it is not an array, return that first element
            return [array[0]]
        # ternary operator => makes the code more readable and easy to write
        # return [reversing_array_within_and_elements(array[0])] if type(array[0]) == list else [array[0]]
    # if the first element is a list/array base case
    if type(array[0]) == list:
        return reversing_array_within_and_elements(array[1:]) + [reversing_array_within_and_elements(array[0])]
        
    return reversing_array_within_and_elements(array[1:]) + [array[0]]

print(reversing_array_within_and_elements([[], [1, 2, 3], [10, 'Hello World!', [10, 12, 13, [14, 19]]], "Long!"])) #output = ['Long!', [[[19, 14], 13, 12, 10], 'Hello World!', 10], [3, 2, 1], []]
print(reversing_array_within_and_elements([[], [1, 2, 3]])) # output = [[3, 2, 1], []]
