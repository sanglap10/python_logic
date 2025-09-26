from abc import ABC, abstractmethod

# This example demonstrates abstraction using Python's abstract base classes.
# The UPI abstract class defines a generic pay method, which must be implemented by subclasses.

class UPI(ABC):
    @abstractmethod
    def pay(self, amount):
        # This method is abstract and must be implemented by any subclass.
        pass

# PhonePe implements the pay method with its specific logic.
class PhonePe(UPI):
    def pay(self, amount):
        print(f"Processing payment of {amount} via PhonePe...")
        print("Payment successful!")

# GooglePay also provides its own implementation of the pay method.
class GooglePay(UPI):
    def pay(self, amount):
        print(f"Processing payment of {amount} via GooglePay...")
        print("Payment successful!")

if __name__ == "__main__":
    # Using abstraction: we interact through the UPI base class,
    # making it easy to substitute different payment providers.
    upi_abstraction = PhonePe()
    upi_abstraction.pay(500)

    upi_abstraction = GooglePay()
    upi_abstraction.pay(1000)
