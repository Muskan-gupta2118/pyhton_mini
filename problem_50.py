# public members
class Student:
    def __init__(self, name, age):
        self.name = name      # public variable
        self.age = age        # public variable

    def display(self):        # public method
        print(f"Name: {self.name}, Age: {self.age}")


# object create
s1 = Student("Muskan", 20)

# accessing public members
print(s1.name)   # directly access
print(s1.age)

s1.display()     # calling public method