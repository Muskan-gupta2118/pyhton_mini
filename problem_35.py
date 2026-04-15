#Task_6:Read File safely(Error handling inside file handling only)
import os

filename = input("Enter filename: ")

if os.path.exists(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line.strip())
else:
    print("File not found. Please check the filename.")