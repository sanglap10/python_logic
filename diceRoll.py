import random

arr = [1,2,3,4,5,6]

def dice_roll():
    global arr
    computer_roll = random.choice(arr)
    return computer_roll

def main():

    print("\n Welcome to dice roll simulator")

    while True:
        

        num = int(input("\n Enetr 1 to roll the dice and 0 to quit: "))

        if num == 1:    
            rolled = dice_roll()
            print(f"\n Dice rolled: {rolled}")
        elif num == 0:
            break
        else:
            print("INVALID!")

main()