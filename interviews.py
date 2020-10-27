"""
Date: 27-10-2020
Position: Full-Stack Software Engineer(Python/Django + JavaScript)
Duration: 1 to 1.5 hours
Company: https://www.vitalinteraction.com/

1- Coding standard of Python

"""

# 2- What is MRO in Python

# Ans
class A(object):

    def sum(self, n1, n2):
        return (n1+n2)


class B(object):

    def sum(self, n1, n2):
        return 2 * (n1+n2)


class C(A, B):

    def sum(self, n1, n2):
        return 3 * (n1+n2)


class D(B):
    pass

b = B()
print(b.sum(2,2)) # 8

c = C()
print(c.sum(2,2)) # 12


d = D()
print(d.sum(2,2)) # 8


# 3- Difference b/w function overloading and overriding
# Ans

# 4- What is abstract class and why we use it?

# Ans

# 5- What is mixins in Python/Django
# Ans


# 6- What is Encapsulation in Python
# Ans

# 7- Difference generator / Iterator in Python?
# Ans

# 8- What is main feature of generator
# Ans

# 9- Can we use create custom generator? then what is main thing to
# have this custom generator

# 10- What is multi-threading / multi-processing in Python
# Ans

# 11- When multi-cores used and when multi-processors used?
# Ans

# 12- What things are shared in multi-threading in Python?
# Ans

# 13- Can multi threads runs in a process?

# 14- Difference b/w muttable and immutable data structures in Python
# Ans

# 15- Is Python strings are mutable?

# 16(a)- When we create strings with same name i.e test = "abc", what
# happened in the memory.

# Ans

# 16(b)- Will strings created on new memory or used same memory?

# Ans

# 17- What are decorators? Write decorator for login required

# Ans

# 18- Lambda function in Python
# Ans

# 19- Design patterns in Python, write singleton pattern in Python
# Ans

# 20- What magic method called when object created in Python?

# 21- __new__ magic do while creating single instance in Python object?

# 22- what is framework? and why Django?

# 23- How request/response works in Django?

# 24- Who process URL when user request to the any uri i.e /api

# 25- Indexes in SQL, types and what is cluster index?

# 26- Difference b/w cluster and non-cluster index

# 27- Joins in database?

# 28- Normalization of database? 1st, 2nd, 3rd with examples?

# 29- What is one-many relation?

# 30- What is many-to-many relation and can we implement this relation
# without 3rd table

# 31- Query

"""
Table: Student Marks
Columns: ID, Name, Class_ID, Marks

=> Fetch students marks 2nd highest class wise 
"""

# 32- Do this above using Django ORM

# 33- Upload big file using Python/Django

# ----------------------------------------------------------------------------
















