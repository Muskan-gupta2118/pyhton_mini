n=int(input("Enter any number : "))
for i in range(2,n):
    if(n%i==0):
        print("Given number is not a prime number.")
        break
else:
        print("Given number is a prime number")    