# The name check.

# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
# The program should check if your input is equal to the stored name even if the given name has another case, 
# e.g., if your input is “Anton” and the stored name is “anton”, it should return True.

name = "yaroslav"

def isName (user_name):
    if user_name.lower() == name:
        return True
    else: 
        return False

my_name = input("Enter your name: ")
print(isName(my_name)) 