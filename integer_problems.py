# Hlulani Myambo
# 17 May 2025 - Saturday

from typing import Self
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

# instance
count_digits: CountDigits = CountDigits()

# if the file is run directly , it must run but if it is imported the code will not be executed immediately
if __name__ == '__main__':
    print(count_digits.get_total(0)) #output = 1
    print(count_digits.get_total(18)) #ouput = 2
    print(count_digits.get_total(123)) #ouput = 3
    print(count_digits.get_total(2025)) #output = 4
    print(count_digits.get_total(19005)) #output = 5
    print(count_digits.get_total(123123)) #output = 6