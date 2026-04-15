#Append New Sales
append_data='5000\n 2500\n 1700'
#with open('sales_data.txt', 'a') as f:
 #   f.write(append_data)

with open('sales_data.txt','r')as file:
    lines=file.readline()
    total_lines=len(lines)
    print(total_lines)
