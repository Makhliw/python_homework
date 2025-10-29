#lesson 5
#task 1 - def is_leap(year): """ Determines whether a given year is a leap year.

def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year = int(input("Enter a year: "))
if is_leap(year):
    print(f"{year} is a leap year ")
else:
    print(f"{year} is not a leap year ")

#task2
n = int(input("Enter a number: "))
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

# task 3
# Solution 1 — with if-else
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a % 2 != 0:
    a += 1  
if b % 2 != 0:
    b -= 1  
if a <= b:
    print(list(range(a, b + 1, 2)))
else:
    print("No even numbers in this range.")
 
# Solution 2 — without if-else
a = int(input("Enter a: "))
b = int(input("Enter b: "))
import math
start = a + (a % 2)
end = b - (b % 2)
print(list(range(start, end + 1, 2)) if start <= end else [])


