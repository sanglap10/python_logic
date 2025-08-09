def PrintMessage(name,grade):
     print(f"Hello {name}, good morning. Your grade is {grade}!")

name = input("Enter your name: ")
marks = input("Enter your marks: ")
m = int(marks)

if m >= 90:
     PrintMessage(name,"A")
elif m >= 70:
     PrintMessage(name,"B")
elif m >= 60:
     PrintMessage(name,"C")
elif m >= 40:
     PrintMessage(name,"D")
else:
     PrintMessage(name,"F")

