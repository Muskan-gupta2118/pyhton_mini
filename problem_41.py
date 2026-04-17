#Task_2:Bill calculator with Error handling
prices=[120,350,'abc',500,-200,800]
total=0
for i in prices:
    try:
        if not isinstance(i,(int,float)):
            raise TypeError("Not a number")
        elif i < 0:
            raise ValueError("smaller than 0")
        else:
         total+=i
         print(f"Total prices are {total}")
    except TypeError:
        print("Not a number")
    except ValueError as va:
        print(va)
print(total)


