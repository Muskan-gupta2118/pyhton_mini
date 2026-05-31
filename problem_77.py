#method overriding
class A:
    def show(self):
        print("P")

class B(A):
    def show(self):
        print("Q")

obj = B()
obj.show()