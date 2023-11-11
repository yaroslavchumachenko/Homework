# Using python as a calculator.

# Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 

# Addition
# Subtraction
# Division
# Multiplication
# Exponent (Power)
# Modulus
# Floor division

a = input("Print the first digit: ")
a = int(a)
b = input("Print the second digit: ")
b = int(b)
char = input("Choose: +|-|/|*|**|%|//")

if char == "+":
    print(a+b)
elif char == "-":
    print(a-b)
elif char == "/":
    print(a/b)
elif char == "*":
    print(a*b)
elif char == "**":
    print(a**b)
elif char == "%":
    print(a%b)
elif char == "//":
    print(a//b)
else:
    print("Wrnong character!")