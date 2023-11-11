#Words combination

#Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.

import random
i = 0
word = input("Введіть слово: ")
word_temp = word
new_text = ""
while i < 5:
    for char in word_temp:
        char = random.randint(0, len(word_temp)-1)
        new_text += word_temp[char]
        word_temp = word_temp[0:char] + word_temp[char+1:]
# if word_temp[char] in new_text:
#            pass
#        else:
#           new_text += word[char]
    print(new_text)
    word_temp = word
    new_text = ""
    i+=1
i_ind = 0

# word = input("Введіть слово: ")
# for i in range(len(word)):
#     i = random.randint(0, len(word))
#     if i == i_ind:
#         pass
#     else:
#         print(i)




# for i in string:
#     rand_string = list(string)
#     random.shuffle(rand_string)
