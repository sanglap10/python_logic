# Encapsulation Example in Python

class Mobile:
    def __init__(self, model, brand, price):
        # Private attributes (not directly accessible)
        self.__model = model
        self.__brand = brand
        self.__price = price

    # Public method to get the model
    def get_model(self):
        return self.__model

    # Public method to set the price
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

    # Public method to get the price
    def get_price(self):
        return self.__price

# Usage
mobile = Mobile("Galaxy S25", "Samsung", 999)
print("Model:", mobile.get_model())
print("Price:", mobile.get_price())

# Attempt to update the price
mobile.set_price(1099)
print("Updated Price:", mobile.get_price())

# Attempt to directly access private attributes (will fail)
# print(mobile.__price)  # This will raise an AttributeError
