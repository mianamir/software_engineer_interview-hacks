# union
print('Python dic union')
a = {'id' : 5, 'username' : 'PythonUser', 'email' : 'pythonista@gmail.com'}
b = {'id' : 5, 'username' : 'PythonUser', 'email' : 'iluvpython@outlook.com'}

print(a | b)
{**b, **a}

#b.update(a)
#print(b)
a |= b
print(a)


# Timezone
print('Python timezone')
from datetime import datetime
#from pytz import timezone
from zoneinfo import ZoneInfo

current_time = datetime.now()
print(current_time)
current_time_amsterdam = datetime.now()
# print(current_time.astimezone(ZoneInfo('Europe/Amsterdam')))
print(current_time.astimezone(ZoneInfo('America/Los_Angeles')))


print('Type hint')
#from typing import List

mylist: list[int] = [1, 2, 3, 4]
print(mylist)

mylist = '1234' # will not break the code
print(mylist)

# remove prefix suffix
print('remove prefix suffix')

doctors = ['Dr. Leonard McCoy', 'Dr. Beverly Crusher', 'Dr. Julian Bashir', 'The Doctor', 'Dr. Phlox']

names = []

#for doctor in doctors:
    #if doctor.startswith('Dr. '):
    #    names.append(doctor[4:])
    #else:
    #    names.append(doctor)
#    names.append(doctor.removeprefix('Dr. '))

names = [doctor.removeprefix('Dr. ') for doctor in doctors]
print(names)