#polymorphism
class product:
    def __init__(self,name,price):
        self.name=name;
        self.price=price

    def get_info(self):
        print("products: ",self.name,self.price)

class laptop(product):
    def get_info(self):
        print("Laptop : ",self.name,self.price)

class Mobile(product):
    def get_info(self):
        print(f"Mobile Name: {self.name}, Price: {self.price}")


# Creating objects
p1 = laptop("HP", 60000)
p2 = Mobile("Samsung", 30000)

# Polymorphism using loop
products = [p1, p2]

for item in products:
    item.get_info()                    