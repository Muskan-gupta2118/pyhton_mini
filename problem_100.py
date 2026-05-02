#public member access
class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_details(self):
        print(self.name, self.price)


c1 = Car("BMW", 5000000)

print(c1.name)   # public access
c1.show_details()