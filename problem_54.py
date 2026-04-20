#Simple inheritance
class Parent:
    def show(self):
        print("This is parent")

class Child(Parent):
    def display(self):
        print("This is child")

c = Child()
c.show()
c.display()