print("Доброго дня, шановний клієнте!")
user_age = input("Вкажіть, скільки вам років?: ")


user_pref = input("""Оберіть товар, який ви бажаєте придбати:
      1. Алкогольні напої;
      2. Енергетичні напої;
      3. Усе інше. \n""")


if int(user_pref) == 1 and int(user_age) >= 18 :
    print("Продано!")
elif int(user_pref) == 2 and int(user_age) >= 14:
    print("Продано!")
elif int(user_pref) == 3 and int(user_age) >= 0:
    print("Продано!")
elif int(user_age) <= 0:
    print("Спробуйте ще раз!")
else:
    print("Повертайся, коли підростеш")



