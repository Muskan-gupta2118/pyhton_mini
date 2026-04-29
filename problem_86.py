# Abstraction
from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


# Subclass 1
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid {amount} using Credit Card")


# Subclass 2
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid {amount} using UPI")


# Testing
p1 = CreditCardPayment()
p2 = UPIPayment()

p1.process_payment(1000)
p2.process_payment(500)