# Extracting numbers.

# Make a list that contains all integers from 1 to 100, then find all integers 
# from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

# Constraint: use only while loop for iteration

my_list = [x for x in range(1,101) if x % 7 == 0 and x % 5 != 0]
print(my_list)

# or
i = 0
my_list_sorted = []
my_list = [*range(1,101)]
while i < 100:
    if my_list[i] % 7 == 0 and my_list[i] % 5 != 0:
        my_list_sorted.append(my_list[i])
    i+=1

print(my_list_sorted)