def get_customer_name():
    customer_name = input("Enter your name: ")
    return customer_name

def get_itmes():
    total_items = int(input("Enter total items you bought: "))
    arr = []
    for i in range(total_items):
        item_name = input("Enter item name: ")
        item_price = int(input("Enter price of item: "))
        arr.append((item_name,item_price))
    return arr

def print_bill(name,items):
    print(f"\nHello {name}, here's your bill: ")
    print("Item Name        Price")
    print("--------------------------------------")

    total = 0
    for item in items:
        print(f"{item[0]:15}       {item[1]}")
        total = total + item[1]
        print("-----------------------------------")
    print(f"Total:           {total} ")

    discount_amount = discount(total)
    print(f"Discount:        {discount_amount}")

    
def discount(bill_amount):
    discount = 0
    if bill_amount > 1000:
        discount = 0.1 * bill_amount
    elif bill_amount > 500:
        discount = 0.05 * bill_amount
    elif bill_amount > 200:
        discount = 0.02 * bill_amount
    else:
        discount = 0
    return discount


def main():
    cust_name = get_customer_name()
    items = get_itmes()
    print_bill(cust_name,items)
    less = discount()

main()