def for_loop(number):
    for i  in range(1,11):
        print(f"{number} x {i} = {number*i}")


def while_loop(number):
    i = 1
    while i < 11:
        print(f"{number} x {i} = {number*i}")
        i = i + 1

def main():
    number = int(input("Enter a number: "))
    while_loop(number)

main()
    