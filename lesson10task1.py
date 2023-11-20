# Write a function called oops that explicitly raises an IndexError exception when called. 
# Then write another function that calls oops inside a try/except state­ment to catch the error. 
# What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    raise IndexError
my_list = [*range(1,10)]
def my_func(x):
    try:
        print(my_list[x])
    except IndexError:
        oops()
    except KeyError:
        raise Exception

my_func(11)
