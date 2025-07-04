# Hlulani Myambo
# 17 May 2025

# test cases 

test_cases: list[str] = ["Hello, World!", "Hlulani", "Myambo", "Cape Town", "", "UCT", "Github"]

# length
class Strings(object):
    def __find_length(self, string: str, index=0):
        if not string:
            return 0
        if len(string) == 1:
            return index + 1
        return self.__find_length(string[1:], index + 1)
    
    def get_length(self, data: str, index = 0) -> str:
        if index >= len(data):
            return
        print(self.__find_length(data[index]))
        return self.get_length(data, index + 1)

strings_: Strings = Strings()
strings_.get_length(test_cases)