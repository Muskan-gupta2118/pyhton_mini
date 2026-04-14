#Task 5 :Using filter():Filter Expensive Products
#1.
price=list(filter(lambda x:x>500,[100,250,400,1200,50,2000,850]))
print(price)

#2.
price2=list(filter(lambda x:x<=500,[100,250,400,1200,50,2000,850]))
print(price2)