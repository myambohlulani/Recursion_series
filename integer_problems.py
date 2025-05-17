# Hlulani Myambo
# 17 May 2025 - Saturday

from typing import Self

# test cases
array_of_integers = [0, 18, 123, 2025, 19005, 123123]

class CountDigits(object):
    # converting the number into string
    # using private method
    @staticmethod
    def __get_string(number: int) -> str:
        return str(number)
    
    # counting the numbers recursively
    # private method
    def __count_numbers(self: Self, string: str, count = 0) -> int:
        if not string:
            return 0
        if len(string) == 1:
            return count + 1
        return self.__count_numbers(string[1:], count + 1)

    # find the total here
    def get_total(self: Self, string: int) -> int:
        return self.__count_numbers(self.__get_string(string))
    
    # printing recursively
    def get_output(self, data: list[int], index=0) -> int:
        if len(data) <= index:
            return
        print(self.get_total(data[index]))
        return self.get_output(data, index + 1)

# instance
count_digits: CountDigits = CountDigits()

# get results from above class
print("Counting...")
count_digits.get_output(array_of_integers)

class FindProduct(object):
    @staticmethod
    def __change_to_string(number: int) -> str:
        return str(number)
    
    def get_product(self: Self, number) -> int:
        string = self.__change_to_string(number)
        if not string:
            return 0
        if len(string) == 1:
            return int(string[0])
        return int(string[0]) * self.get_product(int(string[1:]))

    # printing recursively
    def get_output(self, data: list[int], index=0) -> int:
        if len(data) <= index:
            return
        print(self.get_product(data[index]))
        return self.get_output(data, index + 1)
    
# instance 
find_product: FindProduct = FindProduct()

# get output
print("\nGetting the product.")
find_product.get_output(array_of_integers)