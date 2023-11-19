# Exclusive common numbers.

# Generate 2 lists with the length of 10 with random integers from 1 to 10, 
# and make a third list containing the common integers between the 2 initial lists without any duplicates.

# Constraints: use only while loop and random module to generate numbers
from random import randint
i = 0
list1 = []
list2 = []
list3 = []

while i < 10:
    list1.append(randint(0,10))
    list2.append(randint(0,10))
    i+=1

list1.extend(list2)
list3 = set(list1)
 
print(list3)


