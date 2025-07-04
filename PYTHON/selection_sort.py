
#
#
#

# def selection_sort(array: list[int]) -> list[int]:
#     for index in range(len(array)):
#         minimum = index
#         for inner_index in range(index + 1, len(array)):
#             if array[minimum] > array[inner_index]:
#                 minimum = inner_index
#         array[index], array[minimum] = array[minimum], array[index]

#     return array

# print(selection_sort([64, 25, 12, 22, 11]))

def selection_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array

    def find_min_index(arr, current_index=0, min_index=0):
        if current_index == len(arr):
            return min_index
        if arr[current_index] < arr[min_index]:
            return find_min_index(arr, current_index + 1, current_index)
        return find_min_index(arr, current_index + 1, min_index)

    min_index = find_min_index(array)
    if min_index != 0:
        array[0], array[min_index] = array[min_index], array[0]

    return [array[0]] + selection_sort(array[1:])

print(selection_sort([64, 25, 12, -1,  22, 11]))
