#Task_4:File Reader with Exception Handling
import os
File_name=input("Enter a file name : ")
name=["Muskan","Utkarsh","Naveen"]
try:
      with open(File_name, 'r') as f:
        for i in range(3):
           print(f.readline(),end="")
except FileNotFoundError:
   print("file does not exist") 
else:
   print("File operation attempted")      
