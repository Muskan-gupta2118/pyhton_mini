cart_list=[]
count=0
while(True):
    item=(input("Enter the item : "))
    if (item=='q'):
        break;
    
    try:
      float_value=float(item)
      if float_value<0:
         raise ValueError("Negative price")
      cart_list.append(float_value)
      count+=1
    except ValueError :
       print("Invalid input")
print(count)
total=0
for i in cart_list:
   total=total+i
print(total)