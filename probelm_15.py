#Task_01-product collection(Lists & tuple)

named_products=["apple","banana","mango","papaya","watermelon","kiwi"];

sample_products1=('apple', 5 , 'fruit');
smaple_product2=('banana' ,2, 'fruit');
sample_product3=('mango', 7, 'fruit');
sample_product4=('papaya' , 1, 'fruit');
sample_product5=('watermelon' , 3 , 'friut');
smaple_product6=('kiwi' , 10 , 'fruit');

print(named_products[1])
print(named_products[5])

named_products.append(["grapes","guava"])
print(named_products)
#optional
product_list= list(sample_products1)
product_list[1]=6
sample_products1=tuple(product_list)
print(sample_products1)




