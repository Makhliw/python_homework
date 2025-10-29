LESSON -3 
#task 1 - Create a list containing five different fruits and print the third fruit.
fruits = ["apple", "banana", "cherry", "orange", "mango"]
print("Third fruit:", fruits[4])

#task 2 -Create two lists of numbers and concatenate them into a single list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Combined list:", combined)

#task 3 - Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [10, 20, 30, 40, 50, 60, 70]
new_list = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print("Extracted list:", new_list)

#task 4 - Create a list of your five favorite movies and convert it into a tuple.
movies = ["Inception", "Interstellar", "Avatar", "Titanic", "Gladiator"]
movies_tuple = tuple(movies)
print("Tuple:", movies_tuple)

#task 5 - Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["Tashkent", "Paris", "London", "Berlin"]
if "Paris" in cities:
    print("Paris is in the list!")
else:
    print("Paris is not in the list.")
#task 5 - Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["Tashkent", "Paris", "London", "Berlin"]
if "Paris" in cities:
    print("Paris is in the list!")
else:
    print("Paris is not in the list.")

#task 6 - Create a list of numbers and duplicate it without using loops.
numbers = [1, 2, 3]
duplicated = numbers * 2
print("Duplicated list:", duplicated)

#task 7 - Given a list of numbers, swap the first and last elements.
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print("After swapping:", nums)

#task 8 - Create a tuple of numbers from 1 to 10 and print 
# a slice from index 3 to 7.
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Slice from 3 to 7:", nums[3:8])

#task 9 - Create a list of colors and count how many times "blue" appears in the list.
colors = ["blue", "red", "green", "blue", "yellow", "blue"]
count_blue = colors.count("blue")
print("Blue appears:", count_blue, "times")

#task 10 - Write a Python program to generate 
#a random password containing letters, digits, and special characters.
import random
import string
length = 10
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)

#task 11 - Create two tuples of numbers and merge them into a single tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged = tuple1 + tuple2
print("Merged tuple:", merged)

#task 12 - Given a list and a tuple, find and print their lengths.
my_list = [10, 20, 30]
my_tuple = (5, 10, 15)
print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

#Task 
nums = (1, 2, 3, 4, 5)
converted = list(nums)
print("Converted to list:", converted)

#task 14 - Given a tuple of numbers, find and print the maximum and minimum values.
values = (3, 7, 1, 9, 4)
print("Max:", max(values))
print("Min:", min(values))

#task 15 - Create a tuple of words and print it in reverse order.
words = ("apple", "banana", "cherry")
reversed_tuple = words[::-1]
print("Reversed tuple:", reversed_tuple)

