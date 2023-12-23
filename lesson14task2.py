# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function


def stop_words(words: list):
# Тут ми приймаємо список виключень
    def decorator(func):
# Тут ми приймаємо функцію, яку ми хочемо огорнути
        def wrapper(*args):
# Тут ми створюємо обгортку що приймає таку кількість змінних, скільки є у оригінальній функції, тобто ім'я та вік
            result = func(*args)
            for i in words:
                result = result.replace(i, "*")
            return result
        return wrapper
    return decorator
        



 

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str, age: int):

    return f"{name} drinks pepsi in his brand new BMW! And he is {age} years old!"

print(create_slogan("Steve", 18))

assert create_slogan("Steve", 18) == "Steve drinks * in his brand new *! And he is 18 years old!"