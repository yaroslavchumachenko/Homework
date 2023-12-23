# Doggy age

# Create a class Dog with class attribute 'age_factor' equals to 7. Make __init__() which takes values for a dog’s age. 
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    def __init__(self, age):
        self.age = age
    
    age_factor = 7
    
    def human_age(self):
        human_years = self.age * Dog.age_factor
        return human_years
    
my_dog = Dog(5)
print(my_dog.human_age())