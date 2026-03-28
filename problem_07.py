cart =[{'item':'Apple','cost':5,'quantity':20},
       {'item':'Banana','cost':4,'quantity':15},
       {'item':'Guava','cost':3,'quantity':10}];
def total_cost(cart):
    total=0;
    for i in cart:
        total+=i['cost']*i['quantity'];
    print("The total cost for the item is going to be :",total);   
total_cost(cart)
