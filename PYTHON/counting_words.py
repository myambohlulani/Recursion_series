# counting for the occurances of a word within a string
# Hlulani Myambo
# 30 May 2025

def counting_words(string: str, hashmap = None) -> dict[str, int]:
    if hashmap is None:
        hashmap: dict = {}

    # empty string
    if not string:
        return hashmap

    # for one value only
    if len(string) == 1:
        if string[0] not in hashmap:
            hashmap[string[0]] = 1
            return counting_words(string[1:], hashmap)
        if string[0] in hashmap:
            hashmap[string[0]] += 1
            return counting_words(string[1:], hashmap)

    # in case the length is not 1
    if string[0] not in hashmap:
        hashmap[string[0]] = 1
        return counting_words(string[1:], hashmap)
    if string[0] in hashmap:
        hashmap[string[0]] += 1
        return counting_words(string[1:], hashmap)

string: str = "Hello hlulani hello myambo hi hlulani hello world is crazy hello good morning good people hlulani"
string: list[str] = string.split()

print(counting_words(string)) # output = {'Hello': 1, 'hlulani': 3, 'hello': 3, 'myambo': 1, 'hi': 1, 'world': 1, 'is': 1, 'crazy': 1, 'good': 2, 'morning': 1, 'people': 1}

names: list[str] = ["hlulani", 'Myambo', "Hlulani", "myambo", "Hello, World!"]
print(counting_words(names)) #output = {'hlulani': 1, 'Myambo': 1, 'Hlulani': 1, 'myambo': 1, 'Hello, World!': 1}


# JetBrains Mono Light
# C:\Users\HLULANI\AppData\Local\Microsoft\Windows\Fonts\JetBrainsMono-Light.ttf