#Task 2:Process Multiple Orders(for loop)
order_list=[1200,250,800,1750,3000]
total_revenue=0
for i in order_list:
    print(f"for amount : {i}")
    if(i>=2000):
       remain_amount2=i-(i*15/100)
    elif(1500<=i):
       remain_amount2=i-(i*10/100)
    elif(1000<=i):
        remain_amount2=i-(i*7/100)
    elif(i<1000):
        print("There is no discount in that price ")
    else:
        print("You enetr a invalid number!EXIT")    
    print(remain_amount2)
    print(f"Your left amount is :{remain_amount2}")
    print(f"Tax inculding:{tax}%")
    final_amount2=remain_amount2+(remain_amount2*5/100)
    print(f"now you have to pay :{final_amount2}") 
    total_revenue=total_revenue+final_amount2
2.
print(f"Your total revenue is :{total_revenue}")
3.#optional
count=0
for i in order_list:
    if (i>1000):
        count=count+1
print(f"total number of product those get discount from the list is :{count}")

