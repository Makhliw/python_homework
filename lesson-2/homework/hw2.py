#lesson 2
#task1 - Write a Python program to ask for a user's name and year of birth,
#then calculate and display their age.
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = 2025
age = current_year - year_of_birth
print(f"Hello, {name}! You are {age} years old.")

#task2 - Extract car names from the following text:
txt = "LMaasleitbtui"
car_name = txt[0] + txt[2] + txt[4] + txt[6] + txt[8] + txt[10] + txt[12]
print("Extracted car name:", car_name)

#task 3 - Extract car names from the following text:
txt = "MsaatmiazD"
car_name = txt[0] + txt[2] + txt[4] + txt[6] + txt[8]
print("Extracted car name:", car_name)

#task 4 - Extract the residence area from the following text:
txt = "I'am John. I am from London"
area = txt.split("from")[-1].strip()
print("Residence area:", area)

#task 5 - Write a Python program that takes a user input string 
# and prints it in reverse order.
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# task 6 - Write a Python program that 
# counts the number of vowels in a given string.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print("Number of vowels:", count)

#task 7 -Write a Python program that takes a list of numbers 
#as input and prints the maximum value.
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
print("Maximum value:", max(numbers))

# task 8 -Write a Python program that checks if a given word is a palindrome 
# (reads the same forward and backward).
word = input("Enter a word: ")
if word == word[::-1]:
      print("It's a palindrome!")
else:
      print("Not a palindrome.")

#task 9 - Write a Python program that extracts and prints 
# the domain from an email address provided by the user.
email = input("Enter your email: ")
domain = email.split("@")[-1]
print("Email domain:", domain)

#task 10 - Write a Python program to generate 
#a random password containing letters, digits, and special characters.
import random
import string
length = 10
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
