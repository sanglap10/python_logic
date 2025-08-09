name = input("Enter your name: ")
age = input("Enter your age: ")
a = int(age)

if a >= 18:
    print(f"Hi {name} you are eligible for vote!")
else:
    print(f"Hi {name} you are not eligible for vote!")
    