#Task_2:Constrctor and Encapsulation
class product:
    def __init__(self,name,price,category):
       self.name=name;
       self.__price=price;
       self.category=category
    #Getter method   
    def get_price(self):
        print(f"The price of product is : {self.__price}")
    #Setter method
    def set_price(self,new_price):
        self.__price=new_price
        print(f"New price of product is :{self.__price}")    
Apple=product("Apple",120,"Fruit")
Apple.get_price() 
Apple.set_price(210)       