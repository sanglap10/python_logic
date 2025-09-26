from abc import ABC, abstractmethod

class UPI(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PhonePe(UPI):
    def pay(self, amount):
        print(f"Processing payment of {amount} via PhonePe...")
        print("Payment successful!")

class GooglePay(UPI):
    def pay(self, amount):
        print(f"Processing payment of {amount} via GooglePay...")
        print("Payment successful!")

if __name__ == "__main__":
    upi_abstraction = PhonePe()
    upi_abstraction.pay(500)

    upi_abstraction = GooglePay()
    upi_abstraction.pay(1000)