#Task 4 : Loop control with conditions (break and continue)
daily_list=[200,150,0,400,50,-1,300]
day_count=1
Total_sale=0
for i in daily_list:
    print("Day :",day_count)
    if (i==-1):
        print("negative number")
        break;
    elif(i==0):
        continue;
    Total_sale=Total_sale+i
    print(Total_sale)
    day_count=day_count+1
print("Total sale overall :",Total_sale)