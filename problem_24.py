#Task 2:Recursive function :Factorial Utility
def factorial(n):
    if(n<0):
        print("You enetred a negative number")
    else:    
        if(n==1 or n==0):
            return 1
        return (n)*factorial(n-1)

print(factorial(-3))
print(factorial(5))
print(factorial(0))