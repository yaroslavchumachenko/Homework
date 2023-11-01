#Існують такі типи даних як string, float, integer(int), bool
my_string = "Hello Git!"
my_number = 27
my_boolean = True
#Для перенесення строк використовується \
my_long_string = "toooooooooooooooooooooooooooo loooooooooooo\
    ong sring"
#Можна не використовувати \ для переноси 
triple_string = """hello
git
hub"""
# / - ділення, // ділення без остачі, % ділення із залишком 
#Форматування стічок | String formatting
username = "Yaroslav"
surname = "Chumachenko"
group = "PYTHON 118"
# f-string
print(f"Hi {username} {surname}! Welcome to the {group} group!")

# format()
my_string = "Hi {username} {surname}! Welcome to the {group} group!"
my_string.format(username="Yaroslav", surname="Chumachenko", group="PYTHON 118")

# %s, %d (Використовувася у Python 2.0)

#string concatenation
"hello" + "world"

user = username + surname

#Slicing | Розбиття на індекси 

group = "PYTHON 118"

# [start:stop] like [1:5] the last symbol isn't signed 
# [:stop] from first to the last position
# [start:stop:step]

group.split(" ")
#Creates list with "Python" and "118"

# replace func
my_string = "Hello World!"
my_string = my_string.replace("!", "")

#is-else
if username == "Yaroslav":
    pass #skip this iteration 
elif username != "Yaroslav":
    pass
else:
    print("other user")
username = input("Print your username:")
#you can check definite symbor by typing if username[indecs]

# Also we can use "and" "or" to check many conditions
# Source code

# while & for loops - while some statement is True/False - iterrate code 

for element in username:
    pass
for i in range(len(username)):
    username[i] = 0
my_number = 0
while my_number != 10:
    my_number += 1


my_numb = 5
my_str = "5"
if my_numb == int(my_str):
    pass