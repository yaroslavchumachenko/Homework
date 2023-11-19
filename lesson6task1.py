# The greatest number

# Write a Python program to get the largest number from a list of random numbers with the length of 10

# Constraints: use only while loop and random module to generate numbers

from random import randint


i = 0
list_of_numbers = []

while i < 10:
    list_of_numbers.append(randint(0,99))
    i+=1

sorted_list = sorted(list_of_numbers)
print(f"The highest number is: {sorted_list[-1]}")

