#The birthday greeting program.

#Write a program that takes your name as input, and then your age as input and greets you with the following:

#“Hello <name>, on your next birthday you’ll be <age+1> years”   

user_age = input("Введіть свій вік: ")
user_name = input("Введіть своє ім'я: ")
birthday = int(user_age) + 1

print(f"Привіт {user_name}, на твій наступний день народження тобі буде {birthday} років! ")