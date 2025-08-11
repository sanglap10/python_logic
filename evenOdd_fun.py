def main():
    number = int(input("Enter a number: "))
    num = Even_Odd(number)
    print(f"{number} is {num} !")

def Even_Odd(number):
    if number % 2 == 0:
        return "EVEN"
    else :
        return "ODD"

main()    