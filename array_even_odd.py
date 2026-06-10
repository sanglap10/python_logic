arr = []
total = int(input("Enter total number: "))

def getData():
    for i in range(0,total):
        num = int(input(f"Enter number {i}: "))
        arr.append(num)

def checkEvenOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

getData()

for i in arr:
    if checkEvenOdd(i) == "Even":
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")



# 1. create an array
# 2. get total number of elements to be added in array
# 3. get the number from user and add it to array
# 4. check if the number is even or odd
# 5. display the result


