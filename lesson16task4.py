# Task 4

# Custom exception

# Create your custom exception named 'CustomException', you can inherit from base Exception class, 
#     but extend its functionality to log every error message to a file named 'logs.txt'. Tips: Use __init__ method to extend functionality for saving messages to file

# '''

class CustomException(Exception):

    
    def __init__(self, msg):
        self.msg = msg
        # self.start = 1
        # self.end = 1000

    # def iter(self):
    #     return self
    
    # def next(self):
    #     if self.start >= self.end:
    #         raise StopIteration
    #     else:
    #         self.start += 1

    def __write__(self):
        with open ("logs.txt", "a+") as file:
            data = file.write(f"{self.start}. {self.msg}")

my_error = CustomException("There is no enough space!")

my_error.__write__()

# '''