import random

def randomNumber():
    numbers = [1,2,3,4,5]
    ran = random.choice(numbers)
    return ran
    
def getItems(total):
    items = []
    for i in range(total):
        item_name = input(f"\nEnter name for item {i+1}: ")
        item_price = int(input(f"Enter price of item {i+1}: "))
        items.append((item_name,item_price))
    return items

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
    name = input("Enter your name: ")
    num = randomNumber()
    print(f"Hello {name} you will buy {num} items\n")
    items = getItems(num)
    print_bill(name,items)

main()