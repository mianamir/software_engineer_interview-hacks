"""
http://pep8online.com/checkresult
Python Data Structures
Data structure as a way of organizing and storing data such that we can
access and modify it efficiently
List / List Comprehension
List comprehension is an elegant way to define and create lists based on existing lists
List comprehensions are used for creating new list from another iterables
Common applications are to make new lists where each element is the result of some operations
applied to each member of another sequence or iterable, or to create a subsequence of those
elements that satisfy a certain condition
Example 1
"""

# You can either use loops:
squares = []

for x in range(10):
    squares.append(x ** 2)

print(squares)
print('***************')
# Or you can use list comprehensions to get the same result:
squares = [x ** 2 for x in range(10)]

print(squares)

print('***************')

"""
Multiply every part of a list by three and assign it to a new list.
"""

list1 = [3, 4, 5]

multiplied = [item * 3 for item in list1]

print(multiplied)

"""
take the first letter of each word and make a list out of it
"""

listOfWords = ["this", "is", "a", "list", "of", "words"]

items = [word[0] for word in listOfWords]

print(items)

"""
convert lower case / upper case letters
"""

lower = [x.lower() for x in ["A", "B", "C"]]
print(lower)
upper = [x.upper() for x in ["a", "b", "c"]]
print(upper)

"""
extract all the numbers from a string
"""

string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()]
print(string)
print(numbers)

"""
et specific lines out from a text file
"""

# Then create the filter by using list comprehension:

fh = open("test.txt", "r")

result = [i for i in fh if "line3" in i]

print(result)

"""
use list comprehension in functions
"""


# Create a function and name it double:


def double(x):
    return x * 2


# If you now just print that function with a value in it, it should look like this:


print(double(10))

double_list = [double(x) for x in range(10)]
print(double_list)

double_list1 = [double(x) for x in range(10) if x % 2 == 0]
print(double_list1)

double_list2 = [x + y for x in [10, 30, 50] for y in [20, 40, 60]]
print(double_list2)

"""
separate the letters of the word human and add the letters as items of a list
"""

h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

h_letters = [letter + 'amir' for letter in 'human']
print(h_letters)

"""
Conditionals in List Comprehension
"""

number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

"""
if...else With List Comprehension
"""
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)

"""
Find common numbers from two list using list comprehension
"""

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = [a for a in list_a for b in list_b if a == b]

print(common_num)

"""
Return numbers from the list which are not equal as tuple
"""

list_a = [1, 2, 3]
list_b = [2, 7]

different_num = [(a, b) for a in list_a for b in list_b if a != b]

print(different_num)  # Output: [(1, 2), (1, 7), (2, 7), (3, 2), (3, 7)]

"""
List comprehensions can also be used to iterate over strings
"""

list_a = ["Hello", "World", "In", "Python"]

small_list_a = [str.lower() for str in list_a]

print(small_list_a)  # Output: ['hello', 'world', 'in', 'python']

"""
list comprehensions can be used to produce list of list
"""

list_a = [1, 2, 3]

square_cube_list = [[a ** 2, a ** 3] for a in list_a]

print(square_cube_list)  # Output: [[1, 1], [4, 8], [9, 27]]

"""
To understand what yield does, you must understand what generators are.
And before generators come iterables.
Iterables
When you create a list, you can read its items one by one. 
Reading its items one by one is called iteration:
"""

mylist = [1, 2, 3]

for i in mylist:
    print(i)

"""
Generators are iterators, a kind of iterable you can only iterate over once. 
Generators do not store all the values in memory, they generate the values on the fly
"""

mygenerator = (x * x for x in range(3))
for i in mygenerator:
    print(i)

"""
yield is a keyword that is used like return, except the function will return a generator
"""


def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i * i


mygenerator = create_generator()  # create a generator
print(mygenerator)  # mygenerator is an object!

for i in mygenerator:
    print(i)

