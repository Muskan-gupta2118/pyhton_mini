#Task_3:Custom Exception:Age validator
age=int(input("Enter your age : "))
def check_age(age):
    try:
        if (age>120 or age<0):
            raise ValueError 
    except ValueError:
        print("Invalid age")

check_age(age)