def main():
    totalStudents = int(input("Enter number of student : "))

    for i in range(1,totalStudents+1):
        student = input(f"Enter name of student {i}: ")
        marks = int(input(f"Enter marks for {student}: "))
        grade = CalculateGrade(marks)
        print(f"{student} scored {marks} and got {grade}")

def CalculateGrade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75 and marks >= 89:
        return "A"
    elif marks >= 60 and marks >= 74:
        return "B"
    elif marks >= 50 and marks >= 59:
        return "C"
    else :
        return "FAIL !"

print("Wellcome to grade calculate system!")
main()
