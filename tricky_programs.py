"""

Prime numbers
"""

number = int(input("Enter number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(f"{number} is not prime number")
            print(f"{i}, times, {number//i} is {number}")
            break
    else:
        print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")








