def CalculateTax(tax,price):
    amount = tax / 100 * price
    return amount

def FinalPrice(tax,price):
    finalAmount = tax + price
    print(f"The final price is {finalAmount}")

price = int(input("Enter price of Bike: "))

if price >= 100000:
    tax = CalculateTax(15,price)
    FinalPrice(tax,price)
elif price >= 50000 and price <= 100000:
    tax = CalculateTax(10,price)
    FinalPrice(tax,price)
elif price <= 50000:
    tax = CalculateTax(5,price)
    FinalPrice(tax,price)
else:
    print("invalid!")