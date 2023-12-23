# School

# Make a class structure in python representing people at school. Make a base class called Person, a class called Student, and another one called Teacher. 
# Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not. 
# For example, the name should be a Person attribute, while salary should only be available to the teacher.



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def breath(self):
        return True
    
    def think(self):
        return True

class Student(Person):
    def __init__(self, name, age, class_, grades: list):
        super().__init__(name, age)
        self._class = class_
        self.grades = grades

class Teacher(Person):
    def __init__(self, name, age, work_hours, salary):
        super().__init__(name, age)
        self.work_hours = work_hours
        self.salary = salary

    
