#Employee salary increment
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increment(self, percent):
        self.salary += self.salary * percent / 100


e = Employee("Aman", 20000)
e.increment(10)

print(e.salary)