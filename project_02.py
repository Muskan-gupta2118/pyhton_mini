from prettytable import PrettyTable
import csv
import os


while True:
    print("Here is your menu select any number-")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show Expenses")
    print("4. delete Expenses")
    print("5. Exit")
    choice=int(input(" Enter the number "))
    

    if choice ==1:
         print("Add expense selected")
         date =input("Entre date (YYYY-MM-DD):")
         category = input("Enter category:")
         amount = input("Enter the amount:")
         description=input("Enter description")

         file_exist = os.path.isfile("expenses.csv")

         with open("expenses.csv","a",newline="")as file:
              writer = csv.writer(file)
              if not file_exist:
                   writer.writerow(["Date","category","Amount","Description"])
              writer.writerow([date,category,amount,description])
         print("Expenses added succecsfully!")  


    elif choice ==2:
         print("view expense selected")
         def view_expenses():
            table= PrettyTable()

            table.field_names = ["Date","Category","Amount","Description"]
            with open("expenses.csv","r") as file:
               reader = csv.reader(file)

              # next(reader)    #skip header
               for row in reader:
                 table.add_row(row)

            print(table) 
         view_expenses()        
        # try:
             # with open("expenses.csv","r") as file:
              #     reader = csv.reader(file)
               #    print("\n-----All Expenses-----")
                #   for row in reader:
                 #       print(f"Date:{row[0]},Category:{row[1]},Amount:{row[2]},Description:{row[3]}")
         #except FileNotFoundError:
             # print("No expenses found yet2")


    elif choice ==3:
         print("Show total selected")
         try:
              total=0
              with open("expenses.csv","r") as file:
                   reader = csv.reader(file)
                   for row in reader:
                        total += float(row[2])
                   print(f"your total expenses is {total}")
         except FileNotFoundError:
              print("NO expenses found yet")


    elif choice ==4:
         try:
              
             with open ("expenses.csv","r") as file:
                   reader = list(csv.reader(file))
             if len(reader) <=1:
                   print("No expenses to delete!")
             else:
                   print("\n----->Expenses<-----")
                   for i in range (1,len(reader)):
                        print(f"{i}.{reader[i]}")  
                   delete_index = int(input("Enter expenses number to delete: "))
                   if 1<=delete_index<len(reader):
                        reader.pop(delete_index)

                        with open("expenses.csv","w",newline="") as file:
                            writer = csv.writer(file)
                            writer.writerows(reader)
                            print("Expenses deleted succesfully!")
                   else:
                           print("Invalid number!")
         except FileNotFoundError:     
              print("No expenses found!")                  



              
          
    elif choice ==5:
         print("Exiting program...")
         break
    else:
         print("Invalid choice Try again.")               

     
