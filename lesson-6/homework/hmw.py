#task 1 Modify String with Underscores
def modify_string(txt):
    vowels = 'aeiou'
    result = ''
    count = 0
    for i, ch in enumerate(txt):
        result += ch
        count += 1
        if count == 3 and i != len(txt) - 1:
            if ch in vowels or (i + 1 < len(txt) and txt[i + 1] == '_'):
                result += txt[i + 1] if i + 1 < len(txt) else ''
                count = 0
            else:
                result += '_'
                count = 0
    return result
print(modify_string("hello"))     
print(modify_string("assalom"))     
print(modify_string("abcabcabcdeabcde"))  
#task 2 Integer Squares Exercise
n = int(input("Enter a number: "))
for i in range(n):
    print(i ** 2)
#task 3 Loop-Based Exercises
#exercise 1
i = 1
while i <= 10:
    print(i)
    i += 1
#exercise 2
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#exercise 3
n = int(input("Enter number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum is:", total)
#exercise 4
num = int(input("Enter number: "))

for i in range(1, 11):
    print(num * i)
#exercise 5
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if 150 < num < 200:
        print(num)
#exercise 6
num = 75869
count = 0

while num > 0:
    count += 1
    num //= 10

print("Total digits:", count)
#exercise 7
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
#exercise 8
list1 = [10, 20, 30, 40, 50]

for i in reversed(list1):
    print(i)
#exercise 9
for i in range(-10, 0):
    print(i)
#exercise 10
for i in range(5):
    print(i)
else:
    print("Done!")
#exercise 11
for num in range(25, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
#exercise 12
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
#exercise 13
num = int(input("Enter number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"{num}! = {fact}")
# task 4 Return Uncommon Elements of Lists
def uncommon_elements(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    for x in list2:
        if x not in list1:
            result.append(x)
    return result
print(uncommon_elements([1, 1, 2], [2, 3, 4]))         
print(uncommon_elements([1, 2, 3], [4, 5, 6]))         
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  

