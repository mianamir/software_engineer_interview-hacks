__author__ = "Muhammad Amir"

"""
Python Core Concepts
https://www.datacamp.com/community/tutorials/data-structures-python
https://res.cloudinary.com/dyd911kmh/image/upload/c_scale,f_auto,q_auto:best,w_700/v1512740202/Template_2_oxrskq.png
Primitive Data Structures
Integers
Float
Strings
Boolean

Non-Primitive Data Structures
Arrays
Lists
Files

https://www.datacamp.com/community/tutorials/python-numpy-tutorial

Python String 
https://www.datacamp.com/community/tutorials/python-string-tutorial
https://www.geeksforgeeks.org/python-strings/
https://www.datacamp.com/community/tutorials/python-string-split
https://www.datacamp.com/community/tutorials/python-string-replace
https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU


Python Regular Expression
https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial

https://www.geeksforgeeks.org/python-programming-language/

F String 
f'{one} {two}, Great Country'
f'{one.upper()} {two.title()}, Great Country'
"""

# List Comprehension
# https://www.datacamp.com/community/tutorials/18-most-common-python-list-questions-learn-python

data_list = [1,2,3, 3,4,5,6, 6,7,8,9, 10,10]
print([n*n for n in data_list])
map_res = map(lambda n: n*n, data_list)
for i in map_res:
    print(i, end=" ")

print([n for n in data_list if n % 2 == 0])
filter_res = filter(lambda n: n % 2 == 0, data_list)
for i in filter_res:
    print(i, end=" ")

print([(letter, no) for letter in "abcd" for no in range(4)])

# # Dict Comprehension
names = ["Amir", "Savvy", "Khan", "mian"]
roles = ["Data", "Web", "IT", "Software"]
# dict_res = dict()
# for name, role in zip(names, roles):
#     dict_res[name] = role
# print(dict_res)
print({name: role for name, role in zip(names, roles) if name != "Khan"})

# # Set Comprehension
print({n for n in data_list})

# Generator Expressions

# def gen_func(data):
#     for n in data:
#         yield n*n
# test_gen = gen_func(data_list)

# using generator expression
test_gen = (n*n for n in data_list)

for i in test_gen:
    print(i, end=" ")



"""
Sorting Lists, Tupels, Objects

Difference between list sort() / sorted()
"""
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li, reverse=True)
print("\nOrg. List:\t", li)
print("Sorted List using 'Sorted Func':\t", s_li)
# using without builtin function
for i in range(0, len(li) - 1):
    for j in range(0, len(li) - 1):
        if li[j] > li[j+1]:
            t = li[j]
            li[j] = li[j+1]
            li[j+1] = t

print("Sorted List without using func:\t", li)
s_li.sort(reverse=True)
print("Sorted List using 'Sort Func':\t", s_li)

# Sort list with age
name_age_list = [("Bilal", 132), ("Zasit", 4), ("Ali", 43), ("Cahid",52)]
# Ans
new_list = sorted(name_age_list, key=lambda i: i[1])
# print(new_list)
from operator import itemgetter, attrgetter
new_list_itemgetter = sorted(name_age_list, key=itemgetter(1))
new_list_itemgetter_2 = sorted(name_age_list, key=itemgetter(0))
# new_list_attrgetter = sorted(name_age_list, key=attrgetter('name'))
# print(new_list_itemgetter)
# print(new_list_itemgetter_2)


tuple_data = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tuple = sorted(tuple_data)
print("Sorted Tuple  using 'Sorted Func':\t", li)
# sort() func can't be used for tuple because tuple is immutable


# Sort Objects
class Employee:
    def __int__(self, name:str, age:int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name}, {self.age}, ${self.salary})'

# e1 = Employee('Savvy', 35, 545000.5)
e1 = Employee()
e2 = Employee()
e3 = Employee()

e1.name = 'Savvy'
e1.age = 35
e1.salary = 45000

e2.name = 'Khan'
e2.age = 22
e2.salary = 25000

e2.name = 'Test'
e2.age = 26
e2.salary = 29000

employees = [e1, e2, e3]


def print_employees(data):
    print("Name: ", data.name)
    print("Age: ", data.age)
    print("Salary: ", data.salary)
    print("*******")

# print_employees(employees)



# def e_sort(emp):
#     return emp.age

from operator import attrgetter


# s_employees = sorted(employees, key=e_sort, reverse=True)
# s_employees = sorted(employees, key=lambda e: e.name)
# s_employees = sorted(employees, key=attrgetter('age'))
# print("Sorted Employee Objects", s_employees)

# Write optimized code for below senario
numlist = []
# for num in range(1000000):
#     if num not in numlist:
#           numlist.append(num)

# Ans: Use xrange instead of range:range()
# https://www.geeksforgeeks.org/range-vs-xrange-python/
# xrange() – This function returns the generator object that can be used
# to display numbers only by looping. Only particular range is displayed on
# demand and hence called “lazy evaluation”.
res = (n for n in range(10) if n not in numlist)
print("Optimized code using generator expression")
for i in res:
    print(i, end=" ")


# Python pass by value and reference concept
# https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/

"""
Binary Concept
"""
# num = 5 #(0101)
# bit_index = 2

# num = 3 #(0011)
# bit_index = 2

# def big_finder(bit_index, num):
#
#     return num | bit_index
#
# print(big_finder())

print("\nBinary Concepts")

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
# c = 0

c = a & b        # 12 = 0000 1100
print("Line 1 - Value of c is ", c)

c = a | b        # 61 = 0011 1101
print("Line 2 - Value of c is ", c)

c = a ^ b        # 49 = 0011 0001
print("Line 3 - Value of c is ", c)

c = ~a           # -61 = 1100 0011
print("Line 4 - Value of c is ", c)

c = a << 2       # 240 = 1111 0000
print("Line 5 - Value of c is ", c)

c = a >> 2       # 15 = 0000 1111
print("Line 6 - Value of c is ", c)

# https://www.tutorialspoint.com/python/bitwise_operators_example.htm
# https://realpython.com/python-memory-management/
# https://ironpython.net/
# https://www.jython.org/
# https://www.pypy.org/
