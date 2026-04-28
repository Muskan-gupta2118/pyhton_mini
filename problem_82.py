#overloading in string
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

s = Student("Aman")
print(s)