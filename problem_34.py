#Task_5: Create product Info Fie(User input)
product1=input("Enter the product name : ")
product1_price=(input("Enter the price for product : "))
product2=input("Enter the product name : ")
product2_price=(input("Enter the price for product : "))
product3=input("Enter the product name : ")
product3_price=(input("Enter the price for product : "))
with open('product.txt','w') as f:
    f.write(product1 + '|' + product1_price + '\n')
    f.write(product2 + '|' + product2_price + '\n')
    f.write(product3 + '|' + product3_price + '\n')

with open('product.txt','r') as f:
    print(f.read())