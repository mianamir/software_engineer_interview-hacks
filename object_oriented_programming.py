"""
Object oriented programming
why we use Classes?
Logically grouping the data and functions into classes,
so we can reuse and build
"""


class Employee:
    """
    Class variables / Static variable
    """
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        # self.email = first_name.lower() + '.' + last_name.lower() + '@goey.co'
        """
        Use Employee.num_of_employees instead of self.num_of_employees 
        """
        Employee.num_of_employees += 1

    """
    Regular method
    using property decorator to avoid code breakage 
    make any class instance variable to method and use like a variable
    """
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        print('Name Deleted!')
        self.first_name = None
        self.last_name = None

    @property
    def email(self):
        return '{}.{}.@google.co'.format(self.first_name.lower(), self.last_name.lower())

    def apply_raise(self):
        """
        Write self.raise_amount not Employee.raise_amount
        because if employee want to change raise_amount
        then it can be otherwise will not change
        :return:
        """
        self.pay = int(self.pay * self.raise_amount)

    """
    Additional constructors 
    """

    @classmethod
    def set_raise_method(cls, amount):
        """
        people say, class methods are alternative to constructor.
        :param amount:
        :return:
        """
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """
        people say, class methods are alternative to constructor
        this is the example how can we do this using class method
        :param emp_str:
        :return:
        """

        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """
        static method don't take self, or cls automatic argument
        they are included on class and they are not dependent on instance variables
        they don't operate instance or Class, they operate stand alone
        :param day:
        :return:
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    """
    magic methods for better readability 
    """
    def __repr__(self):
        """
        use to show the object with unabigous representation
        :return:
        """
        return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        """
        use to show the object with better representation
        :return:
        """
        return "{} - {} ".format(self.full_name, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name)


"""
Inheritance 
"""


class Developer(Employee):
    """
    customize parent class inherited variables
    """
    raise_amount = 1.20

    def __init__(self, first_name, last_name, pay, programming_language):
        super().__init__(first_name, last_name, pay)
        self.programming_language = programming_language


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for employee in self.employees:
            print('---->', employee.full_name())


Employee.set_raise_method(6.78)

employee_1 = Employee('Amir', 'Savvy', 8000)
employee_2 = Employee('Mian', 'Savvy', 7000)
employee_3 = Employee('Amir', 'Khan', 9000)

#
# print(employee_1.full_name())  # Employee.full_name(employee_1)
# print(employee_2.full_name())  # Employee.full_name(employee_2)
# print(employee_3.full_name())  # Employee.full_name(employee_1)

print(employee_1.pay)
employee_1.apply_raise()
print(employee_1.pay)

"""
How can we access class variable
"""
print("Class variable")
print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)
print(employee_3.raise_amount)

print(Employee.__dict__)
print(employee_1.__dict__)

employee_1.raise_amount = 1.09  # this will create raise_amount for emaployee_1 only

print(employee_1.__dict__)

print(employee_1.pay)
employee_1.apply_raise()
print(employee_1.pay)

print(Employee.num_of_employees)

"""
Regular methods
Class Methods 
Static Methods
"""

print('Before using class method')
print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)
print(employee_3.raise_amount)
print('after using class method')
Employee.set_raise_method(1.09)
print(Employee.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)
print(employee_3.raise_amount)


"""
 Creation of class object from class method below
"""

emp_str_1 = 'Mian-Amir-7000'
emp_str_2 = 'Amir-Savvy-8000'
emp_str_3 = 'Amir-Khan-9000'


new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

"""
using datetime module for employee workday static method
"""

import datetime

my_date = datetime.date(2020, 6, 30)
print(Employee.is_workday(my_date))


"""
Inheritance
"""

developer_1 = Developer('Amir', 'Savvy', 8000, 'Python')
developer_2 = Developer('Mian', 'Savvy', 7000, 'Elixir')
developer_3 = Developer('Amir', 'Khan', 9000, 'Scala')

print(help(Developer))
print(developer_1.programming_language)
print(developer_2.programming_language)
print(developer_3.programming_language)

employee_1 = Employee('Amir', 'Savvy', 5000)
print(employee_1.pay)
print(developer_1.pay)
developer_1.apply_raise()
print(developer_1.pay)


manager_1 = Manager('Amir', 'Savvy', 8000, [developer_1])
manager_2 = Manager('Mian', 'Savvy', 7000, [developer_2])
manager_3 = Manager('Amir', 'Khan', 9000, [developer_3])

print(help(Manager))
print(manager_1.employees)
print(manager_2.employees)
print(manager_3.employees)


print(manager_1.email)
manager_1.add_emp(developer_2)
manager_1.add_emp(developer_3)
print('Before')
manager_1.print_employees()
manager_1.remove_emp(developer_2)
print('After')
manager_1.print_employees()

print(isinstance(developer_1, Employee))
print(isinstance(developer_1, Manager))
print(isinstance(manager_1, Manager))

print(issubclass(Developer, Employee))



"""
Dandar methods / Magic methods
"""

employee_1 = Employee('Amir', 'Savvy', 5000)

print(employee_1)
print(repr(employee_1))
print(str(employee_1))

print(employee_1.__repr__())
print(employee_1.__str__())

print(1+3)

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))



print(len('amirsavvy'))
print('amirsavvy'.__len__())


employee_1 = Employee('Amir', 'Savvy', 8000)

# print(len(employee_1))

# using email property
employee_1.first_name = 'GG'
employee_1.last_name = 'rr'
employee_1.full_name = 'Ok Testing'

print(employee_1.full_name)
print(employee_1.email)
del employee_1.full_name