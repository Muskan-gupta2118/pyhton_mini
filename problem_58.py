#Employee management(inheritance and overriding)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus   # overriding


e = Employee("Amit", 30000)
m = Manager("Neha", 50000, 10000)

print(e.get_salary())
print(m.get_salary())