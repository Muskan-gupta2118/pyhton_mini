#class and static method
class Math:

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        return "This is Math class"


print(Math.add(2, 3))
print(Math.info())