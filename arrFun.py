arr = []
total_students_num = int(input("Enter total number of students: "))

for i in range(0,total_students_num):
    name = input(f"Enter name of student {i}: ")
    arr.append(name)

counter = 0
for j in arr:
    counter = counter + 1
    print(f"Hello {j} your token no is {counter}")