"""
iterators are something which can be loop over i.e list is iteratable 
List is not iterator because has not next method 
i.e print(next([1, 2, 3, 4, 5])) error: 
"""

nums = [1, 2, 3, 4, 5]
#
# for num in nums:
#     print(num)

# print(dir(nums))
# print(next(nums))

"""
user manually __iter__ method
"""

i_nums = nums.__iter__()
# i_nums = iter(nums)
# print(i_nums)
# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
print('******************')

"""
The other charateristics of iterator is, they only move forward 
"""
while True:
    try:
        item = next(i_nums)
        print(item)

    except StopIteration:
        break

"""
class base iterators 
"""


class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    """
    make the class iterable using this method
    """

    def __iter__(self):
        return self

    """
    add next method for iteration
    """

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


c_nums = MyRange(1, 11)
print("**************************")
# for n in c_nums:
#     print(n)

print(next(c_nums))
print(next(c_nums))
print(next(c_nums))
print(next(c_nums))
print(next(c_nums))

"""
Generators are look like normal functions but instead return the result,
they yield the value. 
Generators are iterators as well but __iter__ snd __next__ methods are
created automatically. 
"""


def my_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1


print('************************')
g_nums = my_generator(1, 11)
# print(next(g_nums))
# print(next(g_nums))

for gn in g_nums:
    print(gn)

"""
Iterators don't need to be end, they can so on forever. 

"""


def my_generator(start):
    current = start
    while True:
        yield current
        current += 1


print('************************')
# g_nums = my_generator(1)

"""
Another feature of iterator is, they take one value at time
its handy when writing memory effient programs 
"""

"""
Generators 
This is more readable procedure 
"""


def square_numbers(s_nums):
    # s_result = []

    for n in s_nums:
        yield (n * n)
        # s_result.append(n * n)
    # return s_result


print("************************")
my_s_nums = square_numbers([1, 2, 3, 4, 5])

"""
below print statement will be show: <generator object square_numbers at 0x0000022BC44E0BF8>,
not the list because generators don't hold entire result in memory, it
Yield one result at a time
"""
print(square_numbers(my_s_nums))

# print(next(my_s_nums))
# print(next(my_s_nums))
for i in my_s_nums:
    print(i)

"""
But instead of above we also can write more efficient code using List Comprehension

"""

my_lc_nums = [x * x for x in [1, 2, 3, 4, 5]]
print('*******************')
for j in my_lc_nums:
    print(j)

"""
Generator example
"""

my_lc_nums = (x * x for x in [1, 2, 3, 4, 5])

"""
Converting generators to list, will loose performance which we have got from generators
"""

list_nums_from_gen = list(my_lc_nums)

print('*******************')
for j in my_lc_nums:
    print(j)

"""
Real example regarding performance 
"""

"""
pip install memory_profiler
2)include it in your code like this
import memory_profiler as mem_profile
3)change code
mem_profile.memory_usage_psutil() to memory_usage()
4)convert you print statements like this
print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )
print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')
print ('Took ' + str(t2-t1) + ' Seconds')
for Windows: https://stackoverflow.com/questions/41191412/no-module-named-mem-profile

for Linux/Ubuntu: https://howtoinstall.co/en/ubuntu/xenial/python-memory-profiler
 
"""
import memory_profiler as mem_profile
import random
import time

names = ['Mian', 'Amir', 'Khan', 'Mian Amir', 'Amir Savvy']
majors = ['Math', 'English', 'Software', 'Web', 'ML', 'AI']
print('*********************************************************************')
print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB')


