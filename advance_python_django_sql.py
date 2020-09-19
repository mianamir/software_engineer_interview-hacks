"""
Python memory management

Python garabag collector checks object references in the code/program
if any object reference is not using in the code, then Python
garbage collector delete that object

https://docs.python.org/3/c-api/memory.html#:~:text=Overview,by%20the%20Python%20memory%20manager.
https://realpython.com/python-memory-management/


Python decorator function
 in the decorator, function remember its last state using yield


(BBI: August 04, 2020)
 Python OOP
 * Polymorphism
 * Function over-riding / loading
 * Virtual functions
 * Static class
 * Difference Interface / Concrete Classes

Django
* ORM
* Middleware and custom middleware
* MVT
* Celery / Redis

Django DRF
* serializers
* viewsets / apiview
* models viewsets


Other Things
* Chat app
* Web sockets
* Auth, Role, permissions
* Authorization / Authentication
*


Django ORM
raw querries
Django models, reverse relation, on delete CASCADE

REST APIS State management
CORS

Cross site scripting

Hashing / Encreption for Register/Login Django

SQL cardnality concept

Scrapy / Python scraping

REACT apis routing


Solution: 1


=> select * from transaction GROUP BY driver_name;

=> Group by is one of the most frequently used SQL clauses.
It allows you to collapse a field into its distinct values.
This clause is most often used with aggregations to show one value per grouped
 field or combination of fields. We can use a group by and aggregates to
 collect multiple types of information.


 Solution: 2

class Driver:
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.owes = 0
        self.payments = []

    def get_balance(self):
        total_paid = 0
        balance = 0
        for paid in self.payments:
            if "amount" in paid:
                total_paid += paid.get("amount")
                balance = self.owes - total_paid
        return balance


driver_a = Driver(first_name="Robert",last_name="Lang",email="robert@some_email.com",phone="9171231122")

driver_a.owes = 56


driver_b = Driver(first_name="Robert",last_name="Langdon",email="langdon@some_email.com",phone="3476567544")

driver_b.owes = 450


print(f"Driver A's name is {driver_a.first_name} {driver_a.last_name}, Balance is ${driver_a.get_balance()}")
print(f"Driver B's name is {driver_b.first_name} {driver_b.last_name}, Balance is ${driver_b.owes}")
print("\n")

import uuid
from pprint import pprint


new_payment_1 = {"ID": uuid.uuid4().hex,"type":"Zelle","amount":300,"date":"05-07-2020","memo":"Robert Langdon 546432"}
pprint(new_payment_1)
new_payment_2 = {"ID": uuid.uuid4().hex, "type":"Zelle","amount":450,"date":"05-07-2020","memo":""}
pprint(new_payment_2)


=> I have added unique UUID into the payment dictionary and in this way we
can identify the driver payment from this ID.



"""






"""
I have added unique UUID into the payment dictionary and in this way we 
can identify the driver payment from this ID.

"""