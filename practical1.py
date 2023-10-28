print("""Необхідно створити пошту у одному з форматів: 
      1. taras.shevchenko@kobzar.com; 
      2. tarshev@kobzar.com
      3. tarasshev@kobzar.com""")
post = None
my_formate = input("Виберіть формат пошти(від 1 до 3): ")
first_name = input("Введіть своє ім'я латиницею: ")
last_name = input("Введіть прізвище латиною: ")

if int(my_formate) == 1:
    post = first_name.lower() + "." + last_name.lower() + "@kobzar.com"
    print(post)
elif int(my_formate) == 2:
    post = first_name[0:3].lower() + last_name[0:4].lower() + "@kobzar.com"
    print(post)
elif int(my_formate) == 3:
    post = first_name.lower() +last_name[0:4].lower() + "@kobzar.com"
else:
    print("wrong result")