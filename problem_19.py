1.
i=int(input("Enter a integer"))
print(f"user entered the amount : {i}")
2.
if(i>=2000):
    remain_amount=i-(i*15/100)
elif(1500<=i):
    remain_amount=i-(i*10/100)
elif(1000<=i):
    remain_amount=i-(i*7/100)
elif(i<1000):
    print("There is no discount in that price ")
else:
    print("You enetr a invalid number!EXIT")    
print(remain_amount)
3.#optional
tax=5
print(f"Your left amount is :{remain_amount}")
print(f"Tax inculding:{tax}%")
final_amount=remain_amount+(remain_amount*5/100)
print(f"now you have to pay :{final_amount}")


