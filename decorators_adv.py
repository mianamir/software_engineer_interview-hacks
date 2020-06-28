"""
To understand closure first check 1st class functions in Python
https://www.youtube.com/watch?v=kr0mpwqttM0

This is closure example
in closure one function return inner function
"""

"""
First class functions / higher order functions 

Properties of 1st class functions
-> pass as argument to other functions 
-> return func 
-> assign functions to variables 

"""


def double_no(no):
    return no * no


def cube_no(no):
    return no * no * no


def test_func(func, data):
    result = list()
    for i in data:
        result.append(func(i))
    return result


print("First class functions / higher order functions")
doubles = test_func(double_no, [1,2,3,4,5])
print(doubles)


"""
Return a func from other function
"""


def logger(message):

    def log_msg():
        print("Log: ", message)

    return log_msg


print("Return a func from other function")
log_hi = logger("Amir SAvvy...")
log_hi()


"""
Return a func from other function, more practical exafromple
"""


def htm_tag(tag):

    def enclose_text(message):
        print(f'<{tag}>{message}</{tag}>')

    return enclose_text


h1_tag = htm_tag('h1')
h1_tag('Amir Savvy (Data Scientist)')
h1_tag('Amir Savvy (Software Engineer)')

print("**********")
p_tag = htm_tag('p')
p_tag('Amir Savvy (Data Scientist)')
p_tag('Amir Savvy (Software Engineer)')


"""
Closure: https://en.wikipedia.org/wiki/Closure_(computer_programming)

"""


def outer_function(name):
    message = name

    def inner_function():
        print(message)
    return inner_function


print("Closure concept")
print(outer_function.__name__)
closure_res = outer_function("Amir")
closure_res()


"""
Closure example
"""


import logging
logging.basicConfig(filename='closure.log', level=logging.INFO)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def logger(func):

    def logger_function(*args):
        logging.info(f'Running {func.__name__} with argument {args}')
        print(func(*args))

    return logger_function


add_logger = logger(add)
sub_logger = logger(sub)


print("Closure example with logging...")
add_logger(2, 2)
add_logger(22, 22)

sub_logger(10, 5)
sub_logger(100, 50)


"""
Python decorators are functions taking other functions as argument,
add some kind of functionality and returns another function
"""


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper function executed before {original_function.__name__}')
        print('Savvy')
        return original_function(*args, **kwargs)
    return wrapper_function


print("Python decorators")


@decorator_function
def display():
    print('Displayed: ' + "Amir Savvy")


@decorator_function
def dis_info(name, age):
    print(f'Name: {name}, Age: {age}')

display()
dis_info("Kashif", 34)
# decorator_display = decorator_function(display)
# decorator_display()

"""
class base decorators
"""


class DecoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'__call__ function executed before {self.original_function.__name__}')
        print('Decorator Class Func Called')
        return self.original_function(*args, **kwargs)


print("Class Base Decorators")


@DecoratorClass
def display():
    print('Displayed: ' + "Amir Savvy")


display()


@DecoratorClass
def display_info(name, age):
    print(f'display function with agrs ({name}, {age}): ')


display_info("Amir Savvy", 26)


"""
Real example for maintaining script logs using python logging
"""
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')

    return wrapper


"""
calculate running time for any function
"""


def my_timmer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in: {t2:} sec')
        return res
    return wrapper


@my_logger
def display_info(name, age):
    print('display function with agrs ({}, {}): '.format(name, age))


display_info("Amir", 27)


import time

"""
using multiple decorators to one function is equal,
display_info = my_logger(my_timmer(display_info))
"""


@my_logger
@my_timmer
def display_info(name, age):
    time.sleep(1)
    print(f'display_info with args ({name}, {age}): ')


# display_info = my_timmer(display_info)
# print(display_info.__name__)
print("Decorators with @wraps")
# display_info("Amir Khan", 30)


"""
Decorators with arguments 
"""


def prefix_decorator(prefix):

    def decorator_function(original_function):

        def wrapper_function(*args, **kwargs):
            print(prefix, "Executed before", original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, "Executed after", original_function.__name__)
            return result

        return wrapper_function

    return decorator_function


@prefix_decorator('TESTING:')
def display_info(name, age):
    print("display_info ran with arguments ({}, {})". format(name, age))


print('Display info using Decorator with arguments')
display_info('Amir Savvy', 26)