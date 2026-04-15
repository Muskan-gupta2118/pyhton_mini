#Read files in Different ways

f=open('sales_data.txt','r')
content=f.read()
print(content)
f.close()
f=open('sales_data.txt','r')
read1=f.readline()
print(read1)
f.close()
f=open('sales_data.txt','r')
read_all=f.readlines()
print(read_all)
f.close()
with open('sales_data.txt', 'r') as f:
    num_list = []
    for line in f:
        num_list.append(int(line.strip()))
print(num_list)