def people_list(num_people):
    i_result = []
    for z in range(num_people):
        person = {
            'id': z,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        i_result.append(person)

    return i_result


def people_generator(num_people):
    for k in range(num_people):
        person = {
            'id': k,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        yield person


"""
Memory (Before): [16.734375]MB
Memory (After) : [289.36328125]MB
Took: 1552894704.703367 seconds
"""

# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.time()


"""
Memory (Before): [16.75]MB
Memory (After) : [16.76171875]MB
Took: 1552894785.937366 seconds
"""

t1 = time.clock()
people = people_generator(1000000)
t2 = time.time()

print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')
print('Took: {} seconds'.format(t2 - t1))

"""
Lambda, filter, reduce and map
"""

f = lambda x, y: x + y
print('**************')
print(f(1, 1))

"""
The advantage of the lambda operator can be seen when it is used in combination
with the map() function. map() is a function with two arguments
r = map(func, seq)
"""

# showing difference between def() and lambda().
x = lambda a: a + 10
print(x(5))

x1 = lambda a, b: a * b
print(x1(5, 6))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))

"""
https://www.youtube.com/watch?v=DEwgZNC-KyE
System level script 

OS module in python provides functions for interacting with the operating system.
OS, comes under Python’s standard utility modules
"""

import os, glob

os.chdir('E:\certificates-badges')

print('*******************************')
for file in glob.glob("*.png"):
    print(file)

print('***System Level Info***')
print(os.getcwd())
print(os.name)
print(os.listdir('E:\Amir'))

"""
FIZZ / BUZZ
"""


def fizz_buzz(start, end):
    for num in range(start, end):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print("Buzz")


print("***FizzBuzz***")
fizz_buzz(1, 101)

"""
Fibonacci Series
"""


def fibonacci_series(start, end):
    a, b = 0, 1
    for i in range(start, end):
        print(a)
        a, b = b, a + b


print("***fibonacci_series***")
# fibonacci_series(0, 10)


"""
Fibonacci Series using Generators
"""


def fibonacci_series_generators(num_range):
    a, b = 0, 1
    for i in range(0, num_range):
        yield "{}: {}".format(i + 1, a)
        a, b = b, a + b


print("***fibonacci_series_generators***")
for item in fibonacci_series_generators(12):
    print(item)

""" 
Python recursive functions
"""


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(0))
print(fact(5))

import sys

sys.setrecursionlimit(3000)


def fact1(n):
    if n == 0:
        return 1
    else:
        return n * fact1(n - 1)


# print(fact1(2000))

# An example of a recursive function to
# find the factorial of a number

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x - 1))


num = 4
print("The factorial of", num, "is", calc_factorial(num))
print("****************")

print('Even Numbers')
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = [m for m in my_list if m % 2 == 0]

print(new_list)

"""
Dictionary Comprehension
"""

names = ['Mian', 'Amir', 'Mian Amir', 'Amir Khan', 'Savvy', 'Amir Savvy']
skills = ['Software', 'Web', 'Games', 'Networks', 'Machine Learning',
          'Data Sciences']
my_dic = {}
print("Dictionary with Zip Func.")
# for name, skill in zip(names, skills):
#     my_dic[name] = skill
#
# print(my_dic)

# Using dictionary comprehension

my_dic = {name: skill for name, skill in zip(names, skills) if
          name != 'Mian Amir'}

print(my_dic)

"""
Sets are smae like lists but have only unique values 
Set comprehension
"""

print("Sets")

nums = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9]
# my_set = set()
# for n in nums:
#     my_set.add(n)

# Using set comprehension

my_set = {n for n in nums}

print(my_set)

"""
Generators expressions
I want to n*n for each in n in nums
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def gen_func(nums):
#     for n in nums:
#         yield (n * n)
#
#
# my_gen = gen_func(nums)
#
# print("Generator func")
# for i in my_gen:
#     print(i)

# Using generator expression

my_gen = (n * n for n in nums)

print("Generator Expression")
for i in my_gen:
    print(i)

"""
Named Tuple
"""

from collections import namedtuple

# color = (55, 155, 255)

# Dictionary color = {'red': 55, 'green': 155, 'blue': 255}
print('Named tuple')

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155,
              255)  # Optional Color(red = 55, green = 155, blue = 255)

print(color.red)
