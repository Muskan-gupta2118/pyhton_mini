#REctangle area and perimeter
class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l + self.w)


r = Rectangle(4, 5)
print(r.area())
print(r.perimeter())