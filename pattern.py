def pattern():
    a = int(input("Enter rows: "))

    for i in range(a,0,-1):
        for j in range(i):
            print("*",end = "")
        print("")

    for i in range(1,a+1):
        for j in range(i):
            print("*",end = "")
        print("")

def pyramid(n):
    star = 1
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(star):
            print("*",end="")
        print()
        star += 2

pyramid(10000)
