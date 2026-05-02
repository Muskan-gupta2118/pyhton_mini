#Multiple inheritance
class Father:
    def money(self):
        print("Father has money")


class Mother:
    def skills(self):
        print("Mother has cooking skills")


class Child(Father, Mother):
    def show(self):
        print("Child inherits both")


c = Child()
c.money()
c.skills()
c.show()