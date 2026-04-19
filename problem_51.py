#private member
class Student:
    def __init__(self, name, age):
        self.name = name        # public
        self.__age = age        # private variable

    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}")

    def get_age(self):          # public method to access private
        return self.__age


# object
s1 = Student("Muskan", 20)

# public access
print(s1.name)

# ❌ direct access (error dega)
# print(s1.__age)

# ✅ correct way
print(s1.get_age())

s1.display()