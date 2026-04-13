#Task 4 : Using map ():Apply GST to list of prices
price=list(map(lambda x:x,[100,250,400,50,2000,850]))
print(price)
gst=10
price_with_gst=list(map(lambda x:x+(x*gst/100),[100,250,400,50,2000,850]))
print(price_with_gst)