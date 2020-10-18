"""
Q1: Find the most repeated character in a string.
Input: "most repeated character"
Output: "e"
"""


def get_char_count(string):
    counter = 0
    for char in string:
        if char in string:
            counter += 1
        print(char)
    return counter


def get_max_char(data):
    return min(data.values())


def solution():
    string = "most repeated character"
    res = dict()
    for char in string:
        count_char = get_char_count(string)
        if count_char > 1:
            res[char] = count_char

    return get_max_char(res)


print(solution())





_string: string = "most repeated character";













