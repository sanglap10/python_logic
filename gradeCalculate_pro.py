def main():
    totalStudent = int(input("Enter number of student: "))
    for i in range(1,totalStudent+1):
        name = input(f"\nEnter name of student{i}: ")
        marks = int(input(f"Enter marks of {name}: "))
        totalMarks = int(input("Enter total marks: "))

        if marks > totalMarks:
            print("Marks cannot be greater than total marks !")
        else:
            grade = calculate_grade(marks)
            percentage = calculate_percentage(marks,totalMarks)

            print(f"{name} your grade is {grade} and percentage is {percentage}")

def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        return "A+"
    elif marks >= 80 and marks <=89:
        return "A"
    elif marks >= 70 and marks <= 79:
        return "B"
    elif marks >= 60 and marks <= 69:
        return "C"
    elif marks >= 30 and marks <= 59:
        return "D"
    else:
        return "FAIL"
        
    
def calculate_percentage(marks,totalMarks):
    percentage = (marks/totalMarks)*100
    return percentage

main()

