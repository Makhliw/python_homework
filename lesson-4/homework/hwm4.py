#lesson 4 
## Dictionary Exercises task  1 - Write a Python script to sort 
# (ascending and descending) a dictionary by value.
my_dict = {'a': 10, 'b': 5, 'c': 30}
asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("Ascending:", asc)
desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Descending:", desc)

# Dictionary Exercises task  2 - Write a Python script to add a key to a dictionary.
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print("Updated dictionary:", my_dict)

# Dictionary Exercises task  3 - Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged = {}
for d in (dic1, dic2, dic3):
    merged.update(d)
print("Merged dictionary:", merged)

# Dictionary Exercises task  4 - Write a Python script to generate 
# and print a dictionary that contains a number 
# (between 1 and n) in the form (x, x*x).
n = 5
squares = {x: x**2 for x in range(1, n + 1)}
print("Dictionary with squares:", squares)

# Dictionary Exercises task  5 - Write a Python script to print a dictionary 
# where the keys are numbers between 1 and 15 (both included) 
# and the values are the square of the keys.
squares = {x: x**2 for x in range(1, 16)}
print("Squares from 1 to 15:", squares)

# Set Exercises task 1 - Write a Python program to create a set.
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Set Exercises task 2 - Write a Python program to iterate over sets.
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)

# Set Exercises task 3 - Write a Python program to add member(s) to a set.
my_set = {"red", "green"}
my_set.add("blue")       # add one
my_set.update(["black", "white"])  # add multiple
print("Updated set:", my_set)

# Set Exercises task 4 - Write a Python program to remove item(s) from a given set.
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")  # raises error if not present
print("After removing banana:", my_set)

# Set Exercises task 5 - Write a Python program to remove an item 
# from a set if it is present in the set.
my_set = {"apple", "banana", "cherry"}
my_set.discard("banana")  # no error if not found
print("After discard:", my_set)


