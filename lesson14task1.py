# Write a decorator that prints a function with arguments passed to it.

# NOTE! It should print the function, not the result of its execution!

# For example:



# def logger(func):
#     print(func)

 

# @logger

# def add(x, y):

#     return x + y

 

# @logger

# def square_all(*args):

#     return [arg ** 2 for arg in args]


def logger(func):
    print(func)

 

@logger
def add(x, y):

    return x + y

 

@logger
def square_all(*args):

    return [arg ** 2 for arg in args]
