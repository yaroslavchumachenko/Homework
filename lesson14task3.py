# Write a decorator "arg_rules" that validates arguments passed to the function.

# A decorator should take 3 arguments:

# max_length: 15

# type_: str

# contains: [] - list of symbols that an argument should contain

# If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.



def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(args):
            result = args
            for i in contains:
                if i in result:
                    is_cont = True
                else:
                    is_cont = False

            if type(result) == type_ and len(result) <= max_length and is_cont == False:
                return func(args)
            elif is_cont == True:
                print("Prohibited sympols!")
                return False
            elif len(result) > max_length:
                print("Too many symbols!")
                return False
            elif type(result) != type_:
                print("Wrong Type!")
        return wrapper
    return decorator


 

@arg_rules(type_=str, max_length=15, contains=['05', '@'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"


# assert create_slogan('johndoe05@gmail.com') is False

# assert create_slogan('05years') is False

# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

# assert create_slogan('SSH') == 'SSH drinks pepsi in his brand new BMW!'