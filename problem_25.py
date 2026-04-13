#Task 3:Lambda function :GST calculator
gst=lambda price:price + (0.18*price)
print(gst(100))


#with discount
gst=lambda price,discount:price + (0.18*price) - (price*discount/100)
print(gst(100,10))