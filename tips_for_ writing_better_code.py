"""
Python Tips and Tricks For Writing Better Code
"""

# Turnary conditions
print("Working Turnary conditions")
condition = False

x = 1 if condition else 0

print(x)

# Working with large values
print("Working with large values")
no1 = 10_000_000_000
no2 = 100_000_000

total = no1 + no2
# use f strings
print(f'{total:,}')

# Working with opening files

# use context managers
# with open('files.txt', 'r') as f:
#     file_contents = f.read()

# Working with lists

print("Working with lists")
names = ['Savvy', 'Amir', 'mian']
positions = ['Developer', 'Engineer', 'DataLake']
skills = ['Python', 'Elixir', 'Scala']
# use zip func instead of this
for name, position, skill in zip(names, positions, skills):
    # position = positions[index]
    print(f'{name.title()} is actually working as {position}, have {skill} '
          f'skill.')

for val in zip(names, positions, skills):
    print(val)


# Working unpacking values
print("Working unpacking values")
a, b, c = (1, 2, 4)
print(a, b, c)

# Getting/Setting objects in classes
print("Getting/Setting objects in classes")







