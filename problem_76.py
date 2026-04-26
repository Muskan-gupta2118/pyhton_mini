#multiple attribute trap
class Demo:
    def __init__(self, lst=[]):
        self.lst = lst

    def add(self, val):
        self.lst.append(val)

d1 = Demo()
d2 = Demo()

d1.add(1)
d2.add(2)

print(d1.lst)
print(d2.lst)