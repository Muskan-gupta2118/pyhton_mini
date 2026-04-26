#object refrence
class A:
    def __init__(self, x):
        self.x = x

obj1 = A(10)
obj2 = obj1

obj2.x = 20

print(obj1.x)