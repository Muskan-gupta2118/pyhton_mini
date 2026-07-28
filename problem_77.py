#method overriding
class A:
    def show(self):
        print("Praneet")

class B(A):
    def show(self):
        print("yess")

obj = B()
obj.show()