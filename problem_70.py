#bank account
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Not enough balance")


a = Account(1000)
a.deposit(500)
a.withdraw(200)

print(a.balance)