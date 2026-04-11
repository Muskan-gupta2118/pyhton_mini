#Task3-product pricing(Dictionries)
1.
price_dict={
    'spiral':80,
    'pen':10,
    'A4 paper':20,
    'box':50,
    'color':30,
    'sheet':5
}
2.
price_dict.update({'bottle':70})
print(price_dict.items())
price_dict.pop('spiral')
print(price_dict)
3.
price_values=price_dict.values()
print(price_values)
average_values=sum(price_values)/len(price_values)
print(average_values)
max_price=max(price_dict,key=price_dict.get)
min_price=min(price_dict,key=price_dict.get)
#optional
print("Maximun price product :",max_price ,price_dict[max_price])
print("Minimum price product: ",min_price,price_dict[min_price])
