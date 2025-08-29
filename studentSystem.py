students = []
subjects = []


def add_students():
    global students
    total_student = int(input("\n Enter total number of students: "))

    counter = 0
    for i in range(0,total_student):
        counter = counter + 1
        name = input(f"\n Enter name for student {counter}: ")
        rollNo = int(input(f"Enter roll no of students {counter} : "))
        email = input(f"Enter email of student {counter}: ")

        students.append({
            "name" : name,
            "rollNo" : rollNo,
            "email" : email
        })

    print("\n Students sucessfully added!")

def remove_student():
    print("remove_student")

def add_subjects():
    global subjects
    total_subjects = int(input("\n Enter total nunber of subjects: "))
    for i in range(1,total_subjects + 1):
        sub_id = int(input(f"\n Enter id of subject {i}: "))
        name = input(f"Enter subject name {i}: ")

        subjects.append({
            "subid" : sub_id,
            "name" : name
        })

    print("\n Subjects sucessfully added!")

def add_marks():
    global students , subjects

    roll = int(input("\n Enter roll no: "))

    student = None
    for stu in students:
        if stu["rollNo"] == roll:
            student = stu
            break
    
    for sub in subjects:
        marks = int(input(f"Enter marks for {sub["name"]}: "))
        student["marks"][sub["name"]] = marks
    
    print("\n Marks added!")

    

def view_all_students_with_marks():
    print("view_all_students_with_marks")

def search_student_by_rollno():
    print("search_student_by_rollno")

def main():
    while True:
        print("\n Welcome to student system !")
        print("1.Add students")
        print("2.Remove student")
        print("3.Add subjects")
        print("4.Add marks")
        print("5.View all students with marks")
        print("6.Search student by roll no")

        choice = int(input("\n Enter choice: "))

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