# The valid phone number program.

# Make a program that checks if a string is in the right format for a phone number. 
# The program should check that the string contains only numerical characters and is only 10 characters long. 
# Print a suitable message depending on the outcome of the string evaluation.

def valid_number(number):
    x = number.isdigit()
    if x:
        if len(number) > 10:
            print("Your number longer than 10 symbols!")
        elif len(number) < 10:
            print("Your number is to short!")
        else:
            print("Your number is valid!")
    else:
        print("It isn't a number!")

my_string = input("Enter your number: ")
valid_number(my_string)