"""
ArbiSoft 19-02-2021

1- Problem Statement
a = [1,2,[3,[4,[5,[6,[],[7]]]]],8]

Required output

a= [1,2,3,4,5,6,7,8]

Sudo Code Solution
res = list()
def get_numbers(a):
    for item in a:
        if type(item) == list:
             get_numbers(inner_item)
        elif item:
            res.append(inner_item)
        else:
             res.append(inner_item)

2- What is Django Framework / Architecture
3- Category/Product Models
4- Default database for Django
5- What are migrations and explain makemigrations/migrate
6- How to create superuser in Django project
7- What is middleware and order matter ?
8- What is serializer and use
9- API throttling in Django rest framework
https://www.django-rest-framework.org/api-guide/throttling/
10- Lazy loading in Python then Django
11- Problem Statement for fibo numbers

# 0,1,1,2,3,5,8,13

def get_fibo(start, end)
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(start, end):
       a,b= i, a+b
       print(b)

get_fibo(0, 5)

0
1
1
2
4

12- Get category name with total number of products count

select c.category_name, count(p.cat_id) as no_products from category c
inner join products p on c.id=p.cat_id order by c.category_name asc;

Note: Count cache db concept








"""