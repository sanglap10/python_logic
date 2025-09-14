import random

def main():
    name = input("Enter your name: ")
    dice = dice_roll()
    print(f"Hello {name} you rolled {dice}")
    items = shop(dice)
    print_bill(name,items)
     

def dice_roll():
    dice = [1,2,3,4,5,6]
    computer_choice = random.choice(dice)
    return computer_choice
    
def shop(total_items):
    items = []
    for i in range(total_items):
        items_name = input("Enter items name: ")
        items_price = int(input("Enter items price: "))
        items.append((items_name,items_price))
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


main()