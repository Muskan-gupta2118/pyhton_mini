#Task4-combined opertion
1.
price_dict={
    'spiral':80,
    'pen':10,
    'A4 paper':20,
    'box':50,
    'color':30,
    'sheet':5
}
product_list=["pen","A4 paper","box","color","sheet","bottle"]
categories=["stationary","stationary","stationary","stationary","stationary","stationary"]
catalog=[]
for i in range(len(product_list)):
    product=product_list[i]
    price = price_dict[product]
    category=categories[i]

    catalog.append((product,price,category))
    
print(catalog)    

2.
category_to_product={}
for product,price,category in catalog:
    if category not in category_to_product:
        category_to_product[category]=[]
    category_to_product[category].append(product);
print(category_to_product)

3.

for category,product in category_to_product.items():
    print(category,":",len(product))