#Task_1:Basic class and object creation
class product:
    def __init__(self,name,price,category):
       self.name=name;
       self.price=price;
       self.category=category
    def get_info(self):
        print(f"the name of the product is :{self.name} at price of {self.price} from {self.category}")   
Apple=product("Apple",120,"Fruit")
Apple.get_info()
copy=product("Copy",80,"stationary")
copy.get_info()