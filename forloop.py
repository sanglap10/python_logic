arr = []
totalPeople = int(input("Enter total no of people: "))

for i in range(1,totalPeople+1):
    name = input(f"Enter name{i}: ")
    arr.append((name,i))
for n in arr:

    print(f"Hello {n[0]} your roll is {n[1]}")