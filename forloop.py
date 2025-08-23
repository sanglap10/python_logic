arr = []
totalPeople = int(input("Enter total no of people: "))

for i in range(0,totalPeople):
    name = input(f"Enter name{i}: ")
    
    arr.append(name)
print(arr)
    #print(f"Hello {name}!")