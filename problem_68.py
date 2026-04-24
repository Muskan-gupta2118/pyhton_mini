#simple shoppping item
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(self.name, self.price)


i = Item("Pen", 10)
i.display()