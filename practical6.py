post_status = True
pass_status = True 

print("Вітаю, шановний користувач! Будь ласка, введіть ваш вік, електронну пошту та пароль для реєстрації.")
user_age = input("Введіть свій вік: ")
user_email = input("Введіть свій email(він має бути у форматі post@gmail.com): ")
while post_status == True:
    if "@gmail.com" in user_email:
        print("Пошта підходить! \n")
        break
    else:
        print('Пошта має містити "@gmail.com"! Спробуйте ще раз!')
while pass_status == True:
    user_password = input("Введіть пароль: ")
    if len(user_password) <= 5:
        print("Пароль надто которткий! Спробуйте ще раз!")
    else: 
        print("Пароль підходить!")
        break
    