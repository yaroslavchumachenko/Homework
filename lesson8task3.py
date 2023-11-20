# A simple calculator.

# Create a function called make_operation, which takes in a simple arithmetic operator 
# as a first parameter (to keep things simple let it only be '+', '-' or '*') 
# and an arbitrary number of arguments (only numbers) as the second parameter. 
# Then return the sum or product of all the numbers in the arbitrary parameter. For example:

# the call make_operation('+', 7, 7, 2) should return 16
# the call make_operation('-', 5, 5, -10, -20) should return 30
# the call make_operation('*', 7, 6) should return 42  

def make_operation(operation_char, *numbers):
    result = 0
    if operation_char == "+":
        for i in numbers:
            result += i
    elif operation_char == "-":
        for i in numbers:
            result -= i
    elif operation_char == "*":
        result += numbers[0]
        for i in numbers:
            if i == result:
                pass
            else:
                result = result*i
    print(result)


make_operation("*", 5, 6, 7)
    