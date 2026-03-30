def even_function(value):
    if value%2==0:
        return True;
#iterable_list=[1,2,3,4,5,6,7,8,9,22,33,44]
print(list(filter(lambda x:x%2==0,[2,3,4,5,6,7,8,9,10])))