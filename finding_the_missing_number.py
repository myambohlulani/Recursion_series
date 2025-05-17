# 17 May 2025 - Saturday
# Hlulani Myambo

# The array is always sorted - working on sorting algorithms

# Today I am choosing OOP
# 0 means that there is no missing number unless there aren't negatives and that missing number is 0
# Still using test_Cases as static data too but, I will improve as time goes by

from typing import Self

class MissingNumber(object):
    # recursively look for sum
    def find_sum(self: Self,array: list[int]) -> int:
        if not array:
            return 0
        if len(array) == 1:
            return array[0]
        return array[0] + self.find_sum(array[1:])

    # finding the sum the list would have
    # @staticmethod
    def find_actual_sum(self, array: list[int]) -> int:
        return sum(range(array[0], array[-1] + 1))
    
    # get the missing number within an array
    def get_missing_number(self, array: list[int]) -> int:
        if self.find_sum(array) < 0 and self.find_actual_sum(array) < 0:
            return self.find_actual_sum(array) - self.find_sum(array)
        else:
            return self.find_actual_sum(array) - self.find_sum(array)
        
if __name__ == '__main__':
    missing_number: MissingNumber = MissingNumber()
    # test cases
    test_1 = [1, 2, 3, 5]  #output = 4
    test_2 = [100, 101, 103, 104, 105] #output = 102
    test_3 = [2000, 2001, 2002, 2003, 2004, 2005, 2007] #output = 2006
    test_4 = [-10, -9, -8, -7, -5, -4, -3, -2] #output = -6
    test_5 = [-2, -1, 1, 2, 3] #output = 0
    test_6 = [1, 2, 3, 4, 5, 6] #output  = 0
    
    test_cases = [test_1, test_2, test_3, test_4, test_5, test_6]
    for test_case in test_cases:
        if missing_number.get_missing_number(test_case) == 0 and test_case[0] < 0:
            print(f"The missing number on the array is {missing_number.get_missing_number(test_case)}.")
        elif missing_number.get_missing_number(test_case) == 0 and test_case[0] != 0:
            print("There is no missing number on the array.")
        else:
            print(f"The missing number is {missing_number.get_missing_number(test_case)}.")