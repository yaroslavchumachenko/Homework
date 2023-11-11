# The math quiz program.

# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.
question = input("Cкільки буде 77+33?: ")
def quizz(user_ans):
    if user_ans == "110":
        print("Вірно!")
    else:
        print("Не вірно!")

quizz(question)