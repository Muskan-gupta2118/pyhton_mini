#mini.project:Simple Inventory system
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} | ₹{self.price} | {self.category}"

    def __add__(self, other):
        return self.price + other.price


# Inventory Class
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                print(f"{name} removed")
                return
        print("Product not found")

    def get_total_value(self):
        total = 0
        for p in self.products:
            total += p.price
        return total

    def show_all_products(self):
        print("\nAll Products:")
        for p in self.products:
            print(p)
# Store Class
class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = int(input("Enter price: "))
        category = input("Enter category: ")

        product = Product(name, price, category)
        self.inventory.add_product(product)

    def show_summary(self):
        print(f"\nStore: {self.store_name}")
        print("Total Products:", len(self.inventory.products))
        print("Total Value:", self.inventory.get_total_value())

store = Store("My Store")

# Adding 3 products
for _ in range(3):
    store.add_new_product()

# Show all products
store.inventory.show_all_products()

# Show summary
store.show_summary()

# Operator overloading test
p1 = store.inventory.products[0]
p2 = store.inventory.products[1]

print("\nCombined Price using + :", p1 + p2)   