#Task 3:User mwnu(While loop + break/continue)
order_list=[]
while True:
    '''Menu Options:
    1--Add Oder amount to a running list
    2.Show all orders and totals after applying discounts
    q--Quit'''
    choice=input("Enter the character : ")
    if(choice=='1'):
        amount=input("Enter the amount : ")
        order_list.append(amount)
    elif(choice=='2'):
        print("orders :",order_list)    
    elif(choice =='q'):
         break;    
    else:
        print("invalid input! try again ")
        continue


