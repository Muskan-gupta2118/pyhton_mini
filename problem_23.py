#Task 1:Basic function:Price After Discount
def apply_discount(price,discount_percent=5):
    if(discount_percent>=60):
        print("there is no discount more than 60")
    else:    
        after_price=price-price*discount_percent/100
        print ("the price after discount is ",after_price)
        return after_price
print(apply_discount(1000,10))
print(apply_discount(1000,60)) 
print(apply_discount(500))    