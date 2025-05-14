# reversing a string recursively
# 0mniManTheCpu
# 15 May 2025 - Thursday
# Recursion series 1 , week 1, # 8

# no recursion
def lazy_Way(string):
    return string[::-1]
print(lazy_Way("hello, World!")) #output = !dlroW ,olleh

# with recursion
def reversing_string(string: str) -> str:
    if not string:
        return ""
    if len(string) == 1:
        return string[0]
    return reversing_string(string[1:]) + string[0]

print(reversing_string("")) #output = 
print(reversing_string("Hello, World!")) #ouput = !dlroW ,olleH
print(reversing_string("hello, 122, 12][")) #output = []21 ,221 ,olleh
print(reversing_string("!hsup ythgim llA")) #output = All mighty push!
print(reversing_string("nrub dlrow eht teL")) #output = Let the world burn
print(reversing_string(")(()")) # ouput = )(()
print(reversing_string("madam")) #output = madam