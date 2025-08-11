def main():

    numbers = []
    for i in range(1,4):
        num = int(input(f"Enter number{i}: "))
        numbers.append(num)

    number1, number2, number3 = numbers
    result = largest_num(number1,number2,number3)
    print(f"{result} is the largest number !")

def largest_num(number1,number2,number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number1 and number2 >= number3:
        return number2
    else:
        return number3
    
main()
