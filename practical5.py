
age_min = 18
age_max = 65
income_min = 100
income_high = 2000

case = input('''Доброго дня, шановний клієнте! Напишіть "так", якщо бажаєте отримати кредит 
або "ні", якщо він вам не потрібен ''')
if case.lower() == "так":
    accept = True
elif case.lower() == "ні":
    accept = False
    print("Приходьте, коли знадобиться!")
else:
    print("Спробуйте ще раз!")

while accept == True:
    first_name = input ("Введіть ваше ім'я: ")
    last_name = input ("Введіть ваше прізвище: ")
    age = input ("Введіть ваш вік: ")
    income = input ("Введіть ваш заробіток (у $): ")
    cl_info = input(f"Все вірно? Вас звуть {first_name} {last_name}, вам {age} і ваш заробіток {income}$?")
    if cl_info.lower() == "так":
        approve = True
        if int(age) >= age_min and int(income) >= income_min and int(income) < income_high:
            print("Вітаю, ви оформили кредит!")
            break
        elif int(age) < age_min or int(income) < income_min:
            print("Приходьте наступного разу!")
            break
        elif int(age) >= age_min and int(income) >= income_min and int(income) > income_high:
            print("Вітаю, ви оформили супер-кредит!")
            break
        else: 
            break
    elif cl_info.lower() == "ні":
        approve = False
    else:
        print("Спробуй ще раз!")
        