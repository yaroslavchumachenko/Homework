# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def muliply_addition(a, b):
    def addition():
        return a + b * a * b
    return addition()

print(muliply_addition(2,3))