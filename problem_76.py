#multiple attribute trap
class Demoo:
    def __init__(self, lst=[]):
        self.lst = lst

    def add(self, val):
        self.lst.append(val)

d1 = Demoo()
d2 = Demoo()

d1.add(1)
d2.add(2)

print(d1.lst)
print(d2.lst)