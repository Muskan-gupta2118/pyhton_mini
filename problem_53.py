#encapsulation
class Demo:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"

obj = Demo()

print(obj.public)        #  allowed
print(obj._protected)    #  allowed but not recommended
# print(obj.__private)    error
