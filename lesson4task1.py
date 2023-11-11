# String manipulation

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.

# Sample String: 'helloworld'

# Expected Result : 'held'

# Sample String: 'my'

# Expected Result : 'mymy'

# Sample String: 'x'

# Expected Result: Empty String
# Tips:

# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a string and negative indexing to get the last characters

def stringlen(user_string):
    two_simbols = 0
    if len(user_string) < 2:
        return
    else: 
        two_simbols = user_string[0:2] + user_string[-2:]
        print(two_simbols)

my_string = input("Введість строку: ")
stringlen(my_string)