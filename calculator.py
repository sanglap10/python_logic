def addition(num1,num2):
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")

def subtraction(num1,num2):
    sub = num1 - num2
    print(f"{num1} - {num2} = {sub}")

def multiplication(num1,num2):
    mul = num1 * num2
    print(f"{num1} * {num2} = {mul}")

def division(num1,num2):
    div = num1 / num2
    print(f"{num1} / {num2} = {div}")

def main():
    print("Calculator")
    while True:
        
        print("Enter 1 for addition")
        print("Enter 2 for subtraction")
        print("Enter 3 for multiplication")
        print("Enter 4 for division")
        print("Enter 5 for exit")

        choice = int(input("Enter choice: "))

        if choice == 5:
            break

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == 1:
            addition(num1,num2)
        elif choice == 2:
            subtraction(num1,num2)
        elif choice == 3:
            multiplication(num1,num2)
        elif choice == 4:
            division(num1,num2)
        else:
            print("Invalid choice !")

main()


