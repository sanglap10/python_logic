def fibonacci_series(number):
    a = 0
    b = 1

    for i in range(number):
        print(a)
        t = a
        a = b
        b = b + t 

    print("Fibonacci series")


def prime_number(number):
    if number < 1:
        return False
    
    for i in range(2,number):
        if number % i == 0:
            return False
    return True        


def sum_of_numbers(number):
    numbers = []
    sum = 0

    for i in range(1,number+1):
        sum += i
        numbers.append(str(i))
    exp = " + ".join(numbers)
    print(f"{exp} = {sum}")

def sum_of_numbers_while(number):
    i = 1
    elements = []
    sum = 0
    while i <= number:
        sum += i
        elements.append(str(i))
        i += 1
    exp = " + ".join(elements)
    print(f"{exp} = {sum}")


def sum_of_numbers_formula(number):
    sum = (number * (number + 1))//2
    print(f"Sum is {sum}")


def factorial_of_numbers(number):
    fact = 1
    values = []
    for i in range(1,number+1):
        z = number - i + 1 

        fact *= i
        values.append(str(z))
    exps = " * ".join(values)
    print(f"{exps} = {fact}")


def factorial_while(number):
    fact = 1
    num = []
    i = 1
    while i <= number:
        fact = fact * i
        z = number - i + 1
        num.append(str(z))
        i = i + 1
    exps = " * ".join(num)
    print(f"{exps} = {fact}")


def main():
    while True:
        print("Enter a choice 1 - 8")
        print("1. Fibonacci series")
        print("2. Prime numbers")
        print("3.  Sum of numbers")
        print("4. Sum of numbers using while loop")
        print("5. Sum of numbers whitout loop")
        print("6. Factorial of number")
        print("7. Factorial of number using while loop")
        print("8. Exit")
        choice = int(input("Enter choice: "))
        number = int(input("Enter number: "))

        match choice:
            case 1:
                fibonacci_series(number)
            case 2:
                if prime_number(number):
                    print(f"{number} is prime number")
                else:
                    print(f"{number} is not prime")
            case 3:
                sum_of_numbers(sum)
            case 4:
                sum_of_numbers_while(number)
            case 5:
                sum_of_numbers_formula(number)
            case 6:
                factorial_of_numbers(number)
            case 7:
                factorial_while(number)
            case 8:
                break
main()
        
        
        