student = []
total_students = int(input("Enter total number od student: "))

for i in range(0,total_students):
    name = input("\nEnter name: ")
    roll = int(input("Enter roll no: "))
    marks = float(input("Enter marks: "))

    student.append(
        {
            "name" : name,
            "rollno" : roll,
            "marks" : marks
        }
    )

print(student)
