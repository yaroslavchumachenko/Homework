# Task 1

# Write a Python program to detect the number of local variables declared in a function.



def func(a):
    b = 2
    c = a + b
    x = locals()
    return len(x)


print(func(1))


   
