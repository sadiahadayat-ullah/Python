# Program: Payment System using Abstraction

# Description: Demonstrates abstraction by defining a common
# payment method that is implemented differently by child classes.

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):

    def pay(self):
        print("Payment successful using Credit Card")

class Cash(Payment):

    def pay(self):
        print("Payment successful using Cash")

credit_card = CreditCard()
cash = Cash()

credit_card.pay()
cash.pay()