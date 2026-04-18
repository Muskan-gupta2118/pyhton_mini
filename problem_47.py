class product:
    def __init__(self,name,price,category):
       self.name=name;
       self.price=price;
       self.category=category
    def get_info(self):
        print(f"the name of the product is :{self.name} at price of {self.price} from {self.category}")
class ElectronicProduct(product):
    def __init__(self,name,price,category,warranty_year):
        super().__init__(name,price,category)
        self.warranty_year=warranty_year
    def get_info(self):
        print(f"the name of the product is :{self.name} at price of {self.price} from {self.category}with warranty till {self.warranty_year}")
Apple=product("Apple",120,"Fruit")
Apple.get_info()
laptop=ElectronicProduct("Apple",200000,"Laptop",2045)  
laptop.get_info()         