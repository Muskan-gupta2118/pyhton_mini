#bank system with encapsulation and validation
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Rahul", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())