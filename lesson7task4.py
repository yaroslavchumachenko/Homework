# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
# Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,

days = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
number = 1
date_day = dict()
for i in days:
    date_day[number] = i
    number +=1
print(date_day)
# date_day = {
#     1:"Monday",
#     2:"Tuesday",
#     3:"Wednesday",
#     4:"Thursday",
#     5:"Friday",
#     6:"Saturday",
#     7:"Sunday"
# }

new_day = [{key:value} for value,key in date_day.items()]

day_date = dict()
for i in new_day:
    day_date.update(i)

print(day_date)