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
    for i in range(number,0,-1):
        fact *= i
        values.append(str(i))
    exps = " * ".join(values)
    print(f"{exps} = {fact}")


def main():
    while True:
        print("Enter 1 for fibonacci series")
        print("Enter 2 for find prime numbers")
        print("Enter 3 for sum of numbers")
        print("Enter 4 for sum of numbers while")
        print("Enter 5 for sum of numbers whitout loop")
        print("Enter 6 for factorial")

        choice = int(input("Enter choice: "))

        if choice == 7:
            break
        number = int(input("Enter number: "))

        if choice == 1:
            fibonacci_series(number)
            print(f"")
        elif choice == 2:
            if prime_number(number):
                print(f"{number} is prime number")
            else:
                print(f"{number} is not prime")
        elif choice == 3:
            sum_of_numbers(sum)
        elif choice == 4:
            sum_of_numbers_while(number)
        elif choice == 5:
            sum_of_numbers_formula(number)
        elif choice == 6:
            factorial_of_numbers(number)
        else:
            print("Invalid")
    
main()
        
        
        