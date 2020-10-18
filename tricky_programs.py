
def prime_number_checker():
    """
    :return:
    """
    number = int(input("Enter number: "))
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(f"{number} is not prime number")
                # print(f"{i}, times, {number//i} is {number}")
                break
        else:
            print(f"{number} is prime number")
    else:
        print(f"{number} is not prime number")


# print(f'Prime number checker')
# prime_number_checker()


def prime_numbers_in_an_interval():
    """
    :return:
    """
    start_number = int(input("Enter start number: "))
    end_number = int(input("Enter start number: "))

    print(f'Print all Prime Numbers in '
          f'{start_number} and '
          f'{end_number} Interval')

    for number in range(start_number, end_number + 1):
        if number > 0:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(f'{number}')


# prime_numbers_in_an_interval()


def factors_of_a_number():
    num = int(input("Enter number to find its factors: "))
    for i in range(1, num + 1):
        if num % i == 0:
            print(f'{i}')


# factors_of_a_number()


def factorial_of_a_number():
    factorial = 1
    num = int(input("Enter number to find its factorial: "))
    if num < 0:
        print(f'-ve number factorial is not exist')
    elif num == 0:
        print(f'Factorial of 0 is 1')
    print(f'factorial with for loop')
    factorial_with_for_loop(num, factorial)

    print(f'factorial with while loop')
    factorial_with_while_loop(num, factorial)

    print(f'factorial with recursion')
    print(f'Factorial of {num} is '
          f'{factorial_with_recursion(num)}')


def factorial_with_for_loop(num, factorial):
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f'Factorial of {num} is {factorial}')


def factorial_with_while_loop(num, factorial):
    while num > 1:
        factorial *= num
        num -= 1
    print(f'Factorial of {num} is {factorial}')


def factorial_with_recursion(num):
    # if num == 1:
    #     return num
    # else:
    #     return num * factorial_with_recursion(num -1)

    return 1 if (num == 1) else num * factorial_with_recursion(num -1)


# factorial_of_a_number()

from collections import Counter


def find_dup_chars():
    string = input("Enter string: ")
    # words_count = Counter(string)
    for char in string:
        char_count = string.count(char)
        if char_count > 1:
            print(char, char_count)


find_dup_chars()











































"""
Q1: Find the most repeated character in a string. 
Input: "most repeated character"
Output: "e"
"""

string = "most repeated character"

for char in string:
    count_char = string.count(char)

    if count_char > 1:
        print(count_char)











