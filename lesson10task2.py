# Write a function that takes in two numbers from the user via input(), 
# call the numbers a and b, and then returns the value of squared a divided by b, 
# construct a try-except block which raises an exception if the two values given by the input function were not numbers, 
# and if value b was zero (cannot divide by zero).    

def my_func(a, b):
    try:
        result = a**2 / b
        print(result)
    except ZeroDivisionError:
        print("Dont divide by 0!")
    except TypeError:
        print("Input should be an int!")
   
user_num1 = input("Enter the first number: ")
user_num2 = input("Enter the secound number: ")
try:
    user_num1 = int(user_num1)
    user_num2 = int(user_num2)
except ValueError:
    pass

my_func(user_num1,user_num2)