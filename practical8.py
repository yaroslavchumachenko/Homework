#Ви - власник онлайн магазину канцтоварів. Кожному 3-му покупцю ви обіцяєте в подарунок ручку до замовлення, а кожному 5-му - лінійку.

system = True
while system == True:
    user_number = input ("Введіть кількість юзерів на сайті:")
    if user_number.isdigit():
        for i in range(1,int(user_number),1):
            if i%5 == 0 and i%3 == 0:
                print(f"Вітаємо, ви {i} покупець! Ви виграли і ручку, і лінійку!")
            elif i%5 == 0:
                print(f"Вітаємо, ви {i} покупець! Ви виграли лінійку!")
            elif i%3 == 0:
                print(f"Вітаємо, ви {i} покупець! Ви виграли ручку до замовлення!")
            else:
                print(f"Вітаємо, ви {i} покупець!")
        break
    else:
        print("Ви ввели не цифру!")
    