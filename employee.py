import requests


class Employee:
    raise_amount = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return '{}.{}@google.co'.format(self.first_name.lower(),
                                         self.last_name.lower())

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def monthly_schedule(self, month):
        response = requests.get(f'http://google.co/{self.last_name}/{month}')
        if response.ok:
            return response.text
        return 'Bad Response!'

