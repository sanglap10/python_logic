students = []
subjects = []


def add_students():
    global students
    total_student = int(input("Enter total number of students: "))
    for i in range(1,total_student):
        name = input("Enter name:")
        rollNo = int(input("Enter roll no: "))
        email = input("Enter email: ")

        students.append({
            "name" : name,
            "rollNo" : rollNo,
            "email" : email
        })

def remove_student():
    print("remove_student")

def add_subjects():
    global subjects
    total_subjects = int(input("Enter total nunber of subjects: "))
    for i in range(1,total_subjects):
        sub_id = int(input("Enter subject id: "))
        name = input("Enter subject name: ")

        subjects.append({
            "subid" : sub_id,
            "name" : name
        })

def add_marks():
    roll = int(input("Enter roll no: "))
    if roll in students:
        for s in range(1,subjects):
            marks = int(input(f"Enter marks for {s}1: "))


def view_all_students_with_marks():
    print("view_all_students_with_marks")

def search_student_by_rollno():
    print("search_student_by_rollno")

def main():
    while True:
        print("Welcome to student system !")
        print("1.Add students")
        print("2.Remove student")
        print("3.Add subjects")
        print("4.Add marks")
        print("5.View all students with marks")
        print("6.Search student by roll no")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_students()
        elif choice == 2:
            remove_student()
        elif choice == 3:
            add_subjects()
        elif choice == 4:
            add_marks()
        elif choice == 5:
            view_all_students_with_marks()
        elif choice == 6:
            search_student_by_rollno()
        elif choice == 7:
            break
        else:
            print("Invalid choice!")

main()