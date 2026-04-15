#Task_4.py
1.
with open('sales_data.txt','r') as f:
    content=f.read()
    print(content)
2.
with open('sales_data.txt','r') as f:
    num_list=[]
    for i in f:
        num_list.append(int(i.strip()))
    print(num_list)
3.
print(f"total sales : {sum(num_list)}")
print(f"highest sale : {max(num_list)}")
print(f"lowest sale : {min(num_list)}")
print(len(num_list))
print(f"Average sale : {sum(num_list)/len(num_list)}")