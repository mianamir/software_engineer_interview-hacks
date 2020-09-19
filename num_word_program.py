"""
Each number on the telephone dial (except 0 and 1) corresponds to three
 alphabetic characters. Those correspondences are:

 2 ABC
 3 DEF
 4 GHI
 5 JKL
 6 MNO
 7 PRS
 8 TUV
 9 WXY

03248428679
print all possible "words" that your phone number (without the area code)
spells. (They may not be real english words, but just some sequence of
characters). Since the digits 0 and 1 have no alphabetic equivalent, an
input number which contains those digits should be rejected. The input will
be one or more seven digit integers from standard input.

"""


def get_words_pattern(cell_numbers, words):
    """
    get possible "words" from phone number
    (without the area code) spells.
    :param cell_numbers:list
    :param words:dict
    :return: words patterns:list
    """
    res_words = list()
    for item in cell_numbers:
        for key in words:
            if item == key and (item != 0 or item != 1):
                res_words.append(words[key])

    return res_words


cell_no_list = [0, 3, 2, 4, 8, 4, 2, 8, 6, 7, 9]
# 03248428679
words_dict = {
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PRS',
    8: 'TUV',
    9: 'WXY'
}
print(get_words_pattern(cell_no_list, words_dict))







