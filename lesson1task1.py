#The Guessing Game.
#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.

import random
answer = False
number = random.randint(1,10)

while answer == False:
    user_number = input("Введіть число від 1 до 10: ")
    if int(user_number) == number:
        print("Ви вгадали!")
        break
    else:
        print("Спробуйте ще раз! \n \n")
        print(number)
