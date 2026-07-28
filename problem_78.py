#super() confusion
class A:
    def __init__(self):
        print("Anuu")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

obj = B()