# Make a program that has some sentence (a string) on input and returns a dict 
# containing all unique words as keys and the number of occurrences as values.
word_list = []
word_dict = dict()
my_string_index = 0
word_count = 0
last_index = 0
my_string = input("Enter your string: ")
for i in my_string:
    if i == " " and word_count == 0:
        word_list.append(my_string[0:my_string_index])

        word_count += 1
        last_index = my_string_index + 1 
    elif i == " " and word_count >= 1:
        word_list.append(my_string[last_index:my_string_index])
        last_index = my_string_index + 1
        word_count += 1
        

    my_string_index += 1

for i in word_list:
    if i not in word_dict:
        word_dict[i] = 1
    else:
        word_dict[i] += 1
print(word_dict)



