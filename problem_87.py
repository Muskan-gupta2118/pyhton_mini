#Magic method & opeartor overloading
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # 1. __str__ method
    def __str__(self):
        return f"Product(Name: {self.name}, Price: {self.price}, Category: {self.category})"

    # 2. Operator Overloading (+)
    def __add__(self, other):
        return self.price + other.price


# Creating objects
p1 = Product("Laptop", 50000, "Electronics")
p2 = Product("Mobile", 20000, "Electronics")

# Testing __str__
print(p1)
print(p2)

# Testing operator overloading
total_price = p1 + p2
print("Total Price:", total_price)