# Implement a class Mathematician which is a helper class for doing math operations on lists

# The class doesn't take any attributes and only has methods:

# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:
    def square_nums(self,nums:list):
        squared = list()
        for i in nums:
            squared.append(i**2)
        return squared

    def remove_positives(self,nums:list):
        negatives = list()
        for i in nums:
            if i < 0:
                negatives.append(i)
        return negatives
    
    def filter_leaps(self, dates: list):
        leaps_list = []
        for i in dates:
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                leaps_list.append(i)
            else: 
                pass
        return leaps_list
        



m = Mathematician()
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

# '''

# class Mathematician:

#     pass

 

# m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

# '''