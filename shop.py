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

def print_bill(customer_name,items):
    print(f"\nHello {customer_name}, here's your bill: ")
    print("Item Name        Price")
    print("--------------------------------------")

    total = 0
    for item in items:
        print(f"{item[0]:15}       {item[1]}")
        total = total + item[1]
        print("-----------------------------------")
    print(f"Total:           {total} ")


def main():
    cust_name = get_customer_name()
    items = get_itmes()
    print_bill(cust_name,items)

main()