# Extend Phonebook application

# Functionality of Phonebook application:

# Add new entries 
# Search by first name 
# Search by last name 
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
 

# The first argument to the application should be the name of the phonebook. 
# Application should load JSON data, if it is present in the folder with application, else raise an error. 
# After the user exits, all data should be saved to loaded JSON.

import json
my_list = []
variable = 0


print("Доброго дня, користувачу!")
while True:
    user_ans = input("""Оберіть, що ви хочете зробити:
                     1. Знайти особу по імені; 
                     2. Знайти особу за прізвищем; 
                     3. Знайти особу за повним ім'ям;
                     4. Знайти особу за телефонним номером;
                     5. Знайти особу за містом проживання;
                     6. Видалити запис за вказаним номером телефону;
                     7. Оновити дані за номером телефону;
                     8. Вийти з додатку: """)
    try:
        user_ans = int(user_ans)
    except ValueError:
        print("Введіть число від 1 до 8!")

# Search by first name
    if user_ans == 1:
        with open("telephone_num.json", "r") as file:
            my_answ = input("Введіть імя особи: ")
            data = json.load(file)
            for i in data:
                for key, value in i.items():
                    if i[key] == my_answ and key == "First_name":
                        print("Ось данні про особу що ви просили: ")
                        print(i)
                        variable += 1
                        break
                    elif i[key] != my_answ: 
                        pass
            if variable > 0:
                variable = 0
                pass
            else:
                print("Данних про цю особу не знайдено!")
# Search by last name 
    elif user_ans == 2:
        with open("telephone_num.json", "r") as file:
            my_answ = input("Введіть прізвище особи: ")
            data = json.load(file)
            for i in data:
                for key, value in i.items():
                    if i[key] == my_answ and key == "Last_name":
                        print("Ось данні про особу що ви просили: ")
                        print(i)
                        variable += 1
                        break
                    elif i[key] != my_answ: 
                        pass
            if variable > 0:
                variable = 0
                pass
            else:
                print("Данних про цю особу не знайдено!")

                        
# Search by full name       
    elif user_ans == 3:
        with open("telephone_num.json", "r") as file:
            my_answ = input("Введіть повне ім'я особи: ")
            data = json.load(file)
            for i in data:
                for key, value in i.items():
                    if i[key] == my_answ and key == "Full_name":
                        print("Ось данні про особу що ви просили: ")
                        print(i)
                        variable += 1
                        break
                    elif i[key] != my_answ: 
                        pass
            if variable > 0:
                variable = 0
                pass
            else:
                print("Данних про цю особу не знайдено!")

# Search by telephone number
    elif user_ans == 4:
        with open("telephone_num.json", "r") as file:
            my_answ = input("Введіть номер особи у форматі (+380ххххххххх): ")
            data = json.load(file)
            for i in data:
                for key, value in i.items():
                    if i[key] == my_answ and key == "Number":
                        print("Ось данні про особу що ви просили: ")
                        print(i)
                        variable += 1
                        break
                    elif i[key] != my_answ: 
                        pass
            if variable > 0:
                variable = 0
                pass
            else:
                print("Данних про цю особу не знайдено!")

# Search by city or state
    elif user_ans == 5:
        with open("telephone_num.json", "r") as file:
            my_answ = input("Введіть місто проживання особи: ")
            data = json.load(file)
            for i in data:
                for key, value in i.items():
                    if i[key] == my_answ and key == "city":
                        print("Ось данні про особу що ви просили: ")
                        print(i)
                        variable += 1
                        break
                    elif i[key] != my_answ: 
                        pass
            if variable > 0:
                variable = 0
                pass
            else:
                print("Данних про цю особу не знайдено!")

# Delete a record for a given telephone number               
    elif user_ans == 6:
        my_answ = input("Введіть номер особи у форматі (+380ххххххххх), запис про яку хочете видалити: ")
        with open("telephone_num.json", "r+") as file:
            data = json.load(file)
            for i in data:
                if i not in my_list:
                    my_list.append(i)
        for i in my_list:
            for key, value in i.items():
                try:
                    if value == my_answ:
                        my_list.pop(my_list.index(i))
                except KeyError:
                    pass
        with open("telephone_num.json", "w+") as file:
            data = json.dump(my_list, file)

# Update a record for a given telephone number  
    elif user_ans == 7:
        my_answ = input("Введіть номер особи у форматі (+380ххххххххх), запис про яку хочете змінити: ")
        with open("telephone_num.json", "r+") as file:
            data = json.load(file)
            for i in data:
                if i not in my_list:
                    my_list.append(i)
        for i in my_list:
            for key, value in i.items():
                try:
                    if i[key] == my_answ:
                        second_answ = input("Номер знайдено, оберіть що ви хочете змінити: ім'я, прізвище, номер телефону. ")
                except KeyError:
                    pass
        if second_answ.lower() == "ім'я":
            third_answ = input("Введіть нове ім'я: ")
        elif second_answ.lower() == "прізвище":
            third_answ = input("Введіть нове прізвище: ")
        elif second_answ.lower() == "номер телефону":
            third_answ = input("Введіть нове прізвище: ")   
        else:
            print("Невідома команда") 
            break
        for i in my_list:
            for key, value in list(i.items()):
                try:
                    if i[key] == my_answ and second_answ == "ім'я": 
                        i["First_name"] = third_answ
                        i["Full_name"] = third_answ + " " + i["Last_name"]
                    elif i[key] == my_answ and second_answ == "прізвище":
                        i["Last_name"] = third_answ 
                        i["Full_name"] = i["First_name"] + " " + third_answ
                    elif i[key] == my_answ and second_answ == "номер телефону":
                        i["Number"] = third_answ  
                    else:
                        pass
                except KeyError:
                    pass
        with open("telephone_num.json", "w+") as file:
            data = json.dump(my_list, file)
        print("Запис успішно змінено") 
        
# An option to exit the program    
    elif user_ans == 8:
        print("Дякуємо за використання додатку, гарного дня!")
        break

