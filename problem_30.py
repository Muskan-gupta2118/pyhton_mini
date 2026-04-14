#Task 1:Write Sales Records to a file

with open('sales_data.txt','r')as f :
    content_data=f.read()
    print(content_data)

sales=['1200\n','450\n','980\n','1500\n','3000\n','7000']
with open('sales_data.txt','w')as f:
    f.writelines(sales)    