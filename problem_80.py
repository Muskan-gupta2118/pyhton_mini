#overriding and default arguments
class A:
    def show(self, x=1):
        print("A", x)

class B(A):
    def show(self, x=2):
        print("B", x)

obj = B()
obj.show()