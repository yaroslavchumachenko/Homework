# Ви - настирливий продавець і коли хтось відвідує ваш сайт онлайн-магазину, ви запитуєте 5 разів у користувача, чи потрібно йому передзвонити. На 6-ий раз ви нарешті лишаєте покупця в спокої і бажаєте йому гарних покупок.
for i in range(5):
    user_ans = input("Вам передзвонити? Введіть так або ні: ")
    if user_ans.lower() == "так":
        print("Ми вам передзвонимо!")
        break
    elif i <=5 : 
        pass
    else:
        print("Гарного дня і хороших покупок!")