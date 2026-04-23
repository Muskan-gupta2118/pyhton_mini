#method chaining
class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, x):
        self.value += x
        return self

    def multiply(self, x):
        self.value *= x
        return self


calc = Calculator()
result = calc.add(5).multiply(2).add(3)
print(result.